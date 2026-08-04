# F.R.I.D.A.Y.
# Software Architecture Specification

Version: 0.3.0

Release: Awakening

Author:
Shae Simpson & OpenAI ChatGPT

---

# Purpose

This document defines the official software architecture of
F.R.I.D.A.Y.

Its purpose is to ensure the project remains consistent,
maintainable, and expandable as it grows.

Whenever there is uncertainty about where code belongs,
this document is considered the source of truth.

---

# Philosophy

FRIDAY is built as a long-term software product.

Priorities:

1. Reliability
2. Readability
3. Maintainability
4. Expandability
5. Simplicity

Every component should have one responsibility.

No unnecessary complexity.

No duplicated logic.

No circular dependencies.

---

# Overall Architecture

```
Application
      │
      ▼
Infrastructure
      │
      ▼
Framework
      │
      ▼
Subsystems
      │
      ▼
Capabilities
```

Each layer may only depend on layers below it.

Never upward.

---

# Infrastructure

Infrastructure contains reusable building blocks.

Infrastructure does not contain assistant logic.

Examples:

- Console
- Event Bus
- Configuration
- Registry
- Logging
- Metrics

Infrastructure should be reusable outside of FRIDAY.

---

# Framework

Framework coordinates infrastructure.

Examples:

- Runtime
- Service
- Collector
- Service Loader

Framework manages execution.

Framework does not perform assistant tasks.

---

# Subsystems

Subsystems provide major assistant functionality.

Examples:

- Doctor
- Echo
- Halo
- Archive
- Atlas

Subsystems communicate through:

- Events
- Services
- Configuration

Subsystems should never directly depend upon one another.

---

# Capabilities

Capabilities are user-facing features.

Examples:

- Apple Music
- HomeKit
- Weather
- Calendar
- Email
- Safari
- Recipes

Capabilities plug into subsystems.

Capabilities never modify the Runtime.

---

# Runtime Responsibilities

Runtime owns:

- Startup
- Shutdown
- Runtime State
- Core Services
- Service Registry
- Service Loader

Runtime should remain small.

Runtime should never contain business logic.

---

# Core Services

Core Services owns:

- Event Bus
- Configuration
- Console

Future additions:

- Logger
- Metrics
- Scheduler
- Plugin Manager

Only one instance of each Core Service exists.

---

# Services

Every major subsystem shall inherit from Service.

Every Service must implement:

- start()
- stop()
- health_report()

Services are registered with the Runtime.

---

# Doctor

Doctor is responsible only for diagnostics.

Doctor coordinates Collectors.

Doctor does not perform diagnostics itself.

Each Collector is responsible for exactly one area.

Examples:

- Runtime
- Memory
- Network
- Bluetooth
- Camera
- Microphone

Doctor combines their reports.

---

# Event Bus

The Event Bus is the communication backbone.

Subsystems communicate through events.

Avoid direct subsystem references whenever possible.

---

# Configuration

Configuration is owned by Core Services.

Subsystems read configuration.

Subsystems do not create configuration managers.

---

# Dependency Rules

Allowed:

Runtime

↓

Core Services

↓

Subsystems

↓

Capabilities

Not Allowed:

Capability

↓

Runtime

Subsystem

↓

Subsystem

Infrastructure

↓

Subsystem

---

# Engineering Rules

Every file shall contain:

- Header
- Purpose
- Author
- Version

Every public function shall contain:

- Type hints
- Docstrings

Every module shall have one responsibility.

---

# Release Process

Every milestone follows:

Architecture

↓

Implementation

↓

Integration

↓

Testing

↓

Git Commit

↓

Release

No milestone is complete until all six steps succeed.

---

# Vision

FRIDAY is designed to become a dependable,
voice-first digital assistant capable of managing
personal productivity, home automation,
knowledge, and intelligent decision support.

The architecture should allow new capabilities
to be added without requiring rewrites of
existing subsystems.

Every architectural decision should support
that long-term goal.