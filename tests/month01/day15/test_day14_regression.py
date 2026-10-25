import pytest
from ml_engineer_roadmap.experiment.month01.day14.challenges import (
    take_last_n,
)
from ml_engineer_roadmap.experiment.month01.day14.study_report_core import (
    build_study_report,
)


@pytest.mark.parametrize(
    "items, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [4, 5]),       # 正常情况，取最后2个
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]), # 边界值：n 等于列表长度
        ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5]),# 边界值：n 大于列表长度，应返回全部
        ([1, 2, 3], 0, []),                 # 边界值：n 为 0（触发 else，返回空列表）
        ([], 3, []),                        # 边界值：空列表
        (None, 3, []),                      # 异常输入：items 为 None
        ("hello", 2, "lo"),                 # 测试字符串（支持切片）
    ]
)
def test_take_last_n(items, n, expected):
    assert take_last_n(items, n) == expected

# 额外测试：确保返回的是新列表（尤其是 n >= len 时使用了 items[:] 的情况）
def test_take_last_n_returns_new_list():
    original = [1, 2, 3]
    result = take_last_n(original, 5)
    assert result == original
    assert result is not original # 验证内存地址不同，说明是新列表



def test_build_study_report_normal():
    """测试正常混合数据（有效、无效、达标、未达标）"""
    raw_sessions = {
        "Monday": "45",     # 有效，未达标
        "Tuesday": "75",    # 有效，达标
        "Wednesday": "abc", # 无效
        "Thursday": "181",  # 无效（越界）
        "Friday": "0",      # 有效，未达标
    }
    
    result = build_study_report(raw_sessions)
    
    assert result['valid'] == {"Monday": 45, "Tuesday": 75, "Friday": 0}
    assert result['invalid_days'] == ["Wednesday", "Thursday"]
    assert result['count'] == 3
    assert result['total'] == 120  # 45 + 75 + 0
    assert result['average'] == 40.0 # 120 / 3
    assert result['met_goal'] == 1   # 只有周二 >= 60

def test_build_study_report_empty_input():
    """测试传入空字典的情况"""
    result = build_study_report({})
    
    assert result['valid'] == {}
    assert result['invalid_days'] == []
    assert result['count'] == 0
    assert result['total'] == 0
    assert result['average'] is None # 关键逻辑：没有有效数据时，平均值为 None
    assert result['met_goal'] == 0

def test_build_study_report_all_invalid():
    """测试全是无效数据的情况"""
    raw_sessions = {
        "Day1": "-5",
        "Day2": "text",
        "Day3": "200"
    }
    result = build_study_report(raw_sessions)
    
    assert result['valid'] == {}
    assert result['invalid_days'] == ["Day1", "Day2", "Day3"]
    assert result['count'] == 0
    assert result['total'] == 0
    assert result['average'] is None
    assert result['met_goal'] == 0

def test_build_study_report_all_met_goal():
    """测试所有有效数据都达标的情况"""
    raw_sessions = {
        "Mon": "60",   # 刚好达标边界
        "Tue": "120",
        "Wed": "90"
    }
    result = build_study_report(raw_sessions)
    
    assert result['valid'] == {"Mon": 60, "Tue": 120, "Wed": 90}
    assert result['invalid_days'] == []
    assert result['count'] == 3
    assert result['total'] == 270
    assert result['average'] == 90.0
    assert result['met_goal'] == 3