def validate_labels(labels: list[str]) -> None:
    """Validate a list of binary classification labels."""
    # 1. 检查输入本身是否为列表
    if not isinstance(labels, list):
        raise TypeError("输入必须是一个列表 (list)")

    # 2. 遍历列表中的每一个元素
    for label in labels:
        # 检查元素是否为字符串
        if not isinstance(label, str):
            raise TypeError(f"标签 '{label}' 必须是字符串 (str)")
        
        # 检查字符串的值是否严格等于 'cat' 或 'dog'（大小写敏感）
        if label not in ("cat", "dog"):
            raise ValueError(f"非法的标签: '{label}'。只允许 'cat' 或 'dog'")
            
    return None