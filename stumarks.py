import sys

if len(sys.argv) == 6:
    script_name = sys.argv[0]
    marks = [float(m) for m in sys.argv[1:6]]
    print("User provided marks values:")
else:
    script_name = sys.argv[0]
    # Default marks if not provided
    marks = [80, 75, 90, 85, 70]
    print("No input given - using default marks:")

average = sum(marks) / 5


if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

# Display results
print("\n--- Result ---")
print("Script Name:", script_name)
print("Marks:", marks)
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
