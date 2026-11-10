from pathlib import Path
import csv
import json

from ml_engineer_roadmap.experiment.month01.day14.challenges import parse_minutes


def load_study_csv(
    path: str | Path,
) -> list[dict[str, str | int]]:
    """Read and validate study records from CSV."""

    path = Path(path)
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        result = []
        if reader.fieldnames != ['name', 'minutes']:
            raise ValueError
        for row in reader:
            name = row['name'].strip()
            if name:
                row['name'] = name
            else:
                raise ValueError
            minutes = parse_minutes(row['minutes'])
            if minutes is not None:
                row['minutes'] = minutes
            else:
                raise ValueError
            result.append(row)
        return result

def save_study_json(
    path: str | Path,
    records: list[dict[str, str | int]],
) -> None:
    """Save validated study records as JSON."""
    path = Path(path)
    with path.open('w', encoding='utf-8') as file:
        json.dump(
            records,
            file,
            ensure_ascii=False,
            indent=2,
        )

    return None