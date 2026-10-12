# Day 6 — Python Dictionaries & Sets

**Date:** 2026-10-12

## 1. What I Learned
Today I learned dictionaries and sets, and through exercises and small projects, I gradually mastered some of their usages.

## 2. Important Concepts
- Dictionary
- Key and Value
- keys(), values(), items()
- Set
- Union, Intersection, Difference

## 3. Exercises Completed
- exercise 1~4

## 4. Mini Project
Student Record System

## 5. Errors Encountered
- None

## 6. How I Solved Them
- None

## 7. What I Still Don't Understand
- None

## 8. Reflection
**1. Why use a Dictionary, not a List for all data?**
*   **Dictionary**: Stores data as **Key-Value pairs** (like `name: score`). It is very fast to find a student by name because it uses a "key". You don't need to look through everything.
*   **List**: Stores data in order. If you want to find a student in a List, you have to **loop** through the entire list one by one. It is slower and harder to use.
*   *Simple summary*: Dictionary is like a phone book (find by name). List is like a shopping list (read from top to bottom).

**2. What is the difference between `student["score"]` and `student.get("score")`?**
*   `student["score"]`: If the key "score" does not exist, Python will throw a **KeyError** and your program will **crash**.
*   `student.get("score")`: If the key "score" does not exist, Python will return **None** (or a default value you set, like `student.get("score", 0)`). The program will **not crash**.
*   *Simple summary*: `.get()` is safer. We use it to avoid the `KeyError` you asked about earlier.

**3. Why does a Set remove duplicates? Does it keep order?**
*   **Why**: A Set uses a **Hash Table**. When you add an item, Python calculates a special "hash" number for it. If the hash number is already there, Python knows it is a duplicate and ignores it.
*   **Order**: **No, it does not keep order.** Because it is based on hash numbers, the items are stored in a random-looking order. If you care about the original order, do not use a Set.

## 9. Next Step
Day 7 — Weekly Review