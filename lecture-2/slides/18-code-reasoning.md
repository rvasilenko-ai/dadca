# Slide 18 — Code reasoning

**Timing:** 43–46 minutes  
**Module:** Why the agent succeeded

## On-slide content

The agent must reason about:

- Source and configuration
- APIs and data formats
- Error messages
- Trust assumptions
- Vulnerability composition
- Intended and unintended behavior

> “Works as implemented” is different from “works as intended.”

## Speaker notes

An attacker does not need a feature to be documented as security-sensitive. If code permits a useful behavior, the agent can treat it as another operation in its search space.

The incident combined familiar weaknesses whose consequences were not obvious when each component was considered in isolation. Code understanding allowed local observations to become hypotheses about the next system.

## Transition

“Understanding the opportunity is insufficient if the model cannot operate the surrounding tools.”

