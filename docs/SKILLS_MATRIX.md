# ML Engineer Skills Matrix

> Baseline: Week 01 assessment, reviewed 2026-10-13.
> **Legend:** Learned = taught; Practiced = shown in code; Verified = explicit run/tests reviewed. "Pending verification" is not a failure.

| Skill / concept | Learned | Practice evidence | Verification / confidence | Next action |
| --- | --- | --- | --- | --- |
| Python environment, virtual environment, VS Code | Yes | Day 01 setup, daily Python scripts | Working environment reported; details not exhaustively rechecked | Review `.venv` and `pyproject.toml` roles |
| Git status / add / commit / push | Yes | Daily commits and terminal outputs | Upload and synchronization previously confirmed | Continue commit hygiene, learn branches/PRs gradually |
| Variables, types, strings, input | Yes | Day 02 code | Basic application demonstrated | Practice invalid input |
| Functions, parameters, return vs print | Yes | Day 02–07 programs | Independent usage appears in submitted code; some tests pending | Reuse functions and explain return values |
| Boolean logic / conditions | Yes | Day 03 + projects | Theory and code evidence | Edge cases / branch ordering |
| Loops / range / break / continue | Yes | Day 04 + projects | Theory and code evidence | Trace iterations without running |
| Lists, tuples, indexing | Yes | Day 05 + assessment | Theory mostly correct | Revisit slicing end-exclusive rule (Q6 wrong) |
| Slicing | Yes | Day 05, Week 01 theory Q6 | **Gap identified: theory error** | 5 short targeted exercises |
| Dictionaries / sets | Yes | Day 06 + Day 07 challenges | Code statically reviewed, runtime tests pending | Nested structures and safe access |
| Simple program design / menus | Yes | Day 06 Student Record System, Day 07 report | Core features statically reviewed | Separate input/logic, improve structure |
| Highest/lowest/average statistics | Yes | Day 07 Challenge 3 and report | Boundary defect risk in report | Initialize from real data or validate range |
| Input validation / exceptions | Not systematically yet | `int(input(...))` in project | **Known weakness** for non-numeric and invalid scores | Learn try/except, validation and error messages |
| Automated tests / pytest | Not yet | Manual expected-output examples | **Not verified** | Introduce once prerequisites are ready |
| NumPy, Pandas, ML, PyTorch, MLOps | Planned only | None yet | Not started | Follow roadmap; don't claim learned |

## Week 01 assessment evidence

- [Assessment and submitted answers](../notes/month01/week01_assessment.md)
- [Four Day 07 programming challenges](../src/ml_engineer_roadmap/experiment/month01/day07/)
- Theory: **18/20**.
- Coding: **40/40 provisional**; project: **27/30 provisional**; reflection: **5/10 provisional**.
- Approximate first review: **90/100 provisional**, pending runtime/edge-case tests.

## Verification rubric

- **Introduced** — encountered in lecture/explanation.
- **Understood** — can explain purpose and behavior in own words.
- **Independent** — can solve a new variation without copying.
- **Verified** — source and test outputs inspected, including relevant edge cases.

For future updates, record the date, repository path/test, the level achieved, and unresolved errors. No false precision in percentages.
