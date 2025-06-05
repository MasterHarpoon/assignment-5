# TASK 1

studentMarks = {"John":89, "Carl":91, "Max":78, "Jacob": 90}

inptName = str(input("Enter the student's name: "))
if inptName in studentMarks:
    print(inptName + "'s marks: " + str(studentMarks[inptName]))
else:
    print("Student not found")
    


