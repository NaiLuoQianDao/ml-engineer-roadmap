import pytest

from ml_engineer_roadmap.experiment.month01.day17.prediction_evaluator import (
    evaluate_predictions,
)


@pytest.mark.parametrize(
    "actual, predicted, expected",
    [
        (
            ["cat", "dog", "dog", "cat"],
            ["cat", "cat", "dog", "dog"],
            {
                "total": 4,
                "correct": 2,
                "incorrect": 2,
                "accuracy": 0.5,
                "wrong_indices": [1, 3],
            },
        ),
        (
            ["cat", "dog"],
            ["cat", "dog"],
            {
                "total": 2,
                "correct": 2,
                "incorrect": 0,
                "accuracy": 1.0,
                "wrong_indices": [],
            },
        ),
        (
            ["cat", "dog"],
            ["dog", "cat"],
            {
                "total": 2,
                "correct": 0,
                "incorrect": 2,
                "accuracy": 0.0,
                "wrong_indices": [0, 1],
            },
        ),
        (
            [],
            [],
            {
                "total": 0,
                "correct": 0,
                "incorrect": 0,
                "accuracy": None,
                "wrong_indices": [],
            },
        ),
    ],
)
def test_evaluate_predictions(actual, predicted, expected):
    assert evaluate_predictions(actual, predicted) == expected


@pytest.mark.parametrize(
    "actual, predicted",
    [
        (["cat"], ["cat", "dog"]),
        (["cat", "dog"], ["cat"]),
    ],
)
def test_different_lengths(actual, predicted):
    with pytest.raises(ValueError):
        evaluate_predictions(actual, predicted)


@pytest.mark.parametrize(
    "actual, predicted",
    [
        (["cat", "bird"], ["cat", "dog"]),
        (["cat", "dog"], ["cat", "bird"]),
    ],
)
def test_invalid_label_values(actual, predicted):
    with pytest.raises(ValueError):
        evaluate_predictions(actual, predicted)


def test_invalid_input_type():
    with pytest.raises(TypeError):
        evaluate_predictions(
            "cat",
            ["cat", "dog", "cat"],
        )


def test_does_not_modify_inputs():
    actual = ["cat", "dog", "cat"]
    predicted = ["dog", "dog", "cat"]

    original_actual = actual.copy()
    original_predicted = predicted.copy()

    evaluate_predictions(actual, predicted)

    assert actual == original_actual
    assert predicted == original_predicted