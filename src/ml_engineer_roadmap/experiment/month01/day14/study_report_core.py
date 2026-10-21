def parse_minutes(raw):
    try:
        int_raw = int(raw)
        if 0 <= int_raw <= 180:
            return int_raw
        else:
            return None
    except ValueError:
        return None

def build_study_report(raw_sessions):
    valid = dict()
    invalid_days = list()
    met_goal = 0
    average = None

    for key, value in raw_sessions.items():
        parsed_val = parse_minutes(value)
        if parsed_val is not None:
            if parsed_val >= 60:
                met_goal += 1
            valid[key] = parsed_val
        else:
            invalid_days.append(key)

    if valid:
        average = sum(valid.values())/len(valid)
    results = {
        'valid': valid,
        'invalid_days': invalid_days,
        'count': len(valid),
        'total': sum(valid.values()),
        'average': average,
        'met_goal': met_goal,
    }

    return results