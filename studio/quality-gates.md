
# Studio Quality Gates

A development task should pass the relevant gates before being considered complete.

## Gate 1 — Requirements

- Objective is clear.
- Scope is understood.
- Acceptance criteria are defined.
- Important assumptions are recorded.

## Gate 2 — Design

- Proposed solution addresses the objective.
- Design is consistent with the approved game concept.
- Dependencies and risks are identified.

## Gate 3 — Implementation

- Changes remain within approved scope.
- Code and resources follow project conventions.
- No unnecessary dependencies are introduced.

## Gate 4 — Validation

- Relevant tests or checks are executed.
- Broken references and obvious regressions are investigated.
- Results are accurately reported.

## Gate 5 — Review

- Deliverables meet acceptance criteria.
- Documentation is updated where necessary.
- Incomplete work is clearly identified.

## Completion Rule

A gate may be marked:

- PASS — verified successfully.
- FAIL — a known requirement is not met.
- NOT RUN — validation was not performed.

Never mark an untested feature as verified.
