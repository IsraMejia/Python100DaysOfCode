# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights, use space to separate the heights:  ").split()
for n in range(0, len(student_heights)): # 0 to start insert the heights in the list on 0
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)

n_heights = 0
sum_h = 0
for actual_height in student_heights:
    #print(sum_h)
    print(f' {sum_h}  It: {n_heights}') 
    #sum_h += sum_h #This variable is reassigned in every iteration xd
    sum_h = sum_h + actual_height
    n_heights += 1

print(f'\nThe sum of heights is = {sum_h}')
print(f'The number of heights is = {n_heights}')

avg_heights = int(sum_h / n_heights)

print(f'\nThe average of the students heights is: {avg_heights}')



