from ml_engineer_roadmap.experiment.month01.day13.student_report_core import (
    calculate_statistics,
    get_passing_students,
)


def main():
    students = {
        "Alice": 90,
        "Bob": 59,
        "Charlie": 60,
    }

    statistics = calculate_statistics(students)
    passing_students = get_passing_students(students)

    print("=== Student Performance Report V3 ===")
    print("Statistics:", statistics)
    print("Passing students:", passing_students)


if __name__ == "__main__":
    main()