# Week 01 — Python Foundations Assessment

**Learning Path:** 24-Month ML Engineer Roadmap
**Phase:** Month 01 — Python Foundations
**Assessment:** Week 01, Day 07
**Status:** Submitted — Review in Progress
**Git Commit:** `3fb02c6`

---

## Assessment Overview

This assessment reviews the Python fundamentals learned during Days 1–6.

| Part      | Assessment                 | Maximum Score |
| --------- | -------------------------- | ------------: |
| Part 1    | Python Theory              |            20 |
| Part 2    | Coding Challenges          |            40 |
| Part 3    | Student Performance Report |            30 |
| Part 4    | Weekly Reflection          |            10 |
| **Total** |                            |       **100** |

---

# Part 1 — Python Theory (20 Points)

**Instructions:** Each question is worth 2 points. The answers below are my original submitted responses.

## Q1. Print vs Return

What is the difference between the following functions?

```python
def add(a, b):
    print(a + b)

def add2(a, b):
    return a + b
```

**Options:**

- A. Both functions behave exactly the same.
- B. The first prints the result; the second returns it.
- C. The second function raises an error.

**My Answer:** B

## Q2. Boolean Logic

What is the value of `result`?

```python
x = 10
result = (x > 5) and (x < 8)
```

**Options:**

- A. True
- B. False
- C. None

**My Answer:** B

## Q3. If / Elif Execution

What will this code print?

```python
score = 95

if score >= 60:
    print("Pass")
elif score >= 90:
    print("Excellent")
```

**Options:**

- A. Pass
- B. Excellent
- C. Both Pass and Excellent

**My Answer:** A

## Q4. For Loop and Range

What will the final output be?

```python
total = 0

for i in range(1, 5):
    total += i

print(total)
```

**Options:**

- A. 10
- B. 15
- C. 6

**My Answer:** A

## Q5. List vs Tuple

Which operation will raise an error?

```python
a = [1, 2, 3]
b = (1, 2, 3)
```

**Options:**

- A. `a[0] = 10`
- B. `b[0] = 10`
- C. `print(b[0])`

**My Answer:** B

## Q6. List Slicing

What will this code print?

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
```

**Options:**

- A. `[10, 20, 30, 40]`
- B. `[20, 30, 40]`
- C. `[20, 30, 40, 50]`

**My Answer:** A

## Q7. Dictionary Access

Which method safely retrieves a potentially missing key?

```python
student = {"name": "Alice"}
```

**Options:**

- A. `student["score"]`
- B. `student.get("score")`
- C. `student.score`

**My Answer:** B

## Q8. Set and Duplicates

How many elements are in this set?

```python
numbers = {1, 2, 2, 3, 3, 3}
```

**Options:**

- A. 6
- B. 5
- C. 3

**My Answer:** C

## Q9. Continue Statement

What does the following code print?

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Options:**

- A. 1, 2
- B. 1, 2, 4, 5
- C. 1, 2, 3, 4, 5

**My Answer:** B

## Q10. Function Return

Which statement is correct?

```python
def check(n):
    if n > 0:
        return "Positive"
    return "Other"
```

**Options:**

- A. Both return statements always execute.
- B. If `n > 0`, the function returns `"Positive"`.
- C. The function has no parameters.

**My Answer:** B

### Part 1 — Answer Summary

| Question | My Answer | Correct Answer | Result    |
| -------- | --------- | -------------- | --------- |
| Q1       | B         | B              | Correct   |
| Q2       | B         | B              | Correct   |
| Q3       | A         | A              | Correct   |
| Q4       | A         | A              | Correct   |
| Q5       | B         | B              | Correct   |
| Q6       | A         | B              | Incorrect |
| Q7       | B         | B              | Correct   |
| Q8       | C         | C              | Correct   |
| Q9       | B         | B              | Correct   |
| Q10      | B         | B              | Correct   |

**Theory Score: 18 / 20**

**Topic to Review:** Python list slicing, particularly the exclusive ending index.

---

# Part 2 — Independent Coding Challenges (40 Points)

The coding solutions are saved under:

`src/ml_engineer_roadmap/experiment/month01/day07/`

| Challenge            | File             | Tested |
| -------------------- | ---------------- | ------ |
| 1 — Number Analyzer  | `challenge01.py` | Review |
| 2 — Unique Words     | `challenge02.py` | Review |
| 3 — Grade Statistics | `challenge03.py` | Review |
| 4 — Student Search   | `challenge04.py` | Review |

### Challenge 1 — Number Analyzer

Implement `analyze_numbers(numbers)` to return a dictionary containing the total count, number of even integers, number of odd integers, and sum.

Test cases include an empty list, repeated even numbers, negative numbers, and zero.

### Challenge 2 — Find Unique Words

Implement `unique_words(words)` to return the number of distinct words using a Set.

The comparison must be case-sensitive.

### Challenge 3 — Grade Statistics

Implement `grade_statistics(scores)` to calculate the average, highest score, lowest score, and number of passing students.

Handle empty input safely.

### Challenge 4 — Student Search

Implement `find_student(students, name)` to return the student's score or `"Student not found"`.

**Initial Review:** All four implementations meet the core requirements. Final runtime verification remains to be completed.

---

# Part 3 — Student Performance Report System (30 Points)

**Source File:** `student_performance_report.py`

## Required Features

- [x] Add student
- [x] View all students
- [x] Search student
- [x] Show class statistics
- [x] Show passing students
- [x] Exit program

## Engineering Requirements

- [x] Use multiple functions.
- [x] Handle an empty dictionary.
- [x] Handle duplicate student names with a clear policy.
- [x] Use loops, dictionaries, and conditions.
- [ ] Validate score range and non-numeric input.
- [ ] Improve highest/lowest score initialization.

## Initial Review

The menu structure and core calculations are implemented. Improvement is needed for input validation and robustness.

---

# Part 4 — Week 01 Learning Reflection (10 Points)

## 1. What were my three strongest learning areas?

**My Original Reflection:**

条件控制 if，循环 while、for，数据结构比如列表、字典、集合、字符串。能写包括学生成绩查询系统之类的简单交互程序。

## 2. Which three areas are currently my weakest?

**My Original Reflection:**

目前还没有。Git 常用命令比如 add、status、commit、push 明白了，但是其他没教我的功能都不知道。

## 3. What was the most difficult error during Week 01?

**My Original Reflection:**

暂时还没有，学得挺顺利的。

## 4. Can I build a program using functions, loops, and dictionaries independently?

**My Original Reflection:**

可以，目前掌握的知识还比较简单，学起来挺快的。

## 5. What do I want to improve during Week 02?

**My Original Reflection:**

听上去都不错，我觉得都可以。

---

# Part 5 — Instructor Review

**Review Type:** Initial static code review

## Strengths

- Correct usage of Python functions and return values.
- Good understanding of loops and conditional logic.
- Successfully applied Lists, Dictionaries, and Sets.
- Able to combine multiple concepts into a practical program.
- Git commits and repository organization show consistent progress.

## Improvement Areas

1. Review List slicing and index boundaries.
2. Strengthen program input validation.
3. Avoid using assumptions such as fixed sentinel values without enforcing valid input.
4. Make weekly reflections more specific and evidence-based.
5. Practice debugging and testing edge cases independently.

## Assessment Status

**Theory:** 18/20
**Coding Challenges:** 40/40 — provisional
**Integrated Project:** 27/30 — provisional
**Reflection:** 5/10 — provisional

**Overall Initial Assessment: Approximately 90/100**

Final score should be confirmed after runtime tests.

---

# Week 02 Preparation

## Topics to Reinforce

- List slicing
- Function design
- Input validation
- Edge cases
- Code readability
- Debugging skills

## Next Learning Phase

Continue the 24-month ML Engineer roadmap, using the Week 01 assessment as a baseline for future weekly evaluations.
