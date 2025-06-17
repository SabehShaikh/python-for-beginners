# develop a program that manages student records by  calculating grades 
# for multiple subjects and determining overall 
#  performance based on the average score

# requirements:
# the program should ask for the number of students
# for each student, input the following information
# Name
# Roll number
# marks in 6 subects (math , science , english, history , 
# computer and physics)

# calculate avg and total marks and avg should be rounded to two decimals:

# A+ 95-100
# A 85 - 94
# B 75 - 84
# C 65 - 74
# D 50 - 64
# F below 50

# generate performance report :
# display the following:
# roll no
# name
# total marks
# avg score
# letter grade

print("Student Performance Report System")

# Ask for number of students
num_students = int(input("Enter the number of students: "))

# List of subjects
subjects = ["Math", "Science", "English", "History", "Computer", "Physics"]

# Loop over each student
for i in range(num_students):
    print(f"\n Enter details for Student {i + 1}")
    
    # Input: Name and Roll number
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    # Input: Marks for 6 subjects
    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("❌ Marks must be between 0 and 100.")
            except ValueError:
                print("❌ Please enter a valid number.")

    # Calculate total and average
    total = sum(marks)
    avg = round(total / len(subjects), 2)

    # Determine grade based on average
    if 95 <= avg <= 100:
        grade = "A+"
    elif 85 <= avg < 95:
        grade = "A"
    elif 75 <= avg < 85:
        grade = "B"
    elif 65 <= avg < 75:
        grade = "C"
    elif 50 <= avg < 65:
        grade = "D"
    else:
        grade = "F"

    # Print performance report
    print("\nPerformance Report:")
    print(f"Roll No     : {roll}")
    print(f"Name        : {name}")
    print(f"Total Marks : {total}")
    print(f"Average     : {avg:.2f}")
    print(f"Grade       : {grade}")

