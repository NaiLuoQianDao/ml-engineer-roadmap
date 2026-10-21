from ml_engineer_roadmap.experiment.month01.day14.study_report_core import build_study_report


def main():
    raw_sessions = {
    "Monday": "45",
    "Tuesday": "abc",
    "Wednesday": "60",
    "Thursday": "181",
    "Friday": "0",
    }
    op_inform = build_study_report(raw_sessions)
    print(op_inform)
    return op_inform

if __name__ == '__main__':
    main()