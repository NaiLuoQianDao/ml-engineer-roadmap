from ml_engineer_roadmap.experiment.month01.day16.score_importer import import_scores
import pytest

def test_import_scores_mixed_data():
    """1. 测试混合数据（部分合法，部分非法）"""
    records = {
        "Alice": "75",
        "Bob": "abc",
        "Charlie": "101",
        "David": " 0 ",  # 带有空格，你的 parse_score_strict 应该能处理
    }
    
    result = import_scores(records)
    
    # 断言：合法成绩进入 accepted
    assert result["accepted"] == {"Alice": 75, "David": 0}
    
    # 断言：非法成绩进入 rejected，并且【保持原始遍历顺序】 (Bob 在 Charlie 前面)
    assert result["rejected"] == ["Bob", "Charlie"]

def test_import_scores_all_valid():
    """2. 测试全部合法数据"""
    records = {
        "StudentA": "0",      # 边界值 0
        "StudentB": "100",    # 边界值 100
        "StudentC": "50",
    }
    
    result = import_scores(records)
    
    assert result["accepted"] == {"StudentA": 0, "StudentB": 100, "StudentC": 50}
    assert result["rejected"] == []

def test_import_scores_all_invalid():
    """3. 测试全部无效数据（触发 ValueError）"""
    records = {
        "Tom": "abc",       # 非数字
        "Jerry": "-5",      # 负数
        "Spike": "200",     # 超过 100
    }
    
    result = import_scores(records)
    
    assert result["accepted"] == {}
    # 顺序必须与字典插入顺序一致
    assert result["rejected"] == ["Tom", "Jerry", "Spike"]

def test_import_scores_empty_dict():
    """4. 测试传入空字典"""
    records = {}
    
    result = import_scores(records)
    
    # 必须完全等于这个特定的字典结构
    assert result == {"accepted": {}, "rejected": []}

def test_import_scores_does_not_modify_input():
    """5. 测试不修改原始输入字典"""
    records = {"Alice": "75", "Bob": "abc"}
    # 备份一份原始数据用于比对
    original_records = records.copy() 
    
    # 执行函数
    import_scores(records)
    
    # 断言：原始字典的内容和长度都没有被改变
    assert records == original_records
    assert len(records) == 2
    assert records["Alice"] == "75" # 确保原本的字符串 "75" 没有被替换成整数 75