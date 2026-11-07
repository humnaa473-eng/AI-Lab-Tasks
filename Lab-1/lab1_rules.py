
def check_eligibility(score, documents_complete, attendance, interview_score):

    if (score >= 70 and documents_complete
            and attendance >= 75 and interview_score >= 50):
        return "Eligible"
    else:
        return "Not Eligible"


test_cases = [
    {
        "name": "Case 1 - Normal Pass",
        "score": 85,
        "documents": True,
        "attendance": 90,
        "interview": 80,
        "expected": "Eligible"
    },
    {
        "name": "Case 2 - Attendance Failure",
        "score": 80,
        "documents": True,
        "attendance": 70,
        "interview": 75,
        "expected": "Not Eligible"
    },
    {
        "name": "Case 3 - Interview Failure",
        "score": 80,
        "documents": True,
        "attendance": 85,
        "interview": 40,
        "expected": "Not Eligible"
    },
    {
        "name": "Case 4 - Threshold Boundary",
        "score": 70,
        "documents": True,
        "attendance": 75,
        "interview": 50,
        "expected": "Eligible"
    }
]

for case in test_cases:
    actual = check_eligibility(
        case["score"],
        case["documents"],
        case["attendance"],
        case["interview"]
    )

    print("\n", case["name"])
    print("Input:", case["score"], case["documents"],
          case["attendance"], case["interview"])
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)

    if actual == "Eligible":
        reason = "All four conditions are satisfied."
    elif case["attendance"] < 75:
        reason = "Attendance is below 75%."
    elif case["interview"] < 50:
        reason = "Interview score is below 50."
    else:
        reason = "Score or document condition is not satisfied."

    print("Reason:", reason)
