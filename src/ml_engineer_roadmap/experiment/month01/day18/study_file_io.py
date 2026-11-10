from pathlib import Path
from ml_engineer_roadmap.experiment.month01.day14.challenges import parse_minutes

def load_study_minutes(path: str | Path) -> list[int]:
    """Read study minutes from a text file."""
    list_of_studyminutes = []
    path = Path(path)
    content = path.read_text(encoding='utf-8')
    date_of_studyminutes = content.splitlines()
    for date_index, date in enumerate(date_of_studyminutes):
        if date.strip():
            result = parse_minutes(date)
            if result is not None:
                list_of_studyminutes.append(result)
            else:
                raise ValueError(f"Invalid data at line {date_index + 1}")

    return list_of_studyminutes

def write_study_summary(
    path: str | Path,
    minutes: list[int],
) -> None:
    """Write a study summary to a text file."""
    write_date = []
    count, total, average = 0, 0, None
    path = Path(path)
    for minute in minutes:
        count += 1
        total += minute
    if count != 0:
        average = total / count
        write_date = [
            f'count={count}\n',
            f'total={total}\n',
            f'average={average}\n',
        ]
        write_date = ''.join(write_date)
        path.write_text(write_date, encoding='utf-8')
    else:
        path.write_text(
            'count=0\n'
            'total=0\n'
            'average=N/A\n', encoding='utf-8'
        )

    return None