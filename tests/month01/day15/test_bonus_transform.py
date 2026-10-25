import pytest
from ml_engineer_roadmap.experiment.month01.day15.bonus_transform import add_bonus

test_list = [30, 40, 50]
@pytest.mark.parametrize(
    'grade, add_grade, expect',
    [
    ([50, 60, 70, 80], 10, [60, 70, 80, 90]),
    ([50, 60, 70, 80], 30, [80, 90, 100, 100]),
    ([], 30, []),
    ([50, 60, 70, 80], 0, [50, 60, 70, 80]),
    ]
)
def test_add_bonus(grade, add_grade, expect):
    # 这里只测试返回值是否正确
    assert add_bonus(grade, add_grade) == expect

# 👇 新增一个测试，单独测试不可变性 (Immutability)
def test_add_bonus_does_not_modify_original():
    # 调用业务函数 add_bonus，而不是 test_add_bonus
    result = add_bonus(test_list, 15)
    assert result is not test_list
    assert test_list == [30, 40, 50] # 确保原列表没被改变