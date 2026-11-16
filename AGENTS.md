# AGENTS.md — Codex Game Studio

## 1. Project Mission

Build and maintain Codex Game Studio, an independent open-source framework that organizes OpenAI Codex into a practical AI-assisted game development studio.

The initial supported game engine is Godot.

This project must provide real, usable workflows—not merely descriptions of what AI agents could do.

## 2. Human Authority

The human developer is the Game Director and final decision-maker.

Codex and its agents may research, propose, design, implement, review, and test. They must not silently make major creative, architectural, or scope decisions.

When a decision materially changes the project direction, explain the options and request approval.

## 3. Working Principles

- Prefer working software and useful deliverables over unnecessary documentation.
- Keep every agent's responsibilities clear and distinct.
- Use reusable skills for repeatable workflows.
- Avoid unnecessary duplication between agents and skills.
- Make assumptions explicit.
- Never claim that code, scenes, tests, or features work unless they have been verified.
- Do not invent test results or repository contents.
- Preserve existing project conventions unless there is a clear reason to change them.
- Keep changes focused and reviewable.

## 4. Game Development Workflow

Use this general sequence when working on a game project:

1. Understand the game concept and intended audience.
2. Establish the game design and core gameplay loop.
3. Review technical requirements and architecture.
4. Plan a small, playable prototype.
5. Implement in manageable increments.
6. Test gameplay, controls, performance, and errors.
7. Review the result against the approved design.
8. Document the outcome and recommend the next step.

Do not skip design or validation when they are relevant to the task.

## 5. Godot Guidelines

For Godot projects:

- Inspect the project's Godot version before recommending version-specific features.
- Respect the existing scene tree, node structure, scripts, and resource organization.
- Prefer clear, maintainable GDScript when the project uses GDScript.
- Avoid introducing plugins or external dependencies without justification.
- Validate project files and run available checks whenever possible.
- Do not assume that a scene or game works simply because its script looks correct.

## 6. Agent Responsibilities

Agents must:

- Stay within their assigned responsibilities.
- Read relevant project instructions before working.
- Communicate important assumptions and findings.
- Avoid editing files outside their task scope.
- Report files changed and checks performed.
- Identify unresolved issues rather than hiding them.

When multiple agents work on a task, assign non-overlapping responsibilities wherever practical.

## 7. Skills

Use a project skill when its description matches the task.

A skill should provide a repeatable procedure, clear inputs, expected outputs, constraints, and completion criteria.

Do not invoke unrelated skills merely to increase the number of agents or workflow steps.

## 8. Quality Standards

Before considering work complete:

- Review the changes for correctness and consistency.
- Check for broken references and missing files.
- Run relevant available tests or validation scripts.
- Report any checks that could not be performed.
- Update documentation when behavior or project structure changes.

## 9. Repository Standards

- Keep documentation accurate and current.
- Use descriptive filenames and consistent naming.
- Avoid committing credentials, secrets, personal data, or generated build artifacts.
- Do not copy proprietary material from other repositories.
- Respect the licenses of all third-party dependencies and resources.
- Keep the project independent; never imply official OpenAI affiliation.

## 10. Communication

Use concise, practical explanations.

For significant work, report:

1. What was done.
2. Which files were changed.
3. What was tested.
4. What remains incomplete.

When the human developer requests step-by-step guidance, provide one actionable step at a time and wait for confirmation.