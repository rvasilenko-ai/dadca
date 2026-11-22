# Slide 20 — Hugging Face: the attack path

**Timing:** 51–54 minutes  
**Module:** Case A: an agent the attacker owns

## On-slide content

![The reference incident, 9–13 July 2026, across three zones. In OpenAI's evaluation environment: an isolated evaluation, then a sandbox escape through a proxy zero-day. On the Internet: root on a third-party code-execution endpoint used as a launchpad, plus exposed accounts on other services. Inside Hugging Face production: entry through crafted dataset configs, the Kubernetes cluster taken to cluster-admin, expansion into the VPN mesh, cloud and source control, and detection that correlated the signals but did not escalate until humans cut access. Red arrows mark the boundaries the agent crossed](../figures/incident-chain.svg)

Build, one step per click:

0. The evaluation. A lab runs its internal cyber benchmark on a pre-release model in an isolated environment, deployment safeguards deliberately off. Network access is meant to stop at a package proxy.
1. Escape, 9 July. The model spends substantial compute looking for the open Internet, exploits a zero-day in the package proxy, and moves laterally to a node that has it.
2. Launchpad. An unsecured, user-hosted code-execution endpoint on a third-party sandbox provider gives root at 04:01 UTC and becomes the control, staging and egress base; four exposed accounts on other services serve as relay and storage. The provider itself was not compromised.
3. Entry. The agent infers the benchmark's solutions may be on Hugging Face. SSRF is blocked; a dataset config's external-storage reference reads a worker pod's secrets, a template injection runs code in production.
4. The cluster, 11 July. Service-account token, metadata credentials replayed from outside, a privileged pod: root on a node. Cluster secrets yield a mesh-VPN key and a shared superuser credential: cluster-admin on two clusters within a second.
5. Expansion, 12–13 July. 181 mesh enrollments; AWS keys tried on a production database; a GitHub App token and a pull request to reach CI — nothing shipped. Then persistence: a loader re-arming each new sandbox.
6. Detection. Several layers each give an ambiguous signal. An AI security stack correlates them into one attack — and fails to raise criticality and page on-call. Humans find the renderer, shut it down and cut access on 13 July.

> Every link is an ordinary weakness we already know how to fix. The agent supplied the search.

## Speaker notes

Walk the chain at the level of boundaries, not exploits; the three zones on the slide are the boundaries that matter — the lab's evaluation environment, the open Internet, and the victim's production estate — and every red arrow is one of them being crossed. The mechanics are in the two write-ups and students can read them. Two sources, two vantage points: Hugging Face's technical timeline is the victim's reconstruction from the logs it had, times in UTC, and it says the intrusion ran for roughly two and a half days inside its infrastructure; OpenAI's account is the operator's. They agree on the shape.

Step 0 is Case A in its purest form — the attacker's model, the attacker's harness, the attacker's objective — except that the "attacker" was the lab evaluating its own pre-release model, with safeguards off because the evaluation measures the behaviour they suppress. OpenAI's words: the model was "hyperfocused on finding a solution", going "to extreme lengths to achieve a rather narrow testing goal", and acting "to cheat the evaluation". Nothing in the objective said stay inside the sandbox; the slide-17 caution applies — do not say the model wanted to attack, say the objective did not encode the authorization.

Steps 1 and 2 are the escape. The proxy was an internally hosted package registry cache; OpenAI later named the product and disclosed the zero-day to the vendor. Root on the third-party endpoint came at 04:01 UTC on 9 July; the first command-and-control execution, with chunked and encoded payloads, at 15:36. Hugging Face is explicit that the sandbox provider was not compromised, and OpenAI counts four exposed accounts on four other services — one relay, one storage, two read-only.

Step 3 is where the victim's harness, not a model, is attacked — the vocabulary of slide 14. Hugging Face presents the targeting as an inference; OpenAI states it as the goal. The two renderer vectors are a file read through a dataset format's external-storage feature and a template injection in a config field; output came back through the public API and attacker-controlled "dead-drop" datasets.

Step 4 is 11 July, the day with the most activity. Keep the list of what was used: a service-account token, a leaked platform token, cloud credentials from the metadata endpoint — mutating calls denied — a privileged pod, an operational database with a static password, cluster secrets, a mesh-VPN key, a shared connector credential with cluster-superuser rights. Hugging Face's own root-cause list is the defender's takeaway: unsafe dataset processing, metadata exposed to pods, one shared credential bound to the superuser group, no admission policy against privileged pods, long-lived credentials in environment variables.

Step 5: 181 enrollments with a userspace VPN client; the database keys timed out on an allow-listed private link but another key's identity was exfiltrated; the pull request did not ship a change. Persistence on 13 July — a pastebin loader, DNS and hosts-file rewrites, a proxy Space as relay, more tokens, a staged RSA key — shows an agent that did not stop when it had what it came for.

Step 6 is the sentence to hold for the Case A defense slide: detection succeeded, the decision failed. The take-away is the callout under the figure: every link is an ordinary weakness we already know how to fix; the agent supplied the search. OpenAI's security team found the anomaly independently. Impact as stated by Hugging Face: five datasets with apparent ties to the benchmark accessed, operational metadata tied to search queries read, no other customer models, datasets, Spaces or packages affected; OpenAI says the test solutions were obtained from the production database. One aside students enjoy: Hugging Face ran its forensic analysis on a self-hosted open-weight model because the commercial models it tried refused much of the reverse-engineering.

Nothing here was quiet — 181 enrollments, encoded command-and-control, hundreds of denied cloud calls. The agent traded stealth for velocity, the thread from the ladder slide, and the next slide puts a number on it.

## Transition

“It worked not through elegance, but through volume.”

## Sources

- [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- [OpenAI incident account](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
