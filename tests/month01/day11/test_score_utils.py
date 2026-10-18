from ml_engineer_roadmap.experiment.month01.day11.score_utils import (
    is_valid_score,
    count_passing,
)


# ==========================
# is_valid_score 测试
# ==========================

def test_score_below_minimum():
    assert is_valid_score(-1) is False


def test_score_lower_boundary():
    assert is_valid_score(0) is True


def test_score_passing_boundary():
    assert is_valid_score(60) is True


def test_score_upper_boundary():
    assert is_valid_score(100) is True


def test_score_above_maximum():
    assert is_valid_score(101) is False


# ==========================
# count_passing 测试
# ==========================

def test_empty_scores():
    assert count_passing([]) == 0


def test_all_passing():
    assert count_passing([60, 70, 80, 90]) == 4


def test_partially_passing():
    assert count_passing([40, 50, 60, 70]) == 2


def test_all_failing():
    assert count_passing([10, 20, 30, 40]) == 0


def test_passing_boundary():
    assert count_passing([58, 59, 60, 61]) == 2