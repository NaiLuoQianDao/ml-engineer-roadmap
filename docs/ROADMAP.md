# 24-Month ML Engineer Roadmap

> Status: **Working roadmap — version 0.1**. This is an adaptable planning framework, not evidence that every month has already been agreed or completed.
> Career direction: Machine Learning Engineer, with the UK job market as an important target.
> Source of truth for actual progress: [PROGRESS.md](PROGRESS.md), [SKILLS_MATRIX.md](SKILLS_MATRIX.md), daily notes and code.

## Principles

- Learn foundations thoroughly, then build and deploy increasingly realistic ML systems.
- Balance Python/software engineering, mathematics, data, ML/DL, MLOps and communication.
- Build a public portfolio responsibly: do not commit private credentials or sensitive personal data.
- Review each week and month. Adjust scope according to demonstrated ability, university commitments and job-market evidence.
- A planned topic is **not** a completed topic. A Git commit is **not** proof that runtime tests passed.

## Provisional 24-month phases

| Months | Primary direction | Representative evidence / milestone |
| --- | --- | --- |
| 01–03 | Python foundations, Git, testing, algorithms and basic engineering | Small independently implemented programs, tested Python modules, regular logs |
| 04–06 | Math for ML, NumPy, Pandas, exploratory data analysis, SQL | Reproducible analysis notebook and data project |
| 07–09 | Classical machine learning: statistics, preprocessing, supervised/unsupervised methods | End-to-end scikit-learn project with appropriate evaluation |
| 10–12 | Software engineering for ML, APIs, experiment tracking, first deployment | Model served through an API and documented deployment |
| 13–15 | Deep learning with PyTorch, neural networks and one domain focus | Trained DL model, error analysis and reproducible experiments |
| 16–18 | LLM applications, embeddings, retrieval, evaluation and reliability | Evaluated RAG or AI application with documented limitations |
| 19–21 | MLOps, CI/CD, containers, cloud fundamentals, monitoring | Deployed and tested ML service with monitoring plan |
| 22–24 | Portfolio consolidation, interviews and UK ML Engineer applications | Refined projects, CV, interview practice and application tracking |

These phase boundaries are provisional. Revisit them at monthly reviews; do not rush onward if prerequisites are insecure.

## Month 01 — Python foundations (current)

| Week | Plan | Status |
| --- | --- | --- |
| Week 01 | Environment & Git; variables & functions; conditionals; loops; lists & tuples; dictionaries & sets; assessment | **Completed; assessment partly provisional** |
| Week 02 | Slicing, boundaries, input validation, pytest, parameterization, modularization and integrated assessment (Days 08–14) | **Completed; mentor regrade 93/100 after corrections** |
| Week 03 | References/copying (Day 15), exception contracts and pytest debugging (Day 16), type hints and prediction evaluation (Day 17); file I/O and structured data next; Week 03 assessment pending | **In progress; Days 15–17 submitted/reviewed, not yet assessed as a week** |
| Week 04 | Foundation consolidation; proposed Student Data Processing Pipeline using CSV input, validation and JSON output; requirements and timing remain provisional | **Planned; not started** |

### Week 01 evidence

- [Week 01 assessment](../notes/month01/week01_assessment.md)
- [Day 01–06 notes](../notes/month01/)
- [Day 07 source code](../src/ml_engineer_roadmap/experiment/month01/day07/)

### Week 02 evidence

- [Week 02 assessment, theory answers and original test transcript](../notes/month01/week02_assessment.md)
- [Day 08–13 learning logs](../notes/month01/)
- [Day 14 study-session report and challenge source](../src/ml_engineer_roadmap/experiment/month01/day14/)
- [Day 14 pytest files](../tests/month01/day14/)
- Day 14 original submission `4a87c58`, then corrections to list identity and module reuse in `386ee6a`. Mentor regrade **93/100**; the recorded Day 14 `18 passed` transcript predates the corrections. See [PROGRESS.md](PROGRESS.md) for verification qualifications.

### Week 03 evidence and next steps

- [Day 15 notes](../notes/month01/day15.md), [source](../src/ml_engineer_roadmap/experiment/month01/day15/) and [tests](../tests/month01/day15/) — list identity/copy semantics, bonus transform and Day 14 regression (`de4207a`).
- [Day 16 notes](../notes/month01/day16.md), [source](../src/ml_engineer_roadmap/experiment/month01/day16/) and [tests](../tests/month01/day16/) — strict score checks and bulk import; logged **87 passed** Month 01 regression; pytest import-name conflict repaired (`909b503`).
- [Day 17 notes](../notes/month01/day17.md), [source](../src/ml_engineer_roadmap/experiment/month01/day17/) and [tests](../tests/month01/day17/) — labeled classification prediction summary; reported **21 Day 17** and **108 total Month 01** test cases, not independent CI verification (`b0ee476`, `0f8dc4b`).
- The October monthly report and November 1 weekly report are historical snapshots through Day 16, not a reason to mark Day 17 unfinished as of November 8. The student opted not to revise original Days 15–16 submissions.
- **Next:** Day 18 file I/O and `pathlib`; then CSV/JSON, independent end-to-end data processing, Week 03 assessment. **Month 01 is not completed** and the Week 04 project remains proposed rather than verified.

## Weekly teaching cycle

1. Check latest progress and repository state.
2. Teach one bounded topic and its prerequisites.
3. Independent exercises + small application; explain why/how/verification.
4. Review actual code, cases and failures — never rely on commit alone.
5. Record new strengths, gaps and next actions in PROGRESS / SKILLS_MATRIX.
6. Weekly assessment; monthly phase review.

## Related documents

- [Current progress](PROGRESS.md)
- [Teaching rules](LEARNING_RULES.md)
- [Skills matrix](SKILLS_MATRIX.md)
