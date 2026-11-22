import pytest
import json
from ml_engineer_roadmap.experiment.month01.day21.prediction_audit import (
    load_prediction_csv,
    build_prediction_audit,
)
from ml_engineer_roadmap.experiment.month01.day17.prediction_evaluator import (
    evaluate_predictions,
)

# 辅助函数：快速写入 CSV
def write_csv(path, content):
    path.write_text(content, encoding="utf-8")


# ==========================================
# 1. 测试 load_prediction_csv (正常读取)
# ==========================================
def test_load_prediction_csv_success(tmp_path):
    csv_file = tmp_path / "valid.csv"
    write_csv(csv_file, "sample_id,actual,predicted\nS1, cat , dog \nS2,dog,dog\n")
    
    result = load_prediction_csv(csv_file)
    assert len(result) == 2
    # 验证空格是否被去掉
    assert result[0] == {"sample_id": "S1", "actual": "cat", "predicted": "dog"}


# ==========================================
# 2. 测试 load_prediction_csv (空输入 / 只有表头)
# ==========================================
def test_load_prediction_csv_header_only(tmp_path):
    csv_file = tmp_path / "header_only.csv"
    write_csv(csv_file, "sample_id,actual,predicted\n")
    
    result = load_prediction_csv(csv_file)
    assert result == []


# ==========================================
# 3. 测试 load_prediction_csv (非法数据：表头错误)
# ==========================================
def test_load_prediction_csv_wrong_header(tmp_path):
    csv_file = tmp_path / "wrong_header.csv"
    write_csv(csv_file, "id,actual,predicted\nS1,cat,dog\n")
    
    with pytest.raises(ValueError, match="Invalid headers"):
        load_prediction_csv(csv_file)


# ==========================================
# 4. 测试 load_prediction_csv (CSV字段损坏：缺列/多列)
# ==========================================
@pytest.mark.parametrize("content", [
    "sample_id,actual,predicted\nS1,cat\n",        # 缺字段
    "sample_id,actual,predicted\nS1,cat,dog,extra\n" # 多字段
])
def test_load_prediction_csv_broken_fields(tmp_path, content):
    csv_file = tmp_path / "broken.csv"
    write_csv(csv_file, content)
    
    with pytest.raises(ValueError, match="Invalid row length"):
        load_prediction_csv(csv_file)


# ==========================================
# 5. 测试 load_prediction_csv (非法标签)
# ==========================================
def test_load_prediction_csv_invalid_label(tmp_path):
    csv_file = tmp_path / "invalid_label.csv"
    write_csv(csv_file, "sample_id,actual,predicted\nS1,Cat,dog\n") # 大写 Cat 非法
    
    with pytest.raises(ValueError, match="Invalid label"):
        load_prediction_csv(csv_file)


# ==========================================
# 6. 测试 evaluate_predictions (评估准确率 & 复制后原数据不变)
# ==========================================
def test_evaluate_predictions_and_no_side_effect():
    actual = ["cat", "dog", "dog"]
    predicted = ["cat", "cat", "dog"]
    actual_copy = actual.copy()
    predicted_copy = predicted.copy()
    
    result = evaluate_predictions(actual, predicted)
    
    assert result["accuracy"] == 2/3
    assert result["wrong_indices"] == [1]
    # 验证原数据未被修改
    assert actual == actual_copy
    assert predicted == predicted_copy


# ==========================================
# 7. 测试 build_prediction_audit (空数据时 accuracy 为 None)
# ==========================================
def test_build_prediction_audit_empty_accuracy(tmp_path):
    csv_file = tmp_path / "empty.csv"
    json_file = tmp_path / "report.json"
    write_csv(csv_file, "sample_id,actual,predicted\n")
    
    report = build_prediction_audit(csv_file, json_file)
    assert report["total"] == 0
    assert report["accuracy"] is None

    # 验证写入 JSON 中的是 null (None)
    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["accuracy"] is None


# ==========================================
# 8. 测试 build_prediction_audit (JSON 保存成功)
# ==========================================
def test_build_prediction_audit_success(tmp_path):
    csv_file = tmp_path / "valid.csv"
    json_file = tmp_path / "report.json"
    write_csv(csv_file, "sample_id,actual,predicted\nS1,cat,cat\nS2,dog,cat\nS3,dog,dog\n")
    
    report = build_prediction_audit(csv_file, json_file)
    
    assert report["total"] == 3
    assert report["correct"] == 2
    assert report["incorrect"] == 1
    assert report["accuracy"] == pytest.approx(2/3)
    
    # 验证 JSON 文件确实存在且内容正确
    assert json_file.exists()
    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["records"][0]["sample_id"] == "S1"
        assert len(data["records"]) == 3


# ==========================================
# 9. 测试 build_prediction_audit (输入无效时不覆盖旧报告)
# ==========================================
def test_build_prediction_audit_does_not_overwrite(tmp_path):
    csv_file = tmp_path / "invalid.csv"
    json_file = tmp_path / "existing_report.json"
    
    # 预先写一个合法的旧 JSON
    with json_file.open("w", encoding="utf-8") as f:
        json.dump({"status": "old data"}, f)
        
    # 创建一个非法的 CSV
    write_csv(csv_file, "sample_id,actual,predicted\nS1,bird,dog\n") 
    
    # 预期抛出 ValueError
    with pytest.raises(ValueError):
        build_prediction_audit(csv_file, json_file)
        
    # 验证旧数据未被覆盖
    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        assert data == {"status": "old data"}