import pytest
from ml_engineer_roadmap.experiment.month01.day22.prediction_accuracy import (
    prediction_accuracy,
)

# 测试 1：正常情况（部分正确）
def test_prediction_accuracy_normal():
    actual = ["cat", "dog", "dog"]
    predicted = ["cat", "cat", "dog"]
    assert prediction_accuracy(actual, predicted) == 2 / 3

# 测试 2：一条样本，预测错误 (有样本，但全猜错)
def test_prediction_accuracy_completely_wrong():
    actual = ["cat"]
    predicted = ["dog"]
    # 必须是 0.0 而不是 False 或空
    assert prediction_accuracy(actual, predicted) == 0.0

# 测试 3：两个列表都为空 (根本没有样本)
def test_prediction_accuracy_empty_lists():
    assert prediction_accuracy([], []) is None

# 测试 4：长度不一致 (抛出 ValueError)
def test_prediction_accuracy_length_mismatch():
    actual = ["cat", "dog", "cat"]
    predicted = ["dog"]
    with pytest.raises(ValueError):
        prediction_accuracy(actual, predicted)