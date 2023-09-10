# Function to calculate the average of three subjects
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to determine pass or fail
def determine_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"

# Input marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Create a list of marks
marks = [subject1, subject2, subject3]

# Calculate the average
average = calculate_average(marks)

# Determine the result
result = determine_result(average)

# Display the result
print(f"Average marks: {average}")
print(f"Result: {result}")
