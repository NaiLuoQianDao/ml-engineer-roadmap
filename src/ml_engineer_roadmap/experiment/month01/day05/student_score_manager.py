scores = []

while True:
    # 1. 接收输入
    enter_score = input('Enter score (or done): ')
    
    # 2. 判断是否退出
    if enter_score == 'done':
        break
        
    # 3. 尝试转换为数字并验证范围
    score = float(enter_score) # 用 float 可以兼容小数，如果你想只要整数可用 int
    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("分数必须在 0 到 100 之间！")


# 4. 输出结果（增加防止空列表报错的判断）
if len(scores) > 0:
    print('Total Students:', len(scores))
    print('Average:', sum(scores) / len(scores))
    print('MAX:', max(scores), 'MIN:', min(scores))
    print('Scores:', scores)
else:
    print("没有输入任何分数。")