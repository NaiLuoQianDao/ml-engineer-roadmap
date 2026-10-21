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
| Week 03 | Reinforce references/copying, code contracts, error handling and independent regression-test design; precise daily tasks to be assigned next | **Planned; not started** |
| Week 04 | Foundation consolidation and a verified small project | Provisional |

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
