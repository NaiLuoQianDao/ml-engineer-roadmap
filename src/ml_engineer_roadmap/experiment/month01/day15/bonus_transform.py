def add_bonus(scores, bonus):
    """Return a new list of adjusted scores capped at 100."""
    copy_scores = scores.copy()
    if scores:
        for i in range(len(scores)):
            if scores[i] + bonus <= 100:
                copy_scores[i] += bonus
            else:
                copy_scores[i] = 100 

    return copy_scores