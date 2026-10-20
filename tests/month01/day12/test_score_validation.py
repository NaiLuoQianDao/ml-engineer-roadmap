import pytest

from ml_engineer_roadmap.experiment.month01.day11.score_utils import (
    is_valid_score,
)


@pytest.mark.parametrize(
    "score, expected",
    [
        (-1, False),
        (0, True),
        (-10, False),
        (101, False),
        (100, True),
    ],
)
def test_valid_score_parametrized(score, expected):
    assert is_valid_score(score) is expected