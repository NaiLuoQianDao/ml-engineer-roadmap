
from pathlib import Path

import pytest

from ml_engineer_roadmap.experiment.month01.day18.study_file_io import (
    load_study_minutes,
    write_study_summary,
)


# =========================
# Part A — 文件读取测试
# =========================

def test_load_valid_minutes(tmp_path):
    file_path = tmp_path / "minutes.txt"
    file_path.write_text(
        "45\n60\n0\n180\n",
        encoding="utf-8",
    )

    result = load_study_minutes(file_path)

    assert result == [45, 60, 0, 180]


def test_load_skips_blank_lines(tmp_path):
    file_path = tmp_path / "minutes.txt"
    file_path.write_text(
        "\n45\n   \n60\n\n",
        encoding="utf-8",
    )

    assert load_study_minutes(file_path) == [45, 60]


def test_load_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    assert load_study_minutes(file_path) == []


@pytest.mark.parametrize(
    "invalid_value",
    ["abc", "-1", "181"],
)
def test_load_invalid_minutes(tmp_path, invalid_value):
    file_path = tmp_path / "invalid.txt"
    file_path.write_text(
        invalid_value,
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_study_minutes(file_path)


def test_load_missing_file(tmp_path):
    file_path = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        load_study_minutes(file_path)


def test_load_error_line_number(tmp_path):
    file_path = tmp_path / "invalid_line.txt"
    file_path.write_text(
        "45\nabc\n90\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        load_study_minutes(file_path)


# =========================
# Part B — 文件写入测试
# =========================

def test_write_normal_summary(tmp_path):
    file_path = tmp_path / "summary.txt"

    write_study_summary(file_path, [45, 60, 90])

    content = file_path.read_text(encoding="utf-8")

    assert content == (
        "count=3\n"
        "total=195\n"
        "average=65.0\n"
    )


def test_write_empty_summary(tmp_path):
    file_path = tmp_path / "empty_summary.txt"

    write_study_summary(file_path, [])

    content = file_path.read_text(encoding="utf-8")

    assert content == (
        "count=0\n"
        "total=0\n"
        "average=N/A\n"
    )


def test_write_accepts_string_path(tmp_path):
    file_path = str(tmp_path / "string_path.txt")

    write_study_summary(file_path, [30, 60])

    content = Path(file_path).read_text(encoding="utf-8")

    assert content == (
        "count=2\n"
        "total=90\n"
        "average=45.0\n"
    )


def test_write_does_not_modify_input(tmp_path):
    file_path = tmp_path / "summary.txt"

    minutes = [45, 60, 90]
    original = minutes.copy()

    write_study_summary(file_path, minutes)

    assert minutes == original
