
#!/usr/bin/env python3
"""Validate the Codex Game Studio repository structure and metadata."""

from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "PROJECT-CHARTER.md",
    "REPOSITORY-BLUEPRINT.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    ".agents/skills/game-project-audit/SKILL.md",
    ".agents/skills/game-design-studio/SKILL.md",
    ".agents/skills/prototype-planner/SKILL.md",
    ".codex/agents/studio-director.toml",
    ".codex/agents/game-designer.toml",
    ".codex/agents/game-architect.toml",
    ".codex/agents/qa-engineer.toml",
    "studio/organization.md",
    "studio/responsibilities.md",
    "studio/quality-gates.md",
    "engines/godot/README.md",
    "design/templates/game-design-document.md",
    "design/templates/prototype-plan.md",
]

def validate():
    errors = []

    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    for skill_file in (ROOT / ".agents/skills").glob("*/SKILL.md"):
        content = skill_file.read_text(encoding="utf-8")
      
        match = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", content, re.DOTALL)

        if not match:
            errors.append(f"Invalid skill frontmatter: {skill_file.relative_to(ROOT)}")
            continue

        metadata = match.group(1)

        for field in ("name", "description"):
            if not re.search(rf"^{field}:\s*\S+", metadata, re.MULTILINE):
                errors.append(
                    f"Missing or empty '{field}' in {skill_file.relative_to(ROOT)}"
                )

    for agent_file in (ROOT / ".codex/agents").glob("*.toml"):
        try:
            with agent_file.open("rb") as file:
                data = tomllib.load(file)

            for field in ("name", "description", "developer_instructions"):
                if not isinstance(data.get(field), str) or not data[field].strip():
                    errors.append(
                        f"Missing or invalid '{field}' in {agent_file.relative_to(ROOT)}"
                    )
        except (tomllib.TOMLDecodeError, OSError) as error:
            errors.append(f"Invalid TOML in {agent_file.relative_to(ROOT)}: {error}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f" - {error}")
        return 1

    print("VALIDATION PASSED")
    print(f"Checked {len(REQUIRED_PATHS)} required files.")
    print("Skill metadata and agent TOML syntax are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
