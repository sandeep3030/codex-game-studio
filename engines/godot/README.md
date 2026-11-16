
# Godot Engine Profile

Godot is the first supported game engine in Codex Game Studio.

## Initial Support

The framework provides guidance for:

- Godot project inspection.
- Scene and node organization.
- GDScript development.
- Resource management.
- Gameplay architecture.
- Testing and project validation.

## Before Working on a Godot Project

1. Locate `project.godot`.
2. Identify the installed and project-compatible Godot version.
3. Inspect existing scenes, scripts, resources, and autoloads.
4. Understand existing naming and folder conventions.
5. Identify available tests and validation methods.

## Development Guidelines

- Preserve existing scene and node relationships unless changes are approved.
- Prefer readable, maintainable GDScript.
- Use signals for appropriate event-driven communication.
- Avoid unnecessary autoloads and global state.
- Keep reusable gameplay systems modular.
- Do not introduce addons without justification.
- Use placeholder assets when appropriate during prototyping.

## Validation

Use the Godot executable available in the environment.

For headless editor validation, a typical command is:

`godot --headless --editor --path . --quit`

The executable may be named `godot4` or differ by installation. Confirm availability before running commands.

This check does not replace gameplay testing.

## Compatibility

Always inspect the project's Godot version before using version-specific APIs or features.

## Future Expansion

Additional engine profiles may be introduced independently without changing the core studio model.
