def check_score(score):
    if not isinstance(score, (int, float)):
        return "invalid input"

    if score < 0 or score > 100:
        return "Invalid Score (Must be 0-100)"

    if score >= 70:
        return "distinction"
    elif score >= 50:
        return "credit"
    elif score >= 40:
        return "pass"
    else:
        return "fail"

user_input = input("Enter a score: ")
try:
    student_score = float(user_input)
    result = check_score(student_score)
    print(result)
except ValueError:
    print("invalid input: Please enter a valid number.")