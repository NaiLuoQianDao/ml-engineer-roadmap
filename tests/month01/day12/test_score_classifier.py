import pytest

from ml_engineer_roadmap.experiment.month01.day12.score_classifier import (
    classify_score,
)


@pytest.mark.parametrize(
    "score, expected",
    [
        (0, "Fail"),
        (60, "Pass"),
        (50.9, 'Invalid'),
        (59, "Fail"),
        (100, "Pass"),
        (True, "Invalid"),
        ('abc', "Invalid"),
        (-1, "Invalid"),
        (101, "Invalid"),
    ],
)
def test_classify_score(score, expected):
    assert classify_score(score) == expected