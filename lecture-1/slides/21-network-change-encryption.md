# Slide 21 — The network changed under the sensor: HTTPS, TLS 1.3, DoH, ECH

**Timing:** 55–57 minutes  
**Module:** Detection pipelines: design and evolution

## On-slide content
![Share of page loads over HTTPS, late 2015 to 2026: Firefox globally and in the United States, Chrome on Windows and on Mac, from about 40 percent to above 90; the four protocol steps that removed fields from the network sensor marked one at a time](../figures/https-chart.svg)

Build, one step per click:

0. Share of page loads over HTTPS: Firefox globally and in the United States, Chrome on Windows and on Mac. About 40 percent in late 2015, half by late 2016, around 70 in early 2018, above 80 by 2020; Chrome on Windows passes 90 in 2021 while Firefox's global figure plateaus near 80–84, a regional mix.
1. HTTPS by default (Let's Encrypt, 2015 onward) removed the payload content from the network sensor.
2. TLS 1.3 (2018) removed the server certificate in the clear.
3. DNS over HTTPS (2018 onward) removed the lookup before the connection.
4. Encrypted Client Hello (browsers 2023, RFC 9849 in 2026, few servers) removed the server name in the handshake.

> A payload signature cannot match content it never sees. The window has been closing one field at a time.

| Step | What it removed from the network sensor |
| --- | --- |
| HTTPS by default (Let's Encrypt, 2015 onward) | Payload content |
| TLS 1.3 (2018) | Server certificate in the clear |
| DNS over HTTPS (2018 onward) | The lookup before the connection |
| Encrypted Client Hello (browsers 2023, RFC 9849 in 2026, few servers) | The server name in the handshake |

## Talking points

- Content rules were built for plaintext; in about five years encrypted page loads went from roughly 40 to roughly 90 percent.
- Each protocol step removed one more field: the payload, the certificate, the lookup, the server name.
- Two minutes: the curve, the four steps, the callout.

## Speaker notes

Network intrusion detection and prevention systems were built when most web traffic was plaintext. Content rules matched exploit strings, downloaded executables, and command-and-control beacons in the payload. Let's Encrypt made certificates free and automated in late 2015, Chrome began marking every plaintext page "Not secure" in July 2018, and within about five years encrypted page loads went from about 40 percent to roughly 90 percent in the United States and on Chrome desktop. Firefox's global average plateaued in the low eighties because of its regional mix, which is why the slide names the browser and region for each figure. The figures were checked in October 2026 against Mozilla's ssl_ratios telemetry dataset and the Google Transparency Report data; Google's own publications gave 51 to 53 percent for Chrome on Windows in October 2016, so the slide rounds down.

The sequence after that matters as much as the first step. Each protocol improvement was good for users and removed one more row of this table from the network sensor's view: TLS 1.3 encrypts the certificate, DNS over HTTPS hides the lookup, and Encrypted Client Hello hides the server name.

This slide is the cause; the next one is the effect, stage by stage. Keep it to two minutes: the curve, the four steps, the callout.

## Transition

“That is the change. Now what it did to each stage of the network pipeline.”

## Sources

- [Google Transparency Report: HTTPS encryption on the web](https://transparencyreport.google.com/https/overview)
- [Let's Encrypt statistics (Firefox telemetry, percentage of page loads over HTTPS)](https://letsencrypt.org/stats/)
- [Google Security Blog: HTTPS encryption on the web, 2016](https://security.googleblog.com/2016/10/https-encryption-on-web.html)
- [Mozilla telemetry: ssl_ratios dataset reference](https://docs.telemetry.mozilla.org/datasets/other/ssl/reference.html)
- [Let's Encrypt: HTTPS progress, June 2016 (39.5 percent at launch)](https://letsencrypt.org/2016/06/22/https-progress-june-2016)
- [Chromium Blog: Towards HTTPS by default (2023)](https://blog.chromium.org/2023/08/towards-https-by-default.html)
- [RFC 9849: TLS Encrypted Client Hello](https://www.rfc-editor.org/rfc/rfc9849.html)
- [RFC 8446: TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [RFC 8484: DNS Queries over HTTPS](https://www.rfc-editor.org/rfc/rfc8484)
- [IETF TLS Encrypted Client Hello draft](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/)
