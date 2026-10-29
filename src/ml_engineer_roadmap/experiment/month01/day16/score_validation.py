def parse_score_strict(raw):
    """Convert a score string to an integer or raise an error."""
    if type(raw) != str:
        raise TypeError
    try:
        age = int(raw)
        if 0 <= age <= 100:
            return age
        else:
            raise ValueError
    except ValueError:
        raise ValueError