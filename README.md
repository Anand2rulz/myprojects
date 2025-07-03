# myprojectsdef calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

students = []

n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks for 3 subjects: ").split()))
    total = sum(marks)
    avg = total / 3
    grade = calculate_grade(avg)
    students.append((name, marks, total, avg, grade))

print("\nStudent Report:")
for s in students:
    print(f"Name: {s[0]}, Marks: {s[1]}, Total: {s[2]}, Avg: {s[3]:.2f}, Grade: {s[4]}")
