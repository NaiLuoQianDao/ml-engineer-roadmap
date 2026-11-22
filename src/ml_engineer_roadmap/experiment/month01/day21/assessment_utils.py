def copy_recent_records(
    records: list[dict[str, str]],
    n: int,
) -> list[dict[str, str]]:
    """Return copies of the last n records."""
    copy_records = []
    if type(n) is not int:
        raise TypeError
    if n == 0:
        return copy_records
    elif n < 0:
        raise ValueError
    
    for record in records[-1, -n]:
        copy_records.append(record)

    return copy_records