# Day 16 — Exception Handling & Function Contracts（异常处理与函数契约）

Date: 2026-10-25

## 1. Learning Goals（学习目标）

- Understand `raise` and `except`（理解异常抛出与捕获）
- Understand Function Contracts（理解函数契约）
- Practice `pytest.raises()`（练习异常测试）
- Separate Strict Validation and Tolerant Processing（区分严格验证与容错处理）

## 2. Key Concepts（核心概念）

**ValueError（值错误）**

什么情况下应该抛出：函数传来的参数类型与要求的不一致

**TypeError（类型错误）**

与 ValueError 有什么区别：这个是执行操作时不符合类型本身要求

**raise（抛出异常）**

作用是什么：可以针对程序可能出现的错误做不同的处理

**try/except（异常捕获）**

什么时候应该捕获异常：当程序可能出现错误,并且需要对错误进行合理处理

**pytest.raises()（预期异常测试）**

作用是什么：测试程序中针对异常的处理是否能正常运行

## 3. Exercise A — Strict Score Validator

我的设计思路：正常做

如何区分输入类型错误与输入值错误：使用type()判断

我主动验证的边界情况：0,100

## 4. Exercise B — Batch Score Importer

为什么需要复用 parse_score_strict：需要对每个人成绩进行检查是否合理

如何确保某条记录错误时其他记录继续处理：使用try/except捕获异常

如何确保原始字典没有被修改：只是用原字典数据用来赋值

## 5. Testing Evidence（测试证据）

Day 16 测试命令：uv run python -m pytest tests/month01/day16/ -v

Day 16 收集测试数量：10

Day 16 通过数量：10

Day 16 失败数量：0

Month 01 完整回归测试命令：uv run python -m pytest tests/month01/ -v

完整回归测试结果：
(ml-engineer-roadmap) PS C:\Users\lk120\dev\ml-engineer-roadmap> uv run python -m pytest tests/month01/ -v
=========================================================================== test session starts ============================================================================
platform win32 -- Python 3.12.14, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\lk120\dev\ml-engineer-roadmap\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lk120\dev\ml-engineer-roadmap
configfile: pyproject.toml
collected 87 items                                                                                                                                                          

tests/month01/day11/test_bug_hunt.py::test_positive_numbers PASSED                                                                                                    [  1%]
tests/month01/day11/test_bug_hunt.py::test_mixed_numbers PASSED                                                                                                       [  2%]
tests/month01/day11/test_bug_hunt.py::test_special_case PASSED                                                                                                        [  3%]
tests/month01/day11/test_first.py::test_addition PASSED                                                                                                               [  4%]
tests/month01/day11/test_first.py::test_subtraction PASSED                                                                                                            [  5%]
tests/month01/day11/test_score_utils.py::test_score_below_minimum PASSED                                                                                              [  6%]
tests/month01/day11/test_score_utils.py::test_score_lower_boundary PASSED                                                                                             [  8%]
tests/month01/day11/test_score_utils.py::test_score_passing_boundary PASSED                                                                                           [  9%]
tests/month01/day11/test_score_utils.py::test_score_upper_boundary PASSED                                                                                             [ 10%]
tests/month01/day11/test_score_utils.py::test_score_above_maximum PASSED                                                                                              [ 11%]
tests/month01/day11/test_score_utils.py::test_empty_scores PASSED                                                                                                     [ 12%]
tests/month01/day11/test_score_utils.py::test_all_passing PASSED                                                                                                      [ 13%]
tests/month01/day11/test_score_utils.py::test_partially_passing PASSED                                                                                                [ 14%]
tests/month01/day11/test_score_utils.py::test_all_failing PASSED                                                                                                      [ 16%]
tests/month01/day11/test_score_utils.py::test_passing_boundary PASSED                                                                                                 [ 17%]
tests/month01/day12/test_parametrize_demo.py::test_multiply[2-3-6] PASSED                                                                                             [ 18%]
tests/month01/day12/test_parametrize_demo.py::test_multiply[0-5-0] PASSED                                                                                             [ 19%]
tests/month01/day12/test_parametrize_demo.py::test_multiply[-2-4--8] PASSED                                                                                           [ 20%]
tests/month01/day12/test_score_classifier.py::test_classify_score[0-Fail] PASSED                                                                                      [ 21%]
tests/month01/day12/test_score_classifier.py::test_classify_score[60-Pass] PASSED                                                                                     [ 22%]
tests/month01/day12/test_score_classifier.py::test_classify_score[50.9-Invalid] PASSED                                                                                [ 24%]
tests/month01/day12/test_score_classifier.py::test_classify_score[59-Fail] PASSED                                                                                     [ 25%]
tests/month01/day12/test_score_classifier.py::test_classify_score[100-Pass] PASSED                                                                                    [ 26%]
tests/month01/day12/test_score_classifier.py::test_classify_score[True-Invalid] PASSED                                                                                [ 27%]
tests/month01/day12/test_score_classifier.py::test_classify_score[abc-Invalid] PASSED                                                                                 [ 28%]
tests/month01/day12/test_score_classifier.py::test_classify_score[-1-Invalid] PASSED                                                                                  [ 29%]
tests/month01/day12/test_score_classifier.py::test_classify_score[101-Invalid] PASSED                                                                                 [ 31%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[-1-False] PASSED                                                                          [ 32%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[0-True] PASSED                                                                            [ 33%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[-10-False] PASSED                                                                         [ 34%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[101-False] PASSED                                                                         [ 35%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[100-True] PASSED                                                                          [ 36%]
tests/month01/day13/test_student_report_core.py::test_empty_statistics PASSED                                                                                         [ 37%]
tests/month01/day13/test_student_report_core.py::test_passing_empty_dict PASSED                                                                                       [ 39%]
tests/month01/day13/test_student_report_core.py::test_single_student PASSED                                                                                           [ 40%]
tests/month01/day13/test_student_report_core.py::test_all_passing PASSED                                                                                              [ 41%]
tests/month01/day13/test_student_report_core.py::test_all_failing PASSED                                                                                              [ 42%]
tests/month01/day13/test_student_report_core.py::test_passing_boundary PASSED                                                                                         [ 43%]
tests/month01/day13/test_student_report_core.py::test_highest_lowest PASSED                                                                                           [ 44%]
tests/month01/day13/test_student_report_core.py::test_average_score PASSED                                                                                            [ 45%]
tests/month01/day13/test_student_report_core.py::test_no_side_effect_statistics PASSED                                                                                [ 47%]
tests/month01/day13/test_student_report_core.py::test_no_side_effect_passing PASSED                                                                                   [ 48%]
tests/month01/day14/test_challenges.py::test_parse_minutes[0-0] PASSED                                                                                                [ 49%]
tests/month01/day14/test_challenges.py::test_parse_minutes[180-180] PASSED                                                                                            [ 50%]
tests/month01/day14/test_challenges.py::test_parse_minutes[-1-None] PASSED                                                                                            [ 51%]
tests/month01/day14/test_challenges.py::test_parse_minutes[190-None] PASSED                                                                                           [ 52%]
tests/month01/day14/test_challenges.py::test_parse_minutes[abc-None] PASSED                                                                                           [ 54%]
tests/month01/day14/test_challenges.py::test_parse_minutes[-None] PASSED                                                                                              [ 55%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform0-2-expect0] PASSED                                                                              [ 56%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform1-0-expect1] PASSED                                                                              [ 57%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform2-8-expect2] PASSED                                                                              [ 58%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform3-3-expect3] PASSED                                                                              [ 59%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform4-4-expect4] PASSED                                                                              [ 60%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[0-0] PASSED                                                                                         [ 62%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[180-180] PASSED                                                                                     [ 63%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[-1-None] PASSED                                                                                     [ 64%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[181-None] PASSED                                                                                    [ 65%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[ -None] PASSED                                                                                      [ 66%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[abc-None] PASSED                                                                                    [ 67%]
tests/month01/day14/test_study_report_core.py::test_build_study_report PASSED                                                                                         [ 68%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade0-10-expect0] PASSED                                                                                 [ 70%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade1-30-expect1] PASSED                                                                                 [ 71%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade2-30-expect2] PASSED                                                                                 [ 72%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade3-0-expect3] PASSED                                                                                  [ 73%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus_does_not_modify_original PASSED                                                                           [ 74%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items0-2-expected0] PASSED                                                                             [ 75%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items1-5-expected1] PASSED                                                                             [ 77%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items2-10-expected2] PASSED                                                                            [ 78%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items3-0-expected3] PASSED                                                                             [ 79%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items4-3-expected4] PASSED                                                                             [ 80%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[None-3-expected5] PASSED                                                                               [ 81%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[hello-2-lo] PASSED                                                                                     [ 82%]
tests/month01/day15/test_day14_regression.py::test_take_last_n_returns_new_list PASSED                                                                                [ 83%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_normal PASSED                                                                                   [ 85%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_empty_input PASSED                                                                              [ 86%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_all_invalid PASSED                                                                              [ 87%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_all_met_goal PASSED                                                                             [ 88%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_valid[55-55] PASSED                                                                         [ 89%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_valid[0-0] PASSED                                                                           [ 90%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_valid[100-100] PASSED                                                                       [ 91%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_type_error PASSED                                                                           [ 93%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_value_error PASSED                                                                          [ 94%]
tests/month01/day16/test_score_importer.py::test_import_scores_mixed_data PASSED                                                                                      [ 95%]
tests/month01/day16/test_score_importer.py::test_import_scores_all_valid PASSED                                                                                       [ 96%]
tests/month01/day16/test_score_importer.py::test_import_scores_all_invalid PASSED                                                                                     [ 97%]
tests/month01/day16/test_score_importer.py::test_import_scores_empty_dict PASSED                                                                                      [ 98%]
tests/month01/day16/test_score_importer.py::test_import_scores_does_not_modify_input PASSED                                                                           [100%]

============================================================================ 87 passed in 0.17s ============================================================================

是否补齐 Day 15 遗留的测试证据：

## 6. Debugging（调试记录）

实际遇到的错误：单独运行 Day 16 测试正常，但是运行 Month 01 全部测试时，pytest 报错 import file mismatch。

错误原因：Day 12 和 Day 16 都存在 test_score_validation.py 文件。pytest 在收集测试时发生了同名模块导入冲突。

如何修复：将 Day 16 的测试文件重命名为 test_day16_score_validation.py，确保不同测试模块的名称唯一。

修复后怎样验证：重新运行 Day 16 测试以及 Month 01 完整回归测试，并记录实际通过数量及失败数量。

## 7. Reflection（学习反思）

今天最重要的新知识：raise和pytest.raise的使用

我现在能否解释何时使用 raise、何时使用 except：需要自己提出异常用raise,需要处理可能的异常用ecxept

哪些代码是我独立完成的：所以

今天仍然需要加强的知识：暂无

## 8. Next Step（下一步）

等待 Day 16 代码审查与下一天学习任务。