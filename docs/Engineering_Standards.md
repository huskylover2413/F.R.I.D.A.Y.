# FRIDAY Engineering Standards

Version: Alpha 0.2 – Forge

---

# Mission

Every line of code should make FRIDAY easier to understand tomorrow than it was yesterday.

---

# Guiding Principles

1. One responsibility per module.
2. One responsibility per class.
3. One responsibility per function.
4. Expandable without rewrites.
5. Context before commands.
6. Sessions over conversations.
7. Readability over cleverness.

---

# Architecture Rules

- Every system has a clearly defined owner.
- No duplicated logic.
- No "misc" folders.
- No hard-coded project paths.
- No circular dependencies.

---

# Documentation

Every Python file must include:

- Header
- Purpose
- Author
- Version

Every public class and function must include a docstring.

Comments explain **why**, not **what**.

---

# Naming

Classes:

PascalCase

Functions:

snake_case

Variables:

snake_case

Constants:

UPPER_CASE

Folders:

lowercase

---

# Error Handling

FRIDAY never panics.

Errors should always explain:

- What happened.
- What still works.
- What FRIDAY is attempting.
- When user action is required.

---

# Console Style

Every subsystem communicates through the Console.

No direct print() statements outside the Console package.

---

# Reviews

Every milestone ends with:

- Architecture review
- Code review
- Testing
- Git checkpoint

---

# Definition of Done

A feature is complete only when:

✓ Code is readable.

✓ Code is documented.

✓ Code is tested.

✓ Architecture is respected.

✓ Project builds cleanly.

✓ Ready for Git checkpoint.