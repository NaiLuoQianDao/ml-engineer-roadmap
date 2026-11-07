import pytest

from ml_engineer_roadmap.experiment.month01.day17.label_validation import (
    validate_labels,
)


@pytest.mark.parametrize(
    "labels",
    [
        ["cat", "dog"],
        ["dog"],
        [],
    ],
)
def test_valid_labels(labels):
    assert validate_labels(labels) is None


@pytest.mark.parametrize(
    "labels",
    [
        ["bird"],
        ["Cat"],
        ["cat", "DOG"],
    ],
)
def test_invalid_label_values(labels):
    with pytest.raises(ValueError):
        validate_labels(labels)


@pytest.mark.parametrize(
    "labels",
    [
        "cat",
        None,
        ("cat", "dog"),
    ],
)
def test_invalid_container_types(labels):
    with pytest.raises(TypeError):
        validate_labels(labels)


@pytest.mark.parametrize(
    "labels",
    [
        [123],
        ["cat", None],
    ],
)
def test_invalid_element_types(labels):
    with pytest.raises(TypeError):
        validate_labels(labels)