def parse_score(raw_value):
    try:
        true_value = int(raw_value)
        if not 0 <= true_value <= 100:
            return None
    except:
        return None

assert parse_score('60') == 60
assert parse_score('0') == 0
assert parse_score('100') == 100
assert parse_score('101') == None
assert parse_score('-1') == None
assert parse_score('abc') == None
assert parse_score('') == None
assert parse_score('60.5') == None