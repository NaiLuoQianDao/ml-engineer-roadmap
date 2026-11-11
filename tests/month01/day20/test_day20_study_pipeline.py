import pytest
import json
from src.ml_engineer_roadmap.experiment.month01.day20.study_pipeline import (
    load_study_csv,
    run_study_pipeline,
)

# --- 辅助函数：快速写入 CSV 内容 ---
def write_csv(path, content):
    path.write_text(content, encoding="utf-8")

# 1. 正常读取两条 CSV 记录
def test_load_study_csv_success(tmp_path):
    csv_file = tmp_path / "valid.csv"
    write_csv(csv_file, "name,minutes\nAlice,45\nBob,30\n")
    
    result = load_study_csv(csv_file)
    assert len(result) == 2
    assert result[0] == {"name": "Alice", "minutes": 45}
    assert result[1] == {"name": "Bob", "minutes": 30}

# 2. 直接测试分钟数边界 0 和 180 (假设 parse_minutes 支持 0-180 的合法范围)
@pytest.mark.parametrize("minutes_val", ["0", "180"])
def test_load_study_csv_minutes_boundary(tmp_path, minutes_val):
    csv_file = tmp_path / "boundary.csv"
    write_csv(csv_file, f"name,minutes\nAlice,{minutes_val}\n")
    
    result = load_study_csv(csv_file)
    assert result[0]["minutes"] == int(minutes_val)

# 3. 数据行缺少分钟数时抛出 ValueError
def test_load_study_csv_missing_minutes(tmp_path):
    csv_file = tmp_path / "missing.csv"
    write_csv(csv_file, "name,minutes\nAlice,\n")
    
    with pytest.raises(ValueError, match="missing minutes"):
        load_study_csv(csv_file)

# 4. 数据行多出字段时抛出 ValueError
def test_load_study_csv_extra_fields(tmp_path):
    csv_file = tmp_path / "extra.csv"
    write_csv(csv_file, "name,minutes\nAlice,45,extra_data\n")
    
    with pytest.raises(ValueError, match="extra data"):
        load_study_csv(csv_file)

# 5. 姓名为空时抛出 ValueError
def test_load_study_csv_empty_name(tmp_path):
    csv_file = tmp_path / "empty_name.csv"
    write_csv(csv_file, "name,minutes\n ,45\n") # 注意这里有个空格
    
    with pytest.raises(ValueError):
        load_study_csv(csv_file)

# 6. 只有正确表头时返回空列表
def test_load_study_csv_only_header(tmp_path):
    csv_file = tmp_path / "header_only.csv"
    write_csv(csv_file, "name,minutes\n")
    
    result = load_study_csv(csv_file)
    assert result == []

# 7. 集成函数写出正确的 JSON 报告
def test_run_study_pipeline_success(tmp_path):
    csv_file = tmp_path / "valid.csv"
    json_file = tmp_path / "report.json"
    write_csv(csv_file, "name,minutes\nAlice,40\nBob,60\n")
    
    report = run_study_pipeline(csv_file, json_file)
    
    # 验证返回的字典
    assert report["count"] == 2
    assert report["total_minutes"] == 100
    assert report["average_minutes"] == 50.0
    
    # 验证 JSON 文件内容
    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["count"] == 2
