# Slide 23 — Network lineage: what each stage lost

**Timing:** 57–60 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content

| Stage | IDS/IPS on the plaintext web (2000s) | After HTTPS, TLS 1.3, DoH and ECH |
| --- | --- | --- |
| sensor | A tap or inline appliance at the perimeter | The same tap, plus the endpoint and the identity provider |
| acquisition | Full packets, kept for hours or days | Flow and DNS metadata for months; packets only behind a decryption proxy |
| extraction | Protocol parsing and file carving from the stream | Decryption at a proxy (pinning, privacy, performance costs), or nothing |
| representation | Payload bytes and strings | Endpoints, timing, volume, TLS fingerprints (JA3 2017, JA4 2023) |
| detection | Content rules on exploits, downloads and beacons (Snort) | Metadata rules, beaconing and anomaly models, reputation |
| investigation | Replay the capture | Flow timelines joined to endpoint and identity events |
| decision and response | Block inline | Block destinations; isolate from the endpoint |
| challenge | Encryption removed the payload (HTTPS by default, 2015 onward), the certificate (TLS 1.3, 2018), the lookup (DoH, 2018 onward) and the server name (ECH, browsers 2023) | Lower specificity; east-west SMB, Kerberos, LDAP and scanning still visible; plaintext survives on the endpoint |

> The sensor stayed where it was. Extraction failed, and everything below it was rebuilt on metadata or moved to the endpoint.
> Scenario check: the network sees a TLS connection to an unfamiliar host and, with DNS over HTTPS, not even the lookup; the shellcode download and the document upload are inside the tunnel. The endpoint sees the process that opened the connection and the plaintext before encryption.

## Speaker notes

Read the table as the twin of the host and file table, with one difference: the sensor row stayed where it was. What failed was extraction. The appliance still sees every packet and can no longer open them, so everything below extraction had to be rebuilt on metadata, and the content-level questions moved to the endpoint and the identity provider. What encryption hides from payload inspection (strings, transferred code and documents, application commands, content signatures, archive contents) remains observable somewhere else: endpoints and DNS activity, timing and volume, TLS properties, the process-to-connection relationship, and the plaintext on the endpoint itself. Next and Previous step through the stages one at a time, with the two eras side by side; clicking a stage on the strip jumps to it, and the table button shows the whole matrix.

Defenders had three responses:

1. **Decrypt in the middle.** A TLS inspection proxy restores payload visibility for north-south web traffic, but it breaks certificate pinning, raises privacy and legal questions, costs performance, and becomes a high-value target holding every session in plaintext.
2. **Move to metadata.** Network detection and response products use endpoints, timing, volume, and TLS fingerprints such as JA3 and JA4. These answer different questions with lower specificity.
3. **Move the sensor to the endpoint.** The plaintext still exists where the process encrypts and decrypts it. EDR observes the process, the connection, and the content before encryption.

Be precise about what survived. East-west internal traffic is often still plaintext or inspectable: SMB, Kerberos, LDAP, and remote-management protocols, which is exactly where lateral movement and credential abuse happen. Scanning, DNS without encryption, and beacon timing remain visible. North-south payload signatures are what lost most of their value without decryption. The XCPE takedown of November 2026 is this lineage working: a firmware botnet in 1.3 million set-top boxes, which no endpoint agent could see, was found from the network side by a home-WiFi vendor and a carrier's research team, and taken down at its control domains.

In the recurring scenario, TLS may conceal the downloaded payload and the uploaded content from an intermediate network sensor. The endpoint may still observe PowerShell, the network retrieval, the document access and the memory activity; metadata and endpoint context answer different questions and often with lower specificity.

## Interaction

Ask whether the organization in the recurring scenario would see the shellcode download or the document upload from a network sensor, then what it would see from the endpoint; the last Next shows the answer.

## Transition

“Two pipelines, one pattern: the evidence moved and the sensor followed. Now every change from Part 1 on one list, with the stage it broke and the product that answered.”

## Sources

- [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [RFC 8484: DNS Queries over HTTPS](https://www.rfc-editor.org/rfc/rfc8484)
- [RFC 9849: TLS Encrypted Client Hello](https://www.rfc-editor.org/rfc/rfc9849.html)
