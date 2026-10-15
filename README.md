# 24-Month ML Engineer Roadmap

A personal, evidence-based learning roadmap for building the skills needed to apply for Machine Learning Engineer roles, with the UK job market as a long-term target.

这是一个持续更新的学习仓库，记录路线、练习代码、学习日志和能力验证。计划中的内容不代表已经学会；每项进度应以实际代码、日志和测试结果为准。

## Current checkpoint

- Month 01 · Week 01 (Day 1–7): completed; Day 7 runtime checks have been recorded.
- Next: Day 8, beginning Week 02.
- Current priorities: list slicing, input validation, debugging, edge cases and introductory testing.

See [current progress](docs/PROGRESS.md), [the roadmap](docs/ROADMAP.md), [learning rules](docs/LEARNING_RULES.md) and [the skills matrix](docs/SKILLS_MATRIX.md) for details. The progress document is the source of truth for what has actually been completed and verified.

## Repository guide

- `docs/` — roadmap, current progress, teaching agreement and skills matrix.
- `notes/` — daily learning logs and assessment records.
- `src/ml_engineer_roadmap/experiment/month01/` — small Python exercises grouped by learning day.
- `pyproject.toml` and `uv.lock` — Python project and dependency configuration.
- `.gitignore` — excludes the local virtual environment and Python cache files.

## Run a practice script

The project targets Python 3.12 or newer and uses [uv](https://docs.astral.sh/uv/) to manage the environment. After installing Python and uv, open a terminal at the repository root:

```powershell
uv sync
uv run python src/ml_engineer_roadmap/experiment/month01/day07/challenge01.py
uv run python src/ml_engineer_roadmap/experiment/month01/day07/student_performance_report.py
```

The first command prepares the project environment. The challenge script prints its example results; the student report opens an interactive menu. Use `6` to exit the menu. These are learning exercises, not a deployed application.

## Learning and verification

Work through the roadmap in small steps. For each exercise, explain the expected result before running it, then compare that expectation with the actual output. Keep failures visible in the progress record; do not treat a commit as proof that code has been tested.

Basic `assert` checks and boundary testing are being introduced in Month 01. The plan is to learn these first, then add pytest once simple tests and their expected results are understood. Pytest is not yet configured in this repository.
