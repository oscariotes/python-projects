students_heights = [180, 124, 165, 173, 169, 146, 156]

total = 0
count = 0
for element in students_heights:
    total += element
    count += 1
print(count)
print(total)
average_height = total/count
print(round(average_height))


# For loop get the maximum

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

print(f'The highest score is :', high_score)






    
  
    
    

    
    