def count_passing(scores):
    count =0
    for score in scores:
        if score >= 60:
            count += 1
    return count

def calculate_pass_rate(scores):
    if scores:
        count = count_passing(scores)
        return (count / len(scores)) * 100
    else:
        return None

def main(scores):
    number_pass = count_passing(scores)
    pass_rate = calculate_pass_rate(scores)
    print(number_pass, pass_rate)
    return number_pass,pass_rate

assert main([60,70,80,90]) == (4,100.0)
assert main([12,42,35,49]) == (0,0.0)
assert main([44,55,80,90]) == (2,50.0)
assert main([]) == (0,None)
assert main([60]) == (1,100.0)
assert main([59,60,61]) == (2,2/3*100)
assert main([60,60,60,60]) == (4,100.0)
assert main([0,100]) == (1,50.0)