# ADR-0001

## Title

All Major FRIDAY Subsystems Shall Be Runtime Services

---

## Status

Accepted

---

## Date

2026-08-03

---

## Context

As FRIDAY grows, major capabilities such as Doctor, Echo,
Halo, Archive, Atlas, and future integrations require a
consistent lifecycle.

Without a common lifecycle, each subsystem would implement
its own startup, shutdown, and health reporting logic,
leading to duplicated code and inconsistent behavior.

---

## Decision

Every major FRIDAY subsystem shall inherit from the
Service base class.

Every Service must implement:

- start()
- stop()
- health_report()

Runtime is responsible for starting and stopping Services.

Subsystems are responsible only for their own behavior.

---

## Consequences

Positive:

- Consistent lifecycle
- Consistent health reporting
- Runtime remains simple
- Easy integration
- Predictable architecture
- Supports graceful degradation

Tradeoffs:

- Small amount of boilerplate for every Service.

This tradeoff is accepted because it significantly improves
long-term maintainability.

---

## Future

The Service Loader will automatically discover and register
Services, eliminating the need to manually modify Runtime
when new subsystems are added.