def get_highest(scores):
    highest = min(scores)

    for score in scores:
        if score > highest:
            highest = score

    return highest