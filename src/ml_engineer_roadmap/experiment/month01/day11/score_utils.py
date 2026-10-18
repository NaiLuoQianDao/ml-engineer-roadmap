def is_valid_score(score):
    if 0 <= score <= 100:
        return True
    else:
        return False 

def count_passing(scores):
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    return count