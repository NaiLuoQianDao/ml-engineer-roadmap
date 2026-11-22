from pathlib import Path
import csv
import json
from ml_engineer_roadmap.experiment.month01.day17.prediction_evaluator import evaluate_predictions

def load_prediction_csv(path: str | Path) -> list[dict[str, str]]:
    path = Path(path)
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ['sample_id', 'actual', 'predicted']:
            raise ValueError("Invalid headers")
        
        result = []
        valid_labels = {"cat", "dog"}
        for row in reader:
            if None in row or None in row.values():
                raise ValueError("Invalid row length")
            
            sample_id = row['sample_id'].strip()
            actual = row['actual'].strip()
            predicted = row['predicted'].strip()
            
            if not sample_id:
                raise ValueError("Empty sample_id")
            if actual not in valid_labels or predicted not in valid_labels:
                raise ValueError("Invalid labels")
                
            result.append({
                "sample_id": sample_id,
                "actual": actual,
                "predicted": predicted
            })
        return result

def build_prediction_audit(csv_path: str | Path, json_path: str | Path) -> dict[str, object]:
    records = load_prediction_csv(csv_path)
    actuals = [r["actual"] for r in records]
    predicteds = [r["predicted"] for r in records]
    
    eval_result = evaluate_predictions(actuals, predicteds)
    
    report = {
        "total": eval_result["total"],
        "correct": eval_result["correct"],
        "incorrect": eval_result["incorrect"],
        "accuracy": eval_result["accuracy"],
        "wrong_indices": eval_result["wrong_indices"],
        "records": records
    }
    
    json_path = Path(json_path)
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        
    return report