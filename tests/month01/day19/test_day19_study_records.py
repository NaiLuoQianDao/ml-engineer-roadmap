import json, csv
import pytest
from ml_engineer_roadmap.experiment.month01.day19.study_records import (
    load_study_csv,
    save_study_json
)


def test_load_valid_csv(tmp_path):
    file_path = tmp_path / "study.csv"

    file_path.write_text(
        "name,minutes\n"
        "Alice,45\n"
        "Bob,60\n",
        encoding="utf-8",
    )

    result = load_study_csv(file_path)

    assert result == [
        {"name": "Alice", "minutes": 45},
        {"name": "Bob", "minutes": 60},
    ]


# ==========================================
# Part A — CSV 文件读取测试
# ==========================================

def test_csv_only_header(tmp_path):
    """只有正确表头时，应该返回空列表。"""
    file_path = tmp_path / "header_only.csv"
    file_path.write_text(
        "name,minutes\n",
        encoding="utf-8",
    )

    result = load_study_csv(file_path)

    assert result == []


def test_csv_completely_empty(tmp_path):
    """完全空的 CSV 文件缺少表头。"""
    file_path = tmp_path / "empty.csv"
    file_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        load_study_csv(file_path)


@pytest.mark.parametrize(
    "header",
    [
        "name",
        "minutes,name",
        "name,minutes,extra",
    ],
)
def test_csv_invalid_header(tmp_path, header):
    """缺少列、顺序错误或出现额外列。"""
    file_path = tmp_path / "bad_header.csv"
    file_path.write_text(
        header + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_study_csv(file_path)


def test_csv_blank_name(tmp_path):
    """姓名只有空格时应该抛出异常。"""
    file_path = tmp_path / "blank_name.csv"
    file_path.write_text(
        "name,minutes\n"
        "   ,60\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_study_csv(file_path)


def test_csv_strip_whitespace(tmp_path):
    """姓名和分钟数字符串允许首尾空格。"""
    file_path = tmp_path / "whitespace.csv"
    file_path.write_text(
        "name,minutes\n"
        " Alice , 60 \n",
        encoding="utf-8",
    )

    result = load_study_csv(file_path)

    assert result == [
        {"name": "Alice", "minutes": 60}
    ]


@pytest.mark.parametrize(
    "invalid_minutes",
    ["abc", "-1", "181"],
)
def test_csv_invalid_minutes(tmp_path, invalid_minutes):
    """检查非数字和超出范围的分钟数。"""
    file_path = tmp_path / "invalid_minutes.csv"
    file_path.write_text(
        f"name,minutes\nAlice,{invalid_minutes}\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_study_csv(file_path)


def test_csv_missing_file(tmp_path):
    """文件不存在时保留 FileNotFoundError。"""
    file_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_study_csv(file_path)


def test_csv_duplicate_names(tmp_path):
    """同一姓名可以有多条学习记录。"""
    file_path = tmp_path / "duplicates.csv"
    file_path.write_text(
        "name,minutes\n"
        "Alice,45\n"
        "Alice,90\n",
        encoding="utf-8",
    )

    result = load_study_csv(file_path)

    assert result == [
        {"name": "Alice", "minutes": 45},
        {"name": "Alice", "minutes": 90},
    ]


def test_csv_accepts_string_path(tmp_path):
    """读取函数也应该接受字符串路径。"""
    file_path = tmp_path / "string_path.csv"
    file_path.write_text(
        "name,minutes\nBob,30\n",
        encoding="utf-8",
    )

    result = load_study_csv(str(file_path))

    assert result == [
        {"name": "Bob", "minutes": 30}
    ]


def test_csv_quoted_comma(tmp_path):
    """姓名包含逗号时，CSV 解析应保持完整。"""
    file_path = tmp_path / "quoted.csv"
    file_path.write_text(
        'name,minutes\n"Li, Wei",45\n',
        encoding="utf-8",
    )

    result = load_study_csv(file_path)

    assert result == [
        {"name": "Li, Wei", "minutes": 45}
    ]


# ==========================================
# Part B — JSON 文件写入测试
# ==========================================

def test_json_normal_write(tmp_path):
    """正常保存并读取 JSON 数据。"""
    file_path = tmp_path / "records.json"

    records = [
        {"name": "Alice", "minutes": 45},
        {"name": "Bob", "minutes": 60},
    ]

    save_study_json(file_path, records)

    with file_path.open("r", encoding="utf-8") as file:
        result = json.load(file)

    assert result == records


def test_json_chinese_name(tmp_path):
    """检查中文姓名是否正确保存。"""
    file_path = tmp_path / "chinese.json"

    records = [
        {"name": "张三", "minutes": 90}
    ]

    save_study_json(file_path, records)

    content = file_path.read_text(encoding="utf-8")

    assert "张三" in content

    with file_path.open("r", encoding="utf-8") as file:
        result = json.load(file)

    assert result == records


def test_json_empty_list(tmp_path):
    """空列表应该保存为合法 JSON 数组。"""
    file_path = tmp_path / "empty.json"

    save_study_json(file_path, [])

    with file_path.open("r", encoding="utf-8") as file:
        result = json.load(file)

    assert result == []


def test_json_accepts_string_path(tmp_path):
    """写入函数应该接受字符串路径。"""
    file_path = tmp_path / "string_output.json"

    records = [
        {"name": "Alice", "minutes": 30}
    ]

    save_study_json(str(file_path), records)

    with file_path.open("r", encoding="utf-8") as file:
        result = json.load(file)

    assert result == records


def test_json_overwrites_existing_file(tmp_path):
    """输出文件存在时，应该覆盖旧内容。"""
    file_path = tmp_path / "existing.json"
    file_path.write_text(
        "old content",
        encoding="utf-8",
    )

    records = [
        {"name": "Bob", "minutes": 80}
    ]

    save_study_json(file_path, records)

    with file_path.open("r", encoding="utf-8") as file:
        result = json.load(file)

    assert result == records


def test_json_does_not_modify_input(tmp_path):
    """函数不能修改传入的记录。"""
    file_path = tmp_path / "unchanged.json"

    records = [
        {"name": "Alice", "minutes": 45}
    ]
    original = [
        record.copy() for record in records
    ]

    returned = save_study_json(file_path, records)

    assert records == original
    assert returned is None


# ==========================================
# Part C — 集成测试
# ==========================================

def test_csv_to_json_integration(tmp_path):
    """验证 CSV 读取和 JSON 写入能协作。"""
    csv_path = tmp_path / "study.csv"
    json_path = tmp_path / "study.json"

    csv_path.write_text(
        "name,minutes\n"
        "Alice,45\n"
        "Bob,60\n"
        "Alice,90\n",
        encoding="utf-8",
    )

    records = load_study_csv(csv_path)

    save_study_json(json_path, records)

    with json_path.open("r", encoding="utf-8") as file:
        result = json.load(file)

    assert result == [
        {"name": "Alice", "minutes": 45},
        {"name": "Bob", "minutes": 60},
        {"name": "Alice", "minutes": 90},
    ]
