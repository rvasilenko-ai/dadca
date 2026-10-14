#!/usr/bin/env python3
"""Drive a long-lived headless Chrome over the DevTools protocol with stdlib only.
Usage: screenshot.py PORT URL OUTDIR SLIDE[:fK][:dark][:click=<css selector without colons>] ...
Writes OUTDIR/sNN[-fK][-dark].png and prints console errors."""
import base64, json, os, socket, struct, sys, time, urllib.request

port, url, outdir = int(sys.argv[1]), sys.argv[2], sys.argv[3]
specs = sys.argv[4:]
os.makedirs(outdir, exist_ok=True)

# ---- wait for chrome
deadline = time.time() + 300
ws_url = None
while time.time() < deadline:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=3) as r:
            info = json.load(r)
        break
    except Exception:
        time.sleep(2)
else:
    sys.exit("chrome did not come up")
# new page target
req = urllib.request.Request(f"http://127.0.0.1:{port}/json/new?about:blank", method="PUT")
with urllib.request.urlopen(req, timeout=10) as r:
    target = json.load(r)
ws_url = target["webSocketDebuggerUrl"]
host, rest = ws_url[len("ws://"):].split("/", 1)
h, p = host.split(":")

# ---- minimal websocket client
sock = socket.create_connection((h, int(p)), timeout=120)
key = base64.b64encode(os.urandom(16)).decode()
sock.sendall((f"GET /{rest} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
              f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
resp = b""
while b"\r\n\r\n" not in resp:
    resp += sock.recv(4096)
assert b" 101 " in resp.split(b"\r\n")[0], resp

def send(obj):
    data = json.dumps(obj).encode()
    hdr = bytearray([0x81])
    n = len(data)
    if n < 126: hdr.append(0x80 | n)
    elif n < 65536: hdr += bytes([0x80 | 126]) + struct.pack(">H", n)
    else: hdr += bytes([0x80 | 127]) + struct.pack(">Q", n)
    mask = os.urandom(4)
    hdr += mask
    sock.sendall(bytes(hdr) + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))

def recv_exact(n):
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(min(1 << 20, n - len(buf)))
        if not chunk: raise ConnectionError("socket closed")
        buf += chunk
    return buf

def recv_msg():
    payload = b""
    while True:
        b1, b2 = recv_exact(2)
        fin, op = b1 & 0x80, b1 & 0x0F
        n = b2 & 0x7F
        if n == 126: n = struct.unpack(">H", recv_exact(2))[0]
        elif n == 127: n = struct.unpack(">Q", recv_exact(8))[0]
        if b2 & 0x80: mask = recv_exact(4)
        else: mask = None
        data = recv_exact(n)
        if mask: data = bytes(b ^ mask[i % 4] for i, b in enumerate(data))
        if op == 9:  # ping -> pong
            sock.sendall(bytes([0x8A, 0x80]) + b"\x00\x00\x00\x00"); continue
        if op == 8: raise ConnectionError("closed by peer")
        payload += data
        if fin: return json.loads(payload.decode())

msg_id = 0
events = []
def call(method, params=None, timeout=60):
    global msg_id
    msg_id += 1
    send({"id": msg_id, "method": method, "params": params or {}})
    t0 = time.time()
    while True:
        m = recv_msg()
        if m.get("id") == msg_id:
            if "error" in m: raise RuntimeError(f"{method}: {m['error']}")
            return m.get("result", {})
        events.append(m)
        if time.time() - t0 > timeout: raise TimeoutError(method)

def drain(seconds):
    sock.settimeout(seconds)
    try:
        while True:
            events.append(recv_msg())
    except (socket.timeout, TimeoutError):
        pass
    finally:
        sock.settimeout(120)

call("Page.enable"); call("Runtime.enable"); call("Log.enable")
call("Emulation.setDeviceMetricsOverride", {"width": 1280, "height": 720, "deviceScaleFactor": 1, "mobile": False})
call("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-color-scheme", "value": "light"}]})
call("Page.navigate", {"url": url})
drain(4)

def errors():
    out = []
    for e in events:
        if e.get("method") == "Runtime.exceptionThrown":
            d = e["params"]["exceptionDetails"]; out.append("EXC " + (d.get("exception", {}).get("description") or d.get("text", ""))[:300])
        if e.get("method") == "Log.entryAdded" and e["params"]["entry"].get("level") == "error":
            out.append("LOG " + e["params"]["entry"].get("text", "")[:300])
        if e.get("method") == "Runtime.consoleAPICalled" and e["params"].get("type") == "error":
            out.append("CON " + " ".join(str(a.get("value", a.get("description", ""))) for a in e["params"]["args"])[:300])
    events.clear(); return out

for err in errors(): print("  ", err)
ready = call("Runtime.evaluate", {"expression": "typeof Reveal !== 'undefined' && Reveal.isReady() && document.querySelectorAll('.reveal .slides section').length", "returnByValue": True})
print("reveal ready; sections:", ready["result"].get("value"))

for spec in specs:
    parts = spec.split(":")
    n = int(parts[0]); frag = None; dark = False; click = None
    for p in parts[1:]:
        if p == "dark": dark = True
        elif p.startswith("click="): click = p[6:]
        elif p.startswith("f"): frag = int(p[1:])
    call("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-color-scheme", "value": "dark" if dark else "light"}]})
    call("Runtime.evaluate", {"expression": f"document.documentElement.removeAttribute('data-theme'); Reveal.slide({n-1}, 0, {frag if frag is not None else -1}); true", "awaitPromise": False})
    drain(0.9)
    if click:
        hit = call("Runtime.evaluate", {"expression": "(function(){var e=document.querySelector(" + json.dumps(click) + "); if(!e) return 'no match'; e.dispatchEvent(new MouseEvent('click',{bubbles:true})); return 'clicked';})()", "returnByValue": True})
        print("  click", click, "->", hit["result"].get("value"))
        drain(0.5)
    shot = call("Page.captureScreenshot", {"format": "png"})
    name = f"s{n:02d}" + (f"-f{frag}" if frag is not None else "") + ("-click" if click else "") + ("-dark" if dark else "") + ".png"
    with open(os.path.join(outdir, name), "wb") as f: f.write(base64.b64decode(shot["data"]))
    errs = errors()
    print(name, "ok" + (" | " + "; ".join(errs) if errs else ""))
print("done")
