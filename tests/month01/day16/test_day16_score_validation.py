from ml_engineer_roadmap.experiment.month01.day16.score_validation import parse_score_strict
import pytest

# 1. 正常解析（参数化）
@pytest.mark.parametrize(
    'raw, out',
    [
        ('55', 55),
        ('0', 0),
        ('100', 100),
    ]
)
def test_score_validation_valid(raw, out):
    assert parse_score_strict(raw) == out

# 2. 类型错误测试 (TypeError)
def test_score_validation_type_error():
    with pytest.raises(TypeError):
        parse_score_strict(75)      # 传入 int
    with pytest.raises(TypeError):
        parse_score_strict(None)    # 传入 None

# 3. 值错误测试 (ValueError)
def test_score_validation_value_error():
    with pytest.raises(ValueError):
        parse_score_strict('abc')   # 非数字字符串
    with pytest.raises(ValueError):
        parse_score_strict('')      # 空字符串
    # 建议补充：越界测试（如果 "strict" 代表限制在 0-100 内）
    # with pytest.raises(ValueError):
    #     parse_score_strict('-1')
    # with pytest.raises(ValueError):
    #     parse_score_strict('101')