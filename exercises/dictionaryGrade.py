student_scores = {
    'Harry': 81,
    'Ron'  : 79,
    'Hermione' : 99,
    'Draco' : 74,
    'Neville' : 62,
}

student_grades = {}



for key, value in student_scores.items():
    if value >= 91:
        student_grades[key] = 'Outstanding'
    elif value >= 81:
        student_grades[key] = 'Exceeds Expectations'
    elif value >= 71:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

print(student_grades)

student_Grades ={}
       
for student in student_scores:
    score = student_scores[student]
    if score >=91:
        student_Grades[student] = 'Outstanding'
    elif score >=81:
        student_Grades[student] = 'Exceeds Expectations'
    
    
print(student_Grades)
