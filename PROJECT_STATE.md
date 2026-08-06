# F.R.I.D.A.Y.
## Project State

**Project:** F.R.I.D.A.Y.
(Fully Responsive Intelligent Digital Assistant for You)

Author:
Shae Simpson

Lead Software Architect:
OpenAI ChatGPT

Current Release:
Foundation Release 7

Current Version:
v0.7.0

Last Updated:
August 2026

---

# Project Vision

F.R.I.D.A.Y. is intended to become a professional-grade personal AI assistant inspired by J.A.R.V.I.S.

The project is designed around long-term maintainability rather than rapid feature development.

Every subsystem should have exactly one responsibility.

The architecture should remain modular enough that major components can be replaced without affecting unrelated systems.

Examples:

- Replace Speech recognition
- Replace LLM provider
- Replace Voice provider
- Replace Memory engine

without redesigning the rest of FRIDAY.

---

# Engineering Philosophy

The following rules are considered permanent.

## No technical debt.

Never build temporary code.

Never build "just for now."

Always build the architecture that should exist five years from now.

---

## One responsibility.

Every package exists for one purpose.

Examples:

Speech hears.

Intent understands.

Decision chooses.

Skills perform work.

Cognition coordinates.

Runtime manages services.

---

## Test before integration.

Every subsystem must have its own demonstration before becoming part of the runtime.

---

## Complete replacement files.

When modifying existing code, regenerate complete files instead of making manual edits whenever practical.

---

## Clean architecture over convenience.

Never sacrifice long-term maintainability to save a few minutes of coding.

---

# Current Architecture

runtime/

    pulse/
        Runtime lifecycle

    doctor/
        Diagnostics

    loader/
        Service loading

    registry/
        Service registry

    context/
        Shared runtime context

    console/
        Console output

    core/
        Shared core services

    devices/
        Hardware abstraction

    speech/
        Speech recognition

    intent/
        User intent detection

    decision/
        Decision engine

    skills/
        User capabilities

    cognition/
        Coordinates reasoning

    session/
        Interactive user session

    echo/
        Reserved for future conversation management

    platforms/
        Reserved for platform integrations

---

# Current Processing Pipeline

User

↓

Speech

↓

Intent

↓

Decision

↓

Skills

↓

Cognition

↓

Response

---

# Current Capabilities

FRIDAY currently supports:

- Interactive keyboard session
- Greeting
- Time requests
- Date requests
- Unknown request handling

---

# Current Entry Point

launcher.py

Application flow:

Launcher

↓

Runtime

↓

Session

↓

Cognition

↓

Response

---

# Coding Standards

Use Python 3.13+

Prefer dataclasses where appropriate.

Prefer type hints everywhere.

Keep functions small.

Keep classes focused.

Avoid circular imports.

Avoid global state.

Avoid hidden dependencies.

Favor dependency injection when practical.

Never duplicate logic.

---

# Git Workflow

Every milestone must:

Build

↓

Test

↓

Commit

↓

Tag

Meaningful commit messages only.

No experimental commits on main.

---

# Folder Organization

tests/

    demos/

    smoke/

    unit/

    integration/

Documentation lives in docs/.

Architecture decisions live in docs/ADR/.

---

# Long-Term Roadmap

Foundation Phase
✓ Complete

Interactive Phase
✓ Complete

Next Phase

Real microphone input

↓

Real speech recognition

↓

Text-to-speech

↓

Memory

↓

LLM integration

↓

Apple ecosystem

↓

Plugins

↓

Automation

↓

Vision

---

# Architectural Decisions

Speech owns recognition.

Intent determines meaning.

Decision selects behavior.

Skills perform work.

Cognition coordinates the reasoning pipeline.

Runtime owns lifecycle.

Session owns one user interaction.

---

# Current Known TODO

Inject dependencies instead of constructing them inside Cognition.

Expand Skill registry.

Introduce Memory subsystem.

Replace keyboard input with microphone.

Replace console output with speech.

Introduce Profile subsystem.

Add configuration management.

Implement Apple platform providers.

---

# Design Goals

FRIDAY should feel:

Professional

Reliable

Helpful

Fast

Natural

Calm

Never gimmicky.

Never overly chatty.

Never feel like a toy.

---

# Continuation Instructions

When continuing development in a new ChatGPT conversation:

1. Read this file completely.

2. Assume all architecture described here already exists.

3. Preserve existing architecture unless a significant improvement is identified.

4. Never introduce technical debt.

5. Continue from the next roadmap milestone.

6. Prefer complete replacement files.

7. Test every subsystem before runtime integration.

8. Preserve modular architecture.

9. Favor long-term maintainability over rapid implementation.

10. Build FRIDAY as if it will still be maintained ten years from now.