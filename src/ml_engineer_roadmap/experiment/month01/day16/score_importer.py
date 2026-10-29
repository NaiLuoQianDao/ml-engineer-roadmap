from ml_engineer_roadmap.experiment.month01.day16.score_validation import parse_score_strict

def import_scores(records):
    """Import valid scores and collect rejected student names."""
    return_dictionary = {
        "accepted": {
    },
        "rejected": [],
    }
    for key, value in records.items():
        try:
            out_grade = parse_score_strict(value)
            return_dictionary['accepted'][key] = out_grade
        except:
            return_dictionary['rejected'].append(key)

    return return_dictionary