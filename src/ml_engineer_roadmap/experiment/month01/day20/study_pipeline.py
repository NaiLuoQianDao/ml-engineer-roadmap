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
        for row_index, row in enumerate(reader):
            if None not in row:    
                name = row['name'].strip()
                if name:
                    row['name'] = name
                else:
                    raise ValueError
                if row['minutes'] is not None and row['minutes'].strip() != '':
                    minutes = parse_minutes(row['minutes'])
                else:
                    raise ValueError(f'Invalid CSV row at line {row_index + 2}: missing minutes')
                if minutes is not None:
                    row['minutes'] = minutes
                else:
                    raise ValueError
                result.append(row)
            else:
                raise ValueError('extra data!!')    
        return result


def run_study_pipeline(
    csv_path: str | Path,
    json_path: str | Path,
) -> dict[str, object]:
    """Read, validate, summarize and save study records."""
    csv_path = Path(csv_path)
    json_path = Path(json_path)
    count = 0
    total_minutes = 0
    average_minutes = None

    study_list = load_study_csv(csv_path)
    count = len(study_list)
    for person in study_list:
        total_minutes += person['minutes']
    if count != 0:
        average_minutes = total_minutes / count
    report_dict = {
        'count' : count,
        'total_minutes' : total_minutes,
        'average_minutes' : average_minutes,
        'records' : study_list
    }
    with json_path.open('w', encoding='utf-8') as file:
        json.dump(
            report_dict,
            file,
            ensure_ascii=False,
            indent=2,
        )

    return report_dict


