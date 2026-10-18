from ml_engineer_roadmap.experiment.month01.day11.bug_hunt import (
    get_highest,
)


def test_positive_numbers():
    assert get_highest([10, 20, 30]) == 30


def test_mixed_numbers():
    assert get_highest([-10, 5, 15]) == 15

def test_special_case():
    assert get_highest([-10, -5, -15]) == -5