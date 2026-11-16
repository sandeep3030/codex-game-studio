---
name: game-project-audit
description: Audit an existing game development repository to understand its engine, structure, architecture, implementation status, risks, and recommended next steps.
---

# Game Project Audit

## Workflow

1. Inspect the repository before making recommendations.
2. Identify the game engine, version, languages, frameworks, and important dependencies.
3. Map the project structure, key scenes, scripts, assets, and configuration files.
4. Identify implemented systems and distinguish them from incomplete or placeholder work.
5. Review architecture, maintainability, performance risks, and technical debt.
6. Run available validation or tests when appropriate.
7. Separate verified findings from assumptions.

## Output

Produce a report containing:

- Project overview
- Technology and engine details
- Architecture and folder structure
- Implemented features
- Missing or incomplete features
- Technical risks
- Recommended priorities
- Suggested next development milestone

## Boundaries

- Do not modify files during an audit unless explicitly requested.
- Do not claim tests passed unless executed.
- Do not infer functionality from filenames alone.
