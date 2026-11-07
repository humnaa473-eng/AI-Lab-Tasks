
# Task 3: Conversational Test vs Rule-Based System

def check_eligibility(score, documents_complete, attendance, interview_score):

    if (score >= 70 and documents_complete
            and attendance >= 75 and interview_score >= 50):
        return "Eligible"
    else:
        return "Not Eligible"


# Scholarship case
score = 68
documents_complete = True
attendance = 90
interview_score = 80

# Example conversational AI response
conversational_result = "Eligible"

# Rule-based system result
actual_result = check_eligibility(
    score, documents_complete, attendance, interview_score
)

print("SCHOLARSHIP CASE")
print("Score:", score)
print("Documents Complete:", documents_complete)
print("Attendance:", attendance)
print("Interview Score:", interview_score)

print("\nConversational AI Result:", conversational_result)
print("Rule-Based System Result:", actual_result)

if conversational_result != actual_result:
    print("Result: Disagreement")
    print("Reason: Score is below 70.")
else:
    print("Result: Agreement")
