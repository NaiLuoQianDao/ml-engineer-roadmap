# ML Engineer — Current Progress

> **Last reviewed:** 2026-10-15 (Asia/Shanghai)
> **Status:** Month 01 · Week 01 complete; Day 07 runtime verification recorded; Week 02 / Day 08 not yet started.
> **Repository baseline checked:** GitHub `main` at `888e0ca`.
> Repository: [NaiLuoQianDao/ml-engineer-roadmap](https://github.com/NaiLuoQianDao/ml-engineer-roadmap)

## Current checkpoint

- **Completed:** Day 01–Day 07 (first week of Python foundations).
- **Next:** Day 08 — start Week 02 with a short `assert` introduction and list-slicing practice.
- **Assessment:** theory **18/20**; coding **40/40 provisional**, integrated project **27/30 provisional**, reflection **5/10 provisional**. About **90/100 initial estimate**, **not** a verified final score.
- **Known theory weakness:** Python list slicing uses an exclusive stop index (Q6).
- **Verified project risks:** the report accepts negative scores and scores above 100; a negative score can produce an incorrect highest score because `highest` starts at `-1`. A nonnumeric score raises `ValueError`.
- **Git workflow:** branches and pull requests are the next gradual Git topic. The assistant's documentation/cache proposal is on a separate branch for review.

## Daily completion record

| Day | Core topic | Evidence | Status |
| --- | --- | --- | --- |
| 01 | Development environment, Git, initial Python | `notes/month01/day01.md`, experiment/day01 | Completed |
| 02 | Variables, functions and return | `notes/month01/day02.md`, experiment/day02 | Completed |
| 03 | Conditionals and Boolean logic | `notes/month01/day03.md`, experiment/day03 | Completed |
| 04 | Loops, range, break/continue | `notes/month01/day04.md`, experiment/day04 | Completed |
| 05 | Lists, tuples, indexing and slicing | `notes/month01/day05.md`, experiment/day05 | Completed; slicing revisit |
| 06 | Dictionaries and sets | `notes/month01/day06.md`, experiment/day06 | Completed |
| 07 | Week 01 theory, four challenges, student performance report | `notes/month01/week01_assessment.md`, experiment/day07 | Submitted; runtime checks below |

All experiment paths in the table are under `src/ml_engineer_roadmap/experiment/month01/`.

## Day 07 runtime verification — 2026-10-15

The five GitHub `main` scripts were copied without edits to a temporary verification folder and run with Python 3.12. The submitted challenge/report files were not changed.

### Four challenges

- `challenge01.py` — **pass for the included examples** (exit 0). Stdout:
  `{'count': 5, 'even': 2, 'odd': 3, 'sum': 15}`,
  `{'count': 0, 'even': 0, 'odd': 0, 'sum': 0}`,
  `{'count': 3, 'even': 3, 'odd': 0, 'sum': 6}`,
  `{'count': 4, 'even': 2, 'odd': 2, 'sum': -4}`.
  Extra checks: `[0]` and `[-1]` gave correct totals/parity. Mixed integer/text input raised `TypeError`.
- `challenge02.py` — **pass for the included examples** (exit 0); stdout: `3`, `0`, `2`. Empty list returned 0. An unhashable list item raised `TypeError`; case-sensitive counting is demonstrated by `["Python", "python"]` returning 2.
- `challenge03.py` — **pass for the included examples** (exit 0); stdout: `{'average': 71.0, 'highest': 100, 'lowest': 40, 'passed': 3}` and `None`. Extra boundary check `[0, 100]` returned average 50.0, highest 100, lowest 0, passed 1; negative scores were also calculated correctly. Text input raised `TypeError`.
- `challenge04.py` — **pass for the included examples** (exit 0); stdout: `90` and `Student not found`. Searching an empty dictionary also returned `Student not found`.

“Pass” above means the committed examples and named checks produced the expected result; it is not a claim that every possible input is supported.

### Student performance report

| Scenario | Result |
| --- | --- |
| Empty database: view, statistics, passing list, exit | **Pass** — clear empty-state messages; exit code 0 |
| Scores 0 and 100 | **Pass** — average 50.0, highest 100, lowest 0, one passing student |
| Duplicate name | **Pass** — informs the user and updates the old score |
| Negative score `-5` | **Fail** — accepted; average and lowest are -5, but highest is incorrectly shown as -1 |
| Score `101` | **Fail** — accepted even though it is outside the expected 0–100 range |
| Nonnumeric score `abc` | **Fail** — unhandled `ValueError`, exit code 1 |
| Empty stdin at the menu | **Fail** — unhandled `EOFError`, exit code 1 |

**Not run:** blank/whitespace-only student names, invalid menu text, and exhaustive combinations. No test framework has been added yet. These checks establish the current behavior; they do not authorize changes to the original assessment answers.

## Immediate follow-up

- [x] Run the four challenge scripts and record their actual stdout.
- [x] Exercise empty, boundary, negative and invalid-score behavior in the student report.
- [ ] Revisit list slicing: `a[start:stop]` includes start and excludes stop.
- [ ] Teach score validation and exception handling before asking the student to repair the report.
- [ ] Review the student's own fixes and rerun the same failing cases before updating the assessment status.
- [ ] Improve self-reflection with concrete errors, evidence and unresolved questions.

## Introductory testing sequence

Progress gradually, alongside Day 08–Week 02 material. The purpose is to learn how to check one's own reasoning, not to reveal or replace assessment answers.

1. **Day 08 — expected values and `assert`:** predict a function result, write a simple assertion for a known input, run it, and read the failure message. Practice list slicing with ordinary and empty lists.
2. **Day 09 — boundary tests:** for list/statistics functions try empty, one-item, repeated, negative and zero values; for scores compare 59/60 and 0/100. Explain why each case matters.
3. **Day 10 — input validation:** distinguish a valid integer, nonnumeric text and an out-of-range score. Learn validation and `try/except`; keep tests as small manually run checks.
4. **After these basics — pytest:** install/use pytest only when simple assertions and expected-vs-actual results are understood. Start with one small test function and a few cases; later learn parameterized tests and fixtures.

**Acceptance evidence:** independently write at least three meaningful assertions (including an edge case), predict the result before running, and explain one failure. Only then move on to the first pytest test. Adjust the pacing if the work shows a gap.

## Update protocol

After each day, update **current day**, **completed vs unverified**, **concrete new gaps**, and **next action**. Cite paths, commits or test results. If code has not been run, say **static review only**. Never silently replace a submitted score or claim that a pending task was completed.

## Links

- [Roadmap](ROADMAP.md) · [Skills matrix](SKILLS_MATRIX.md) · [Teaching rules](LEARNING_RULES.md)
