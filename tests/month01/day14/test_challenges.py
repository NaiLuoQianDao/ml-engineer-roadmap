import pytest
from ml_engineer_roadmap.experiment.month01.day14.challenges import (
    parse_minutes,
    take_last_n
)

@pytest.mark.parametrize(
        'input_inform, expect',
        [
            ('0', 0),
            ('180', 180),
            ('-1', None),
            ('190', None),
            ('abc', None),
            ('', None)
        ],
)

def test_parse_minutes(input_inform, expect):
    assert parse_minutes(input_inform) == expect

@pytest.mark.parametrize(
    'input_inform, n, expect',
    [
        ([], 2, []),
        ([1,2,3,4], 0, []),
        ([1, 2, 3, 4, 5, 6], 8, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 4, 5, 6], 3, [4, 5, 6]),
        ([3, 3, 3, 3, 3, 3, 3], 4, [3, 3, 3, 3]),
    ],
)
def test_take_last_n(input_inform, n, expect):
    assert take_last_n(input_inform, n) == expect