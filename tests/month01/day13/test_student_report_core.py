import pytest

from ml_engineer_roadmap.experiment.month01.day13.student_report_core import (
    calculate_statistics,
    get_passing_students
)

def test_empty_statistics():
    assert calculate_statistics({}) is None

def test_passing_empty_dict():
    assert get_passing_students({}) == {}

def test_single_student():
    students = {"Alice": 75}
    stats = calculate_statistics(students)
    assert stats["count"] == 1
    assert stats["highest"] == 75
    assert stats["lowest"] == 75
    assert stats["average"] == 75.0
    assert stats["passing_count"] == 1

def test_all_passing():
    students = {"Alice": 90, "Bob": 60, "Charlie": 100}
    stats = calculate_statistics(students)
    assert stats["passing_count"] == 3
    
    passing = get_passing_students(students)
    assert len(passing) == 3
    assert passing == students

def test_all_failing():
    students = {"Alice": 59, "Bob": 0, "Charlie": 30}
    stats = calculate_statistics(students)
    assert stats["passing_count"] == 0
    
    passing = get_passing_students(students)
    assert passing == {}

def test_passing_boundary():
    students = {"Alice": 59, "Bob": 60}

    expected = {"Bob": 60}

    assert get_passing_students(students) == expected

def test_highest_lowest():
    students = {"A": 10, "B": 95, "C": 50, "D": 88}
    stats = calculate_statistics(students)
    assert stats["highest"] == 95
    assert stats["lowest"] == 10

def test_average_score():
    students = {"Alice": 90, "Bob": 60, "Charlie": 50}
    stats = calculate_statistics(students)
    # 90+60+50 = 200, 200/3 = 66.6666...
    assert stats["average"] == pytest.approx(66.66666666666667)

def test_no_side_effect_statistics():
    original = {"Alice": 59, "Bob": 60}
    # 调用函数前拷贝一份，用于对比
    original_copy = original.copy() 
    
    calculate_statistics(original)
    
    assert original == original_copy
    assert "Alice" in original
    assert original["Alice"] == 59

def test_no_side_effect_passing():
    original = {"Alice": 59, "Bob": 60}
    original_copy = original.copy()
    
    get_passing_students(original)
    
    assert original == original_copy
    assert "Alice" in original
    assert original["Alice"] == 59