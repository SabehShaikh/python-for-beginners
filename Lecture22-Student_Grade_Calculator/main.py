# Student grade calculator:

print("Welcome to the Grade calculator")

print("Enter 5 subject marks: prog. calculates avg and grade")


# create empty list for marks:
marks = []

# loop to take input for 5 subjects:
for i in range(1,6):

    number = float(input(f"Enter the mark for subject {i} : "))

# ensure marks are between 0 and 100:
    if 0 <= number <= 100: # if number >=0 and number <= 100
        marks.append(number)

    else:
        print("Marks must be between 0 and 100")    

# calculate the average:
avg = sum(marks) / len(marks)

# calculate the grade:

# Check if avg is greater than or equal to 90 
# and less than or equal to 100.

# Chained comparison:  
if 90<=avg<=100:  # if avg >= 90 and avg <= 100:
    grade = "A"
elif 80<=avg<90:
    grade = "B"
elif 70<=avg<80:
    grade = "C"
elif 60<=avg<70:
    grade = "D"
else:
    grade = "F"

# display the results:
print(f"Marks: {marks}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")    