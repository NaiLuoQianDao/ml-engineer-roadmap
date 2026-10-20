def classify_score(score):
    """Classify an integer score as Pass, Fail, or Invalid."""
    if type(score) is int:
        if 0 <= score <= 59:
            return 'Fail'
        elif 60 <= score <= 100:
            return 'Pass'
        else:
            return "Invalid"
    else:
        return 'Invalid'