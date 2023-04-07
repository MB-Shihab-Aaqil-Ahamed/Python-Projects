# create an empty 2D list to store the marks
marks = []

# read the marks from the keyboard for each student
for i in range(4):
    
    subject1, subject2, subject3 = map(int, input().split())
    marks.append([subject1, subject2, subject3])

# calculate and display the total and average marks for each student
for i in range(4):
    
    total_marks = sum(marks[i])
    average_mark = round(total_marks / 3, 1)
    print("Total:", total_marks, "Average:", average_mark)




    