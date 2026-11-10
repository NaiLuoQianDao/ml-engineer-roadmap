# Day 19 — CSV & JSON Processing

**Date:** 2026-11-10  
**Stage:** Month 01 · Week 03  
**Topic:** CSV Reading, JSON Writing & Data Validation

---

## 1. Learning Goals

- [x] 理解 CSV 文件的基本结构和用途
- [x] 学习 `csv.DictReader()` 的使用方法
- [x] 理解 `reader.fieldnames`、`reader` 和 `row` 的区别
- [x] 学习 `json.dump()` 和 `json.load()`
- [x] 实现 CSV 数据读取与验证
- [x] 实现 JSON 文件写入
- [x] 使用 `tmp_path` 测试文件操作
- [x] 完成 CSV → JSON 集成测试
- [x] Day 19 测试全部通过

## 2. Key Concepts

### 2.1 CSV — Comma-Separated Values

CSV 是一种使用逗号分隔数据字段的文本文件格式，经常用于存储表格数据。

CSV 通常包含 Header（表头）和 Rows（数据行）。

例如：

```csv
name,minutes
Alice,45
Bob,60
```

第一行表示字段名称，后续每一行表示一条记录。

CSV 中的数字在使用 `csv.DictReader()` 读取后通常仍是字符串，因此需要进行类型转换和有效性验证。

### 2.2 csv.DictReader

`csv.DictReader()` 可以将 CSV 中的每条数据记录转换为字典，字典的键来自 CSV 表头。

例如：

```python
{"name": "Alice", "minutes": "45"}
```

`reader.fieldnames` 用于获取 CSV 的表头列表，例如：

```python
["name", "minutes"]
```

`reader` 是 CSV 读取器，负责依次提供数据。

`row` 是遍历过程中当前的一条记录，可以通过 `row["name"]` 获取姓名。

相比直接使用 `split(",")`，`csv.DictReader()` 能按照 CSV 格式规则处理字段。例如，带引号的姓名 `"Li, Wei"` 不会被错误拆分。

### 2.3 JSON — JavaScript Object Notation

JSON 是一种常用的结构化数据交换格式。

它与 Python 的字典和列表结构相似，适合保存配置、处理结果和数据记录，也常用于 API 数据交换。

JSON 中的 Object 对应 Python 的字典，Array 对应 Python 的列表。

### 2.4 JSON Functions

| Function | Understanding |
|---|---|
| `json.dump()` | 将 Python 对象写入 JSON 文件 |
| `json.dumps()` | 将 Python 对象转换为 JSON 字符串 |
| `json.load()` | 从 JSON 文件读取并解析 Python 对象 |
| `json.loads()` | 将 JSON 字符串解析为 Python 对象 |

`ensure_ascii=False` 可以让中文字符直接保存在 JSON 文件中，而不是全部转成 Unicode 转义形式。

`indent=2` 用于格式化 JSON 输出，使内容更容易阅读。

### 2.5 Data Validation

从 CSV 读取的数据不一定符合程序要求，因此需要检查表头、字段内容和数据范围。

本次任务中：

- `ValueError`：用于报告表头、姓名或分钟数不符合要求的情况。
- `FileNotFoundError`：读取文件不存在时由文件操作自然抛出。
- `None`：Day 14 的 `parse_minutes()` 在分钟数不合法时返回的结果，需要转换为明确的验证异常。

## 3. Exercise A — CSV Reader

**File:** `src/ml_engineer_roadmap/experiment/month01/day19/study_records.py`

**Function:** `load_study_csv()`

### 3.1 Function Design

函数接收一个字符串路径或 `Path` 对象，读取 CSV 文件，并返回经过验证的数据记录列表。

函数处理过程：

1. 使用 `Path(path)` 统一文件路径类型。
2. 使用 `path.open()` 以 UTF-8 编码打开文件。
3. 使用 `csv.DictReader()` 读取 CSV。
4. 通过 `reader.fieldnames` 检查表头是否为 `["name", "minutes"]`。
5. 创建空列表保存验证后的记录。
6. 使用 `for row in reader` 遍历每条记录。
7. 使用 `.strip()` 清理姓名首尾空格。
8. 复用 Day 14 的 `parse_minutes()` 解析分钟数。
9. 对非法姓名或分钟数抛出 `ValueError`。
10. 将验证成功的记录加入结果列表，最后返回完整列表。

### 3.2 Validation Rules

**CSV 表头验证：**

通过 `reader.fieldnames` 与预期字段列表进行比较。缺少字段、字段顺序错误或存在额外字段时抛出 `ValueError`。

**姓名验证：**

首先使用 `.strip()` 去除首尾空白字符。如果处理后为空字符串，则认为姓名不合法。

**分钟数验证：**

复用 Day 14 的 `parse_minutes()`。有效的分钟数范围是 0–180，合法值转换为整数；如果返回 `None`，则抛出 `ValueError`。

**空文件处理：**

完全空的 CSV 文件没有有效表头，应抛出 `ValueError`。

只有正确表头、没有数据记录的 CSV 文件，应返回空列表 `[]`。

**结果收集：**

通过 `result.append(row)` 收集验证成功的记录，在循环结束后使用 `return result` 返回完整列表，而不是返回 `DictReader` 对象。

## 4. Exercise B — JSON Writer

**File:** `src/ml_engineer_roadmap/experiment/month01/day19/study_records.py`

**Function:** `save_study_json()`

### 4.1 Function Design

函数接收文件路径和已经验证的数据记录列表，将记录写入 JSON 文件。

主要实现：

1. 使用 `Path(path)` 将路径转换为 `Path` 对象。
2. 使用 `path.open("w", encoding="utf-8")` 打开输出文件。
3. 使用 `json.dump()` 将数据写入 JSON。
4. 指定 `ensure_ascii=False`，支持中文字符直接保存。
5. 指定 `indent=2`，让文件内容具有清晰缩进。
6. 写入完成后返回 `None`。

### 4.2 Design Decisions

使用 `json.dump()`，因为本次任务需要将 Python 数据直接保存到文件，而不是只生成 JSON 字符串。

使用 `"w"` 模式写入文件，因此目标文件已经存在时会被覆盖。

函数不会直接修改传入的 `records` 列表，保持输入数据不变。

## 5. Testing Evidence

### 5.1 Day 19 Tests

**测试文件：**

`tests/month01/day19/test_day19_study_records.py`

**测试命令：**

```powershell
uv run python -m pytest tests/month01/day19/ -v
```

**测试环境：**

- Operating System: Windows
- Python: 3.12.14
- pytest: 9.1.1

**实际测试结果：**

```text
collected 22 items
22 passed in 0.26s
```

**通过数量：** 22  
**失败数量：** 0

### 5.2 Test Coverage

已通过的测试涉及：

- 正常 CSV 文件读取
- 只有表头的 CSV
- 完全空的 CSV
- 非法或不完整的表头
- 空白姓名
- 姓名和分钟数首尾空白
- 非法分钟数，包括 `abc`、`-1`、`181`
- 读取不存在的文件
- 重复姓名记录
- 字符串形式的文件路径
- 包含逗号的姓名
- 正常 JSON 文件写入
- 中文姓名保存
- 空列表 JSON 写入
- JSON 字符串路径
- 覆盖已有 JSON 文件
- 不修改原始记录
- CSV → JSON 集成测试

### 5.3 Month 01 Regression Tests

**测试命令：**

```powershell
uv run python -m pytest tests/month01/ -v
```

**实际测试结果：** (ml-engineer-roadmap) PS C:\Users\lk120\dev\ml-engineer-roadmap> uv run python -m pytest tests/month01/ -v      
========================================= test session starts =========================================
platform win32 -- Python 3.12.14, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\lk120\dev\ml-engineer-roadmap\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\lk120\dev\ml-engineer-roadmap
configfile: pyproject.toml
collected 144 items                                                                                    

tests/month01/day11/test_bug_hunt.py::test_positive_numbers PASSED                               [  0%]
tests/month01/day11/test_bug_hunt.py::test_mixed_numbers PASSED                                  [  1%]
tests/month01/day11/test_bug_hunt.py::test_special_case PASSED                                   [  2%]
tests/month01/day11/test_first.py::test_addition PASSED                                          [  2%]
tests/month01/day11/test_first.py::test_subtraction PASSED                                       [  3%]
tests/month01/day11/test_score_utils.py::test_score_below_minimum PASSED                         [  4%]
tests/month01/day11/test_score_utils.py::test_score_lower_boundary PASSED                        [  4%]
tests/month01/day11/test_score_utils.py::test_score_passing_boundary PASSED                      [  5%]
tests/month01/day11/test_score_utils.py::test_score_upper_boundary PASSED                        [  6%]
tests/month01/day11/test_score_utils.py::test_score_above_maximum PASSED                         [  6%]
tests/month01/day11/test_score_utils.py::test_empty_scores PASSED                                [  7%]
tests/month01/day11/test_score_utils.py::test_all_passing PASSED                                 [  8%]
tests/month01/day11/test_score_utils.py::test_partially_passing PASSED                           [  9%]
tests/month01/day11/test_score_utils.py::test_all_failing PASSED                                 [  9%]
tests/month01/day11/test_score_utils.py::test_passing_boundary PASSED                            [ 10%]
tests/month01/day12/test_parametrize_demo.py::test_multiply[2-3-6] PASSED                        [ 11%]
tests/month01/day12/test_parametrize_demo.py::test_multiply[0-5-0] PASSED                        [ 11%]
tests/month01/day12/test_parametrize_demo.py::test_multiply[-2-4--8] PASSED                      [ 12%]
tests/month01/day12/test_score_classifier.py::test_classify_score[0-Fail] PASSED                 [ 13%]
tests/month01/day12/test_score_classifier.py::test_classify_score[60-Pass] PASSED                [ 13%]
tests/month01/day12/test_score_classifier.py::test_classify_score[50.9-Invalid] PASSED           [ 14%]
tests/month01/day12/test_score_classifier.py::test_classify_score[59-Fail] PASSED                [ 15%]
tests/month01/day12/test_score_classifier.py::test_classify_score[100-Pass] PASSED               [ 15%]
tests/month01/day12/test_score_classifier.py::test_classify_score[True-Invalid] PASSED           [ 16%]
tests/month01/day12/test_score_classifier.py::test_classify_score[abc-Invalid] PASSED            [ 17%]
tests/month01/day12/test_score_classifier.py::test_classify_score[-1-Invalid] PASSED             [ 18%]
tests/month01/day12/test_score_classifier.py::test_classify_score[101-Invalid] PASSED            [ 18%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[-1-False] PASSED     [ 19%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[0-True] PASSED       [ 20%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[-10-False] PASSED    [ 20%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[101-False] PASSED    [ 21%]
tests/month01/day12/test_score_validation.py::test_valid_score_parametrized[100-True] PASSED     [ 22%]
tests/month01/day13/test_student_report_core.py::test_empty_statistics PASSED                    [ 22%]
tests/month01/day13/test_student_report_core.py::test_passing_empty_dict PASSED                  [ 23%]
tests/month01/day13/test_student_report_core.py::test_single_student PASSED                      [ 24%]
tests/month01/day13/test_student_report_core.py::test_all_passing PASSED                         [ 25%]
tests/month01/day13/test_student_report_core.py::test_all_failing PASSED                         [ 25%]
tests/month01/day13/test_student_report_core.py::test_passing_boundary PASSED                    [ 26%]
tests/month01/day13/test_student_report_core.py::test_highest_lowest PASSED                      [ 27%]
tests/month01/day13/test_student_report_core.py::test_average_score PASSED                       [ 27%]
tests/month01/day13/test_student_report_core.py::test_no_side_effect_statistics PASSED           [ 28%]
tests/month01/day13/test_student_report_core.py::test_no_side_effect_passing PASSED              [ 29%]
tests/month01/day14/test_challenges.py::test_parse_minutes[0-0] PASSED                           [ 29%]
tests/month01/day14/test_challenges.py::test_parse_minutes[180-180] PASSED                       [ 30%]
tests/month01/day14/test_challenges.py::test_parse_minutes[-1-None] PASSED                       [ 31%]
tests/month01/day14/test_challenges.py::test_parse_minutes[190-None] PASSED                      [ 31%]
tests/month01/day14/test_challenges.py::test_parse_minutes[abc-None] PASSED                      [ 32%]
tests/month01/day14/test_challenges.py::test_parse_minutes[-None] PASSED                         [ 33%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform0-2-expect0] PASSED         [ 34%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform1-0-expect1] PASSED         [ 34%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform2-8-expect2] PASSED         [ 35%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform3-3-expect3] PASSED         [ 36%]
tests/month01/day14/test_challenges.py::test_take_last_n[input_inform4-4-expect4] PASSED         [ 36%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[0-0] PASSED                    [ 37%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[180-180] PASSED                [ 38%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[-1-None] PASSED                [ 38%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[181-None] PASSED               [ 39%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[ -None] PASSED                 [ 40%]
tests/month01/day14/test_study_report_core.py::test_parse_minutes[abc-None] PASSED               [ 40%]
tests/month01/day14/test_study_report_core.py::test_build_study_report PASSED                    [ 41%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade0-10-expect0] PASSED            [ 42%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade1-30-expect1] PASSED            [ 43%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade2-30-expect2] PASSED            [ 43%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus[grade3-0-expect3] PASSED             [ 44%]
tests/month01/day15/test_bonus_transform.py::test_add_bonus_does_not_modify_original PASSED      [ 45%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items0-2-expected0] PASSED        [ 45%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items1-5-expected1] PASSED        [ 46%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items2-10-expected2] PASSED       [ 47%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items3-0-expected3] PASSED        [ 47%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[items4-3-expected4] PASSED        [ 48%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[None-3-expected5] PASSED          [ 49%]
tests/month01/day15/test_day14_regression.py::test_take_last_n[hello-2-lo] PASSED                [ 50%]
tests/month01/day15/test_day14_regression.py::test_take_last_n_returns_new_list PASSED           [ 50%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_normal PASSED              [ 51%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_empty_input PASSED         [ 52%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_all_invalid PASSED         [ 52%]
tests/month01/day15/test_day14_regression.py::test_build_study_report_all_met_goal PASSED        [ 53%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_valid[55-55] PASSED    [ 54%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_valid[0-0] PASSED      [ 54%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_valid[100-100] PASSED  [ 55%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_type_error PASSED      [ 56%]
tests/month01/day16/test_day16_score_validation.py::test_score_validation_value_error PASSED     [ 56%]
tests/month01/day16/test_score_importer.py::test_import_scores_mixed_data PASSED                 [ 57%]
tests/month01/day16/test_score_importer.py::test_import_scores_all_valid PASSED                  [ 58%]
tests/month01/day16/test_score_importer.py::test_import_scores_all_invalid PASSED                [ 59%]
tests/month01/day16/test_score_importer.py::test_import_scores_empty_dict PASSED                 [ 59%]
tests/month01/day16/test_score_importer.py::test_import_scores_does_not_modify_input PASSED      [ 60%]
tests/month01/day17/test_day17_label_validation.py::test_valid_labels[labels0] PASSED            [ 61%]
tests/month01/day17/test_day17_label_validation.py::test_valid_labels[labels1] PASSED            [ 61%]
tests/month01/day17/test_day17_label_validation.py::test_valid_labels[labels2] PASSED            [ 62%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_label_values[labels0] PASSED    [ 63%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_label_values[labels1] PASSED    [ 63%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_label_values[labels2] PASSED    [ 64%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_container_types[cat] PASSED     [ 65%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_container_types[None] PASSED    [ 65%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_container_types[labels2] PASSED [ 66%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_element_types[labels0] PASSED   [ 67%]
tests/month01/day17/test_day17_label_validation.py::test_invalid_element_types[labels1] PASSED   [ 68%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_evaluate_predictions[actual0-predicted0-expected0] PASSED [ 68%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_evaluate_predictions[actual1-predicted1-expected1] PASSED [ 69%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_evaluate_predictions[actual2-predicted2-expected2] PASSED [ 70%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_evaluate_predictions[actual3-predicted3-expected3] PASSED [ 70%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_different_lengths[actual0-predicted0] PASSED [ 71%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_different_lengths[actual1-predicted1] PASSED [ 72%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_invalid_label_values[actual0-predicted0] PASSED [ 72%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_invalid_label_values[actual1-predicted1] PASSED [ 73%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_invalid_input_type PASSED           [ 74%]
tests/month01/day17/test_day17_prediction_evaluator.py::test_does_not_modify_inputs PASSED       [ 75%]
tests/month01/day18/test_day18_file_io.py::test_load_valid_minutes PASSED                        [ 75%]
tests/month01/day18/test_day18_file_io.py::test_load_skips_blank_lines PASSED                    [ 76%]
tests/month01/day18/test_day18_file_io.py::test_load_empty_file PASSED                           [ 77%]
tests/month01/day18/test_day18_file_io.py::test_load_invalid_minutes[abc] PASSED                 [ 77%]
tests/month01/day18/test_day18_file_io.py::test_load_invalid_minutes[-1] PASSED                  [ 78%]
tests/month01/day18/test_day18_file_io.py::test_load_invalid_minutes[181] PASSED                 [ 79%]
tests/month01/day18/test_day18_file_io.py::test_load_missing_file PASSED                         [ 79%]
tests/month01/day18/test_day18_file_io.py::test_load_error_line_number PASSED                    [ 80%]
tests/month01/day18/test_day18_file_io.py::test_write_normal_summary PASSED                      [ 81%]
tests/month01/day18/test_day18_file_io.py::test_write_empty_summary PASSED                       [ 81%]
tests/month01/day18/test_day18_file_io.py::test_write_accepts_string_path PASSED                 [ 82%]
tests/month01/day18/test_day18_file_io.py::test_write_does_not_modify_input PASSED               [ 83%]
tests/month01/day18/test_day18_tmp_path_practice.py::test_create_and_read_file PASSED            [ 84%]
tests/month01/day18/test_day18_tmp_path_practice.py::test_numbers_file PASSED                    [ 84%]
tests/month01/day19/test_day19_study_records.py::test_load_valid_csv PASSED                      [ 85%]
tests/month01/day19/test_day19_study_records.py::test_csv_only_header PASSED                     [ 86%]
tests/month01/day19/test_day19_study_records.py::test_csv_completely_empty PASSED                [ 86%]
tests/month01/day19/test_day19_study_records.py::test_csv_invalid_header[name] PASSED            [ 87%]
tests/month01/day19/test_day19_study_records.py::test_csv_invalid_header[minutes,name] PASSED    [ 88%]
tests/month01/day19/test_day19_study_records.py::test_csv_invalid_header[name,minutes,extra] PASSED [ 88%]
tests/month01/day19/test_day19_study_records.py::test_csv_blank_name PASSED                      [ 89%]
tests/month01/day19/test_day19_study_records.py::test_csv_strip_whitespace PASSED                [ 90%]
tests/month01/day19/test_day19_study_records.py::test_csv_invalid_minutes[abc] PASSED            [ 90%]
tests/month01/day19/test_day19_study_records.py::test_csv_invalid_minutes[-1] PASSED             [ 91%]
tests/month01/day19/test_day19_study_records.py::test_csv_invalid_minutes[181] PASSED            [ 92%]
tests/month01/day19/test_day19_study_records.py::test_csv_missing_file PASSED                    [ 93%]
tests/month01/day19/test_day19_study_records.py::test_csv_duplicate_names PASSED                 [ 93%]
tests/month01/day19/test_day19_study_records.py::test_csv_accepts_string_path PASSED             [ 94%]
tests/month01/day19/test_day19_study_records.py::test_csv_quoted_comma PASSED                    [ 95%]
tests/month01/day19/test_day19_study_records.py::test_json_normal_write PASSED                   [ 95%]
tests/month01/day19/test_day19_study_records.py::test_json_chinese_name PASSED                   [ 96%]
tests/month01/day19/test_day19_study_records.py::test_json_empty_list PASSED                     [ 97%]
tests/month01/day19/test_day19_study_records.py::test_json_accepts_string_path PASSED            [ 97%]
tests/month01/day19/test_day19_study_records.py::test_json_overwrites_existing_file PASSED       [ 98%]
tests/month01/day19/test_day19_study_records.py::test_json_does_not_modify_input PASSED          [ 99%]
tests/month01/day19/test_day19_study_records.py::test_csv_to_json_integration PASSED             [100%]

========================================= 144 passed in 0.44s =========================================

### 5.4 Test Authorship

两个业务函数由自己独立编写，并根据导师的静态代码审查建议多次修改。

主要 pytest 测试代码由导师协助提供，自己负责运行测试、检查结果以及理解验证场景。

目前能够确认 Day 19 的 22 项本地测试已通过，但尚未进行独立环境或 GitHub CI 验证。

## 6. Debugging

### Problem 1 — CSV Header Validation

**问题：**

初版代码没有正确验证 CSV 表头，后续修改时曾将 `name` 拼写成 `neme`。

**原因：**

对 `row.keys()` 和 `reader.fieldnames` 的区别不熟悉，并存在字段名称拼写错误。

**解决方法：**

学习 `reader.fieldnames` 属性，并在遍历记录前统一检查表头。

**验证：**

Day 19 中正常表头与非法表头的测试均已通过。

### Problem 2 — Reader and Row Confusion

**问题：**

早期代码混淆了 `reader` 和 `row`，尝试使用读取器访问当前记录字段。

**原因：**

没有完全理解 CSV 读取器与当前数据行字典之间的区别。

**解决方法：**

在 `for row in reader` 循环内，通过 `row["name"]` 和 `row["minutes"]` 读取及处理当前记录。

**验证：**

正常读取、多条记录和重复姓名测试均已通过。

### Problem 3 — Return Position and Result Collection

**问题：**

最初将 `return reader` 放在循环内部，导致无法正确处理全部记录，且返回类型不符合要求。

**原因：**

对 `for` 循环、结果列表和 `return` 的执行顺序理解不够清楚。

**解决方法：**

在循环前创建空列表，每次验证成功后使用 `.append()`，并在循环结束后返回列表。

**验证：**

正常 CSV、只有表头以及多条记录测试均已通过。

### Problem 4 — Data Validation

**问题：**

初版代码没有完整处理空白姓名和 `parse_minutes()` 返回 `None` 的情况。

**原因：**

没有充分考虑输入数据非法时函数应该如何响应。

**解决方法：**

使用 `.strip()` 清理姓名，并对非法姓名或分钟数明确抛出 `ValueError`。

**验证：**

空白姓名、非法分钟数和数据清理测试均已通过。

**说明：** 上述问题来自编写过程中的源码审查与修改，不代表每个问题都曾产生 pytest 运行失败。

## 7. Reflection

**今天最重要的新知识：**

学习了使用 `csv.DictReader()` 读取结构化数据，以及使用 `json.dump()` 保存 Python 数据。进一步理解了文件读取、数据验证、类型转换和结果输出之间的关系。

**今天独立完成的内容：**

独立编写 `load_study_csv()` 和 `save_study_json()` 两个函数，并根据代码审查反馈修改了 CSV 表头验证、循环逻辑和非法数据处理。

**今天遇到的最大困难：**

最初没有完全理解 `reader`、`row` 和结果列表的区别，导致字段访问、循环返回及数据收集出现逻辑问题。

**对 reader、row 和 result 的新理解：**

`reader` 用于从 CSV 文件中依次读取记录，`row` 代表当前处理的字典，`result` 用于保存所有验证成功的数据。只有完成整个循环后，才能返回完整的数据集合。

**对独立解决问题能力的认识：**

今天通过多次修改逐步完善了读取函数。对 CSV 文件处理的基本流程有了更明确的认识，但仍需要通过不依赖完整参考代码的新练习，检验是否真正掌握。

**仍需加强的知识：**

- CSV 文件的边界情况与异常处理
- 独立设计 pytest 测试
- 循环中的数据收集与函数返回逻辑
- 多个函数之间的数据传递及集成测试

## 8. GitHub Submission

**Planned Commit Message:**

`Complete day 19 CSV and JSON processing`

**提交内容：**

- `study_records.py`
- `test_day19_study_records.py`
- `day19.md`

## 9. Next Step

**Day 20 — Integrated Data Processing Practice**

下一步将 CSV 读取、数据验证、统计处理与 JSON 输出组合起来，练习一个更加完整的数据处理流程。

继续为 Month 01 · Week 03 综合考核以及后续 Student Data Processing Pipeline 项目做准备。