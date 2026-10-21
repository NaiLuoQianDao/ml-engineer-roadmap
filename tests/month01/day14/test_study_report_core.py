import pytest
from ml_engineer_roadmap.experiment.month01.day14.study_report_core import (
    parse_minutes,
    build_study_report,
)


@pytest.mark.parametrize(
    'ip, op',
    [
        ('0', 0),
        ('180', 180),
        ('-1', None),
        ('181', None),
        (' ', None),
        ('abc', None),
    ],    
)

def test_parse_minutes(ip, op):
    assert parse_minutes(ip) == op


def test_build_study_report():
    example = raw_sessions = {
    "Monday": "45",
    "Tuesday": "abc",
    "Wednesday": "60",
    "Thursday": "181",
    "Friday": "0",
    }

    assert build_study_report(example) =={
    "valid": {
        "Monday": 45,
        "Wednesday": 60,
        "Friday": 0,
    },
    "invalid_days": ["Tuesday", "Thursday"],
    "count": 3,
    "total": 105,
    "average": 35.0,
    "met_goal": 1,
    }   