def parse_minutes(raw):
    try:
        int_raw = int(raw)
        if 0 <= int_raw <= 180:
            return int_raw
        else:
            return None
    except ValueError:
        return None

def take_last_n(items, n):
    if items and n: 
        if n <= len(items):   
            return items[-n:]
        else: 
            return items
    else:
        return []