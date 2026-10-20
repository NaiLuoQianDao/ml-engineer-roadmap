# ML Engineer — Current Progress

> **Last reviewed:** 2026-10-20 (Asia/Shanghai)
> **Status:** Month 01 · Week 01 completed (assessment still provisional); Week 02 Day 08–Day 11 completed and reviewed; Day 12 planned, not started.
> **Repository baseline checked:** GitHub `main` at `48f6782b8affbf9923656133fe111a58d153f9dc` (2026-10-18, bytecode-cache cleanup).
> Repository: [NaiLuoQianDao/ml-engineer-roadmap](https://github.com/NaiLuoQianDao/ml-engineer-roadmap)

## Current checkpoint

- **Completed learning days:** Day 01–Day 11. Week 02 is **in progress**, not yet complete.
- **Next proposed day:** Day 12 — introductory pytest parameterization, with a short reading from the [pytest documentation](https://docs.pytest.org/en/stable/how-to/parametrize.html). Await independent work and verification.
- **Week 01 assessment:** theory **18/20**; coding **40/40 provisional**, integrated project **27/30 provisional**, reflection **5/10 provisional**; approximately **90/100 initial estimate**, **not a final regraded score**.
- **Original Day 07 code is preserved:** the original student report still has the documented invalid-score/initialization failures. Day 10's `student_performance_report_v2.py` is a **separate improvement**, not a retroactive change to the Day 07 assessment.
- **Current concrete gains:** slicing practice and `assert` (Day 08); boundary-case design and fixing a percentage-versus-proportion error (Day 09); `try/except`, range checking and retry loops (Day 10); first organized pytest suite and a reproduced negative-number bug (Day 11).
- **Remaining gaps:** more precise reflective/test evidence; narrow `except ValueError` rather than bare `except:` in Day 10's `parse_score`; broader invalid-input and regression checks; module/import and pytest organization; comfort with less-common Git/uv flags.
- **Git workflow:** daily commits and pushes demonstrated; mistakenly tracked `.pyc` files removed by `48f6782b`. `.gitignore` already excludes `__pycache__/` and `*.pyc`. Branch/PR workflows and advanced Git commands remain gradual learning goals.
- **Evidence limitation:** the separate “ML Engineer 每周复盘” conversation's summary could not be retrieved during this review. A weekly automation ran on 2026-10-18, but its message text was not accessible. No unverified claims from that recap are included.

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
| 08 | List slicing, expected values, `assert` and score window viewer | `notes/month01/day08.md`, experiment/day08; `194aacbe5` | Completed; source reviewed; reflection has incomplete items |
| 09 | Boundary value analysis and pass-rate analyzer | `notes/month01/day09.md`, experiment/day09; `69d5b108`, fix `35033de` | Completed; percentage behavior corrected |
| 10 | Input validation, `try/except`, report V2 | `notes/month01/day10.md`, experiment/day10; final fix `1a51d1a` | Completed; specified behavior reviewed; some robustness gaps |
| 11 | pytest basics, test discovery and bug hunt | `notes/month01/day11.md`, experiment/day11 and `tests/month01/day11/`; `dbef7a2` | Completed; 15-test suite reviewed, previously reported passing |

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

## Week 02 evidence — Day 08 to Day 11

### Day 08 — slicing and `assert` (2026-10-16)

- **Commit:** `194aacbe5` (following `d9fe2fd`); `exercise01.py`, `exercise02.py`, `score_window_viewer.py` and `day08.md`.
- Slicing functions `get_first_n` / `get_every_second` and the score-window statistics project meet the specified basic cases, including empty selections. The first exercise's example calls do not themselves assert returned values.
- The course review accepted the core programming work. **Evidence gap:** the original Q4 prediction is blank and the learning log contains terse or unfilled explanations. The student opted to move forward rather than retroactively rewrite that reflection.

### Day 09 — boundary value analysis (2026-10-17/18)

- **Commits:** `69d5b108` (initial work), `35033de` (corrected percentage and tests).
- `is_passing` tests the 59/60 boundary; `count_above_threshold` uses strict `>` and handles empty, repeated and negative inputs. `pass_rate_analyzer.py` now calculates **percentage points (0–100)** rather than a fraction (0–1), including an `[0, 100]` check.
- **Evidence gap:** `day09.md` retained its earlier “19 tests” record even after an eighth project assertion was added (20 assertions across the three exercise scripts). Log wording about the 59/60 distinction is partly stale. Do not rewrite the student's original record silently.

### Day 10 — input validation and exception handling (2026-10-18)

- **Commit:** `1a51d1a` after earlier correction commits. `exercise01_try_except.py` now invokes its input function; `parse_score` returns a valid integer or `None`; `student_performance_report_v2.py` includes add/update, list, search, passing list, statistics and exit.
- V2 uses a retry loop with `except ValueError` and checks the score range 0–100. Previous review checked valid 0/100, invalid text/out-of-range then retry, empty records, duplicate names and other menu cases. **Only specified scenarios were verified**, not exhaustive interaction paths.
- **Remaining improvement:** `exercise02_score_validation.py` still has a bare `except:`; V2's menu input has no `EOFError` handling (out of Day 10 minimum scope). The student's Day 10 log describes the pre-fix version and does not fully document final retest evidence.

### Day 11 — first pytest suite (2026-10-18)

- **Commits:** `dbef7a2` (Day 11 code, tests and note); `48f6782b` (untrack generated bytecode files).
- The repository contains **15 distinct pytest test functions**: `test_first.py` (2), `test_score_utils.py` (10), `test_bug_hunt.py` (3), under `tests/month01/day11/`. Student learning log records **15 passed** using `uv run --with pytest ... python -m pytest tests/month01/day11/ -v`; the prior mentor code review also accepted the specified cases. This is **not CI coverage** or a claim of exhaustive tests.
- `get_highest` previously failed for an all-negative non-empty list; the student's new test uses `[-10, -5, -15]` and the current function initializes from `min(scores)`. The assignment explicitly assumes a **non-empty list**; `min([])` still raises `ValueError` outside that contract.
- Initial PyPI download and file-path issues were resolved using a temporary package index and the correct `tests/month01/day11/` path. Long `uv`/Git maintenance commands are **reference-use skills**, not memorization requirements.

## Immediate follow-up

- [x] Revisit exclusive-stop slicing, ordinary and empty selections (Day 08).
- [x] Introduce expected outputs, `assert` and boundary case selection (Days 08–09).
- [x] Teach numeric conversion and score range validation (Day 10, separate V2).
- [x] Introduce pytest test discovery and multiple independently named tests (Day 11).
- [x] Remove tracked `.pyc` caches from Git without deleting original source (commit `48f6782b`).
- [ ] Keep the original Day 07 assessment provisional; do not replace original code with V2 or silently change the assessment score.
- [ ] Improve exception specificity, test isolation/import behavior and reproducible regression evidence gradually.
- [ ] Day 12: write first `@pytest.mark.parametrize` tests and explain test case inputs/expected outputs before using advanced pytest features.
- [ ] At the next weekly review, revisit logging precision, independent debugging, and how to read unfamiliar command flags safely.
- [ ] Integrate the separate weekly recap only after its actual contents become available and can be checked against repository evidence.

## Tools and learning expectations

- **Independent routine use (now):** `git status`, `git add`, `git commit`, `git push`; running existing Python scripts.
- **Understand and adapt with reference (now):** `git diff --cached`, `uv run --with pytest`, `python -m pytest <path> -v`, interpreting PASSED/FAILED and locating files.
- **Understand purpose/risk; look up when needed (not a memory test):** `git rm -r --cached`, `git check-ignore -v --no-index`, `uv --index-url`; future branch and pull-request maintenance.
- For each new day, recommend **only the essential official resource**, supplement with a video only when it materially improves understanding. Continue to prioritize independent code and actual verification.

## Update protocol

After each day, update **current day**, **completed vs unverified**, **concrete new gaps**, and **next action**. Cite paths, commits or test results. If code has not been run, say **static review only**. Never silently replace a submitted score or claim that a pending task was completed.

## Links

- [Roadmap](ROADMAP.md) · [Skills matrix](SKILLS_MATRIX.md) · [Teaching rules](LEARNING_RULES.md)
