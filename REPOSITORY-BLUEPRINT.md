
# Repository Blueprint

## 1. Repository Identity

- Name: Codex Game Studio
- Repository: `codex-game-studio`
- Version target: `0.1.0`
- AI environment: OpenAI Codex
- First engine: Godot
- License: MIT

## 2. Architecture

The repository is organized into five main layers.

### A. Codex Instructions

Location: Root `AGENTS.md`

Defines the persistent rules and working principles for Codex.

### B. Specialist Agents

Location: `.codex/agents/`

Provides focused responsibilities for:

- Studio Director
- Game Designer
- Game Architect
- QA Engineer

### C. Reusable Skills

Location: `.agents/skills/`

Provides repeatable workflows:

- `game-project-audit`
- `game-design-studio`
- `prototype-planner`

Each skill contains a `SKILL.md` file.

### D. Studio Knowledge

Locations:

- `studio/`
- `design/`

Contains studio organization, responsibilities, quality standards, and reusable design templates.

### E. Engine Profiles

Location: `engines/`

Contains engine-specific development guidance.

The first profile is Godot.

## 3. Planned Repository Structure

```text
codex-game-studio/
│
├── README.md
├── AGENTS.md
├── PROJECT-CHARTER.md
├── REPOSITORY-BLUEPRINT.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
│
├── .agents/
│   └── skills/
│       ├── game-project-audit/
│       │   └── SKILL.md
│       ├── game-design-studio/
│       │   └── SKILL.md
│       └── prototype-planner/
│           └── SKILL.md
│
├── .codex/
│   └── agents/
│       ├── studio-director.toml
│       ├── game-designer.toml
│       ├── game-architect.toml
│       └── qa-engineer.toml
│
├── studio/
│   ├── organization.md
│   ├── responsibilities.md
│   └── quality-gates.md
│
├── engines/
│   └── godot/
│       └── README.md
│
├── design/
│   └── templates/
│       ├── game-design-document.md
│       └── prototype-plan.md
│
├── scripts/
│
├── tests/
│   └── studio-tests/
│
└── examples/
```

## 4. Design Rules

- Keep the core framework independent of any single game engine.
- Put engine-specific guidance inside its own profile.
- Keep agent responsibilities focused.
- Make skills reusable across different game projects.
- Keep templates engine-independent unless a specific engine requires otherwise.
- Avoid duplicating instructions across files.
- Preserve human authority over project decisions.

## 5. Validation Strategy

The repository should eventually validate:

1. Required root files.
2. Expected directory structure.
3. Skill folder and metadata conventions.
4. Agent TOML syntax and supported configuration fields.
5. Required documentation.
6. Broken internal references.

Validation must produce clear pass/fail results.

## 6. Future Extensions

Potential future additions:

- Gameplay engineering agent.
- Level design agent.
- Technical art agent.
- Audio design agent.
- Unity profile.
- Unreal Engine profile.
- Godot demonstration project.
- Additional game development skills.
- Automated quality and release checks.

These extensions must be based on practical requirements and tested workflows.

## 7. Release Principle

A release should contain features that have been checked and documented.

The repository must distinguish between:

- Implemented
- Tested
- Planned
- Experimental

A feature must not be described as production-ready merely because its documentation exists.
