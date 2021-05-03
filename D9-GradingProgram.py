student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
print('\n\t Grading Program\n')
#TODO-1: Create an empty dictionary called sudent_grades.
sudent_grades = {}

#TODO-2: Write your code below to add the grades to sudent_grades.👇
for student in student_scores:
    score = student_scores[student]  #We use the Key student
    if score > 90:
        sudent_grades[student] = 'Outstanding'
    elif score >80:
        sudent_grades[student] = 'Exceeds Expectations'
    elif score >70:
        sudent_grades[student] = 'Acceptable'
    else:
        sudent_grades[student] = 'Fail'
    

# 🚨 Don't change the code below 👇
print(f'Student grades:\n{sudent_grades}')

