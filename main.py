# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_student_heights=0
for heights in student_heights:
    sum_student_heights=heights+sum_student_heights
num_student=0
for i in student_heights:
  num_student+=1
avg= round(sum_student_heights/num_student)
print(avg)
