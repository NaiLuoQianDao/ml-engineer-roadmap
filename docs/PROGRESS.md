# ML Engineer — Current Progress

> **Last reviewed:** 2026-10-13 (Asia/Shanghai)
> **Status:** Month 01 · Week 01 complete; Week 02 / Day 08 not yet started.
> Repository: [NaiLuoQianDao/ml-engineer-roadmap](https://github.com/NaiLuoQianDao/ml-engineer-roadmap)

## Current checkpoint

- **Completed:** Day 01–Day 07 (first week of Python foundations).
- **Next:** Day 08 — choose and deliver the Week 02 task after checking the Week 01 assessment and any outstanding errors.
- **Latest confirmed main commit when these documents were prepared:** `1a128c7` (improved Week 01 assessment documentation).
- **Assessment:** theory **18/20**; coding **40/40 provisional**, integrated project **27/30 provisional**, reflection **5/10 provisional**. About **90/100 initial estimate**, **not** a verified final score.
- **Known theory weakness:** Python list slicing uses an exclusive stop index (Q6).
- **Known project risks:** no robust nonnumeric/0–100 score validation; `highest = -1`, `lowest = 101` depend on assumptions not enforced by input validation.
- **Git workflow:** add, status, commit, push and rename practiced; latest user-reported local status was clean/synchronized. Do not infer future status from this snapshot.

## Daily completion record

| Day | Core topic | Evidence | Status |
| --- | --- | --- | --- |
| 01 | Development environment, Git, initial Python | `notes/month01/day01.md`, experiment/day01 | Completed |
| 02 | Variables, functions and return | `notes/month01/day02.md`, experiment/day02 | Completed |
| 03 | Conditionals and Boolean logic | `notes/month01/day03.md`, experiment/day03 | Completed |
| 04 | Loops, range, break/continue | `notes/month01/day04.md`, experiment/day04 | Completed |
| 05 | Lists, tuples, indexing and slicing | `notes/month01/day05.md`, experiment/day05 | Completed; slicing revisit |
| 06 | Dictionaries and sets | `notes/month01/day06.md`, experiment/day06 | Completed |
| 07 | Week 01 theory, four challenges, student performance report | `notes/month01/week01_assessment.md`, experiment/day07 | Submitted and statically reviewed; runtime verification pending |

All experiment paths in the table are under `src/ml_engineer_roadmap/experiment/month01/`.

## Immediate follow-up (before or during Week 02)

- [ ] Run explicit normal/edge-case tests for all Day 07 challenge functions.
- [ ] Check Day 07 student report with no students, duplicate names, malformed score, negative score and score > 100.
- [ ] Review and fix `highest`/`lowest` initialization or enforce validated score input.
- [ ] Revisit list slicing: `a[start:stop]` includes start, excludes stop.
- [ ] Improve self-reflection with concrete errors, evidence and unresolved questions.
- [ ] Assign Day 08 with the usual why/how/verify instructions.

## Update protocol

After each day, update **current day**, **completed vs unverified**, **concrete new gaps**, and **next action**. Cite paths, commits or test results. If code has not been run, say **static review only**. Never silently replace a submitted score or claim that a pending task was completed.

## Links

- [Roadmap](ROADMAP.md) · [Skills matrix](SKILLS_MATRIX.md) · [Teaching rules](LEARNING_RULES.md)
