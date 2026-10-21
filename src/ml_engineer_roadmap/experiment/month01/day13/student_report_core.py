def calculate_statistics(students):
    """Calculate class statistics from a student-score dictionary."""

    students_inform = dict()
    passing_number = 0
    for key, value in students.items():
        students_inform[key] = value
        if value >= 60:
            passing_number += 1
    if students_inform:        
        out_inform = {
            'count' : len(students_inform),
            'highest' : max(students_inform.values()),
            'lowest' : min(students_inform.values()),
            'average' : sum(students_inform.values())/len(students_inform),
            'passing_count' : passing_number,
        }
        return out_inform
    else:
        return None    

def get_passing_students(students):
    """Return a new dictionary containing passing students."""

    passing_students = dict()
    for key, value in students.items():
        if value >= 60:
            passing_students[key] = value
    return passing_students