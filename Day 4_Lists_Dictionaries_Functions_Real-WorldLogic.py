"""
Day 4 — Lists, Dictionaries, Functions & Real-World Logic
"""


# =====================================================
# 1. STUDENT MARKS ANALYZER
# =====================================================

def analyze_marks(students):
    highest_marks = max(students.values())

    top_scorers = []
    for name, marks in students.items():
        if marks == highest_marks:
            top_scorers.append(name)

    average_marks = sum(students.values()) / len(students)

    above_80 = []
    for name, marks in students.items():
        if marks > 80:
            above_80.append(name)

    passed_count = 0
    for marks in students.values():
        if marks >= 40:
            passed_count += 1

    print("Highest Scorer:", ", ".join(top_scorers))
    print("Highest Marks:", highest_marks)
    print("Average Marks:", average_marks)
    print("Students Above 80:", ", ".join(above_80))
    print("Number of Students Passed:", passed_count)


students = {
    "Ravi": 85,
    "Anil": 72,
    "Kiran": 91,
    "Suresh": 68,
    "Priya": 91
}

analyze_marks(students)


# =====================================================
# 2. MUTABLE DEFAULT ARGUMENT — FIXED
# =====================================================

def add_student(name, students=None):
    if students is None:
        students = []

    students.append(name)
    return students


print("\nMutable Default Argument Fix:")
print(add_student("Ravi"))
print(add_student("Anil"))
print(add_student("Kiran"))


# =====================================================
# 3. REMOVE DUPLICATES USING SET
# =====================================================

def remove_duplicates_with_set(numbers):
    seen = set()
    result = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


numbers1 = [10, 20, 10, 30, 20, 40, 30]

print("\nRemove Duplicates Using Set:")
print(remove_duplicates_with_set(numbers1))


# =====================================================
# 4. REMOVE DUPLICATES WITHOUT SET
# =====================================================

def remove_duplicates_without_set(numbers):
    result = []

    for number in numbers:
        if number not in result:
            result.append(number)

    return result


numbers2 = [3, 1, 3, 2, 1, 5]

print("\nRemove Duplicates Without Set:")
print(remove_duplicates_without_set(numbers2))


# =====================================================
# 5. APPEND VS EXTEND
# =====================================================

print("\nappend() vs extend():")

numbers = [1, 2]
numbers.append([3, 4])
print("append:", numbers)

numbers = [1, 2]
numbers.extend([3, 4])
print("extend:", numbers)


# =====================================================
# 6. REMOVE, POP AND DEL
# =====================================================

print("\nremove(), pop(), del:")

numbers = [10, 20, 30]
numbers.remove(20)
print("remove:", numbers)

numbers = [10, 20, 30]
removed = numbers.pop(1)
print("pop removed:", removed)
print("after pop:", numbers)

numbers = [10, 20, 30]
del numbers[1]
print("del:", numbers)


# =====================================================
# 7. DICTIONARY ACCESS AND GET
# =====================================================

print("\nDictionary Access:")

student = {
    "name": "Ravi",
    "age": 21
}

print("Age:", student["age"])
print("Marks:", student.get("marks"))
print("Marks with default:", student.get("marks", 0))


# =====================================================
# 8. STUDENT MANAGEMENT SYSTEM
# =====================================================

students_by_id = {
    101: {
        "name": "Ravi",
        "email": "ravi@example.com",
        "phone": "9876543210",
        "course": "Python",
        "marks": 85,
        "attendance": 90
    },
    102: {
        "name": "Anil",
        "email": "anil@example.com",
        "phone": "9876543211",
        "course": "Django",
        "marks": 78,
        "attendance": 88
    }
}

students_by_email = {
    "ravi@example.com": 101,
    "anil@example.com": 102
}

students_by_name = {
    "Ravi": [101],
    "Anil": [102]
}

print("\nStudent Management System:")
print("By ID:", students_by_id.get(101))
print("ID by Email:", students_by_email.get("ravi@example.com"))
print("IDs by Name:", students_by_name.get("Ravi"))
