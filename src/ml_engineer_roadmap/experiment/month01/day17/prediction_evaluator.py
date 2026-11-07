from ml_engineer_roadmap.experiment.month01.day17.label_validation import validate_labels

def evaluate_predictions(
    actual: list[str],
    predicted: list[str],
) -> dict[str, object]:
    """Evaluate predictions and return a summary."""
    out_dict = {
        'total': 0,
        'correct': 0,
        'incorrect': 0,
        'accuracy': None,
        'wrong_indices': [],
    }
    if len(actual) != len(predicted):
        raise ValueError
    validate_labels(actual)
    validate_labels(predicted)
    if actual:
        out_dict['total'] = len(actual)    
        compared_group = zip(actual, predicted)
        for index, value in enumerate(compared_group):
            if value[0] == value[1]:
                out_dict['correct'] += 1
            else:
                out_dict['incorrect'] += 1
                out_dict['wrong_indices'].append(index)
        out_dict['accuracy'] = out_dict['correct'] / out_dict['total']

    return out_dict