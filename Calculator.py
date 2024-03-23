def calculate_grade():
    score=float(input("Enter the student's score:"))
    if score>=90 and score<=100:
        return 'A'
    elif score>=80 and score<=89:
        return 'B'
    elif score>=70 and score<=79:
        return 'C'
    elif score>=60 and score<=69:
        return 'D'
    else:
        return 'F'
grade = calculate_grade()
print(f"Student's grade:{grade}")
