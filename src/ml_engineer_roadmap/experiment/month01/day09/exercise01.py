def is_passing(score):
    return score >= 60  

assert is_passing(20) == False
assert is_passing(80) == True
assert is_passing(59) == False
assert is_passing(60) == True
assert is_passing(0) == False
assert is_passing(100) == True