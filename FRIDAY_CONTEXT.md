# F.R.I.D.A.Y.
## Fully Responsive Intelligent Digital Assistant for You

---

# Purpose

FRIDAY is a long-term AI assistant project designed to become a production-quality personal assistant inspired by the capabilities and professionalism of the assistant seen in the Iron Man films.

The goal is NOT to build a chatbot.

The goal is to build a modular, extensible operating environment capable of interacting with the user through voice, vision, reasoning, memory, and external services.

Every architectural decision should favor long-term maintainability over short-term convenience.

---

# Project Philosophy

This project follows several non-negotiable principles.

## 1. Architecture First

Never build features before the architecture exists.

Features should naturally fit into the existing architecture.

Never write code that "just works."

Always build code that belongs.

---

## 2. One Responsibility Per Class

Classes should do one thing well.

Avoid giant "manager" classes.

Prefer many small focused classes.

---

## 3. Platform Isolation

Platform-specific code never leaks into the core runtime.

Correct:

runtime/platforms/apple/

Incorrect:

runtime/core/apple.py

---

## 4. Runtime Independence

The runtime should never know:

- Apple
- Windows
- Linux

The runtime only communicates with abstract interfaces.

---

## 5. Replaceability

Every subsystem should be replaceable.

Examples:

Speech Provider

AppleSpeechProvider

WhisperSpeechProvider

AzureSpeechProvider

should all satisfy the same interface.

---

## 6. Incremental Development

Every release should leave the project in a working state.

Never leave the repository broken.

Always:

Build

↓

Test

↓

Commit

↓

Tag

↓

Continue

---

# Current Architecture

launcher.py

↓

Runtime

↓

Session

↓

Input

↓

Speech

↓

Intent

↓

Decision

↓

Cognition

↓

Voice

---

# Major Runtime Packages

runtime/

core/

context/

console/

loader/

registry/

session/

speech/

input/

voice/

profile/

skills/

platforms/

doctor/

devices/

---

# Apple Platform

Apple-specific functionality belongs ONLY here.

runtime/platforms/apple/

Future Apple integrations include:

Speech

Camera

Vision

Calendar

Contacts

Music

Reminders

Notifications

HomeKit

Shortcuts

---

# Current Status

Completed

Runtime

Service Registry

Session

Voice Output

Profile Management

Input Abstraction

Speech Architecture

Cognition Pipeline

Skill Loading

Current Work

Apple Speech Integration

Upcoming

Live Microphone

Wake Word

Conversation Mode

Memory

Vision

Planning

External Tool Execution

---

# Coding Standards

Always use:

Type hints

Docstrings

Small classes

Constructor injection

Meaningful names

No hidden magic

No global state unless absolutely required by the platform API.

Generate complete replacement files when modifying existing files.

---

# Git Workflow

Create feature branch

↓

Implement

↓

Run demo

↓

Run tests

↓

Commit

↓

Tag release

↓

Merge

---

# Release Philosophy

Foundation Releases build architecture.

Later Releases build intelligence.

Never sacrifice architecture to add features faster.

---

# Testing Philosophy

Every subsystem should have:

Demo

Smoke test

Integration test

Failures should be reproducible.

---

# Design Goals

FRIDAY should eventually provide:

Voice conversation

Natural interruption

Long-term memory

Vision

Calendar

Email

Tasks

Home automation

Reasoning

Planning

Camera understanding

Document understanding

Tool use

Multi-step execution

Cross-platform support

Plugin architecture

---

# Things Future ChatGPT Should NOT Do

Do NOT redesign the architecture.

Do NOT flatten the folder structure.

Do NOT merge unrelated responsibilities.

Do NOT replace abstractions with shortcuts.

Do NOT remove demos.

Do NOT remove tests.

Do NOT build giant files.

Do NOT introduce platform-specific code into the runtime.

---

# Preferred Development Workflow

1. Discuss architecture.

2. Create folders.

3. Create files.

4. Generate complete code.

5. Paste.

6. Save.

7. Test immediately.

8. Fix immediately.

9. Commit.

10. Tag.

Only then begin the next feature.

---

# Current Objective

Complete the Apple Speech provider.

Replace keyboard input with microphone input.

Add wake-word detection.

Transition FRIDAY from keyboard-first to voice-first interaction.

---

This document is the canonical description of the FRIDAY project architecture and development philosophy.

Future conversations should preserve these principles unless there is a compelling architectural reason to change them.