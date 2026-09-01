""" DAY 5 — FUNCTIONS, DICTIONARIES & DATA VALIDATION ST School | Python Fullstack Program | Daily Developer Challenge QUESTIONS AND ANSWERS """


# 1. CODING PROBLEM — STUDENT RECORD MANAGER

students = [
    {"id": 101, "name": "Ravi", "marks": 85},
    {"id": 102, "name": "Anil", "marks": 72},
    {"id": 103, "name": "Kiran", "marks": 91},
    {"id": 104, "name": "Priya", "marks": 78}
]



# Student Record Manager


def add_student(student_id, name, marks):
    """Add a new student after validating ID and marks."""

    if not isinstance(marks, (int, float)) or not 0 <= marks <= 100:
        return "Invalid marks. Marks must be between 0 and 100."

    for student in students:
        if student["id"] == student_id:
            return "Student ID already exists."

    students.append({
        "id": student_id,
        "name": name,
        "marks": marks
    })

    return "Student added successfully."


def search_student(student_id):
    """Search for a student by ID."""

    for student in students:
        if student["id"] == student_id:
            return student

    return "Student not found."


def update_marks(student_id, marks):
    """Update a student's marks after validation."""

    if not isinstance(marks, (int, float)):
        return "Marks must be numeric."

    if not 0 <= marks <= 100:
        return "Marks must be between 0 and 100."

    for student in students:
        if student["id"] == student_id:
            student["marks"] = marks
            return "Marks updated successfully."

    return "Student not found."


def delete_student(student_id):
    """Delete a student by ID."""

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return "Student deleted successfully."

    return "Student not found."


def display_students():
    """Display all student records."""

    if not students:
        print("No students available.")
        return

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}"
        )


def highest_marks_student():
    """Find the student with the highest marks."""

    if not students:
        return "No students available."

    highest = students[0]

    for student in students[1:]:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest


def get_students_above(threshold):
    """Return all students whose marks are above a threshold."""

    if not isinstance(threshold, (int, float)):
        return "Threshold must be numeric."

    if not 0 <= threshold <= 100:
        return "Threshold must be between 0 and 100."

    result = []

    for student in students:
        if student["marks"] > threshold:
            result.append(student)

    return result

# Q1. Add a new student.
# Answer:
# Use a function that checks whether the ID already exists and
# validates that marks are between 0 and 100.


students = [
    {"id": 101, "name": "Ravi", "marks": 85},
    {"id": 102, "name": "Anil", "marks": 72},
    {"id": 103, "name": "Kiran", "marks": 91},
    {"id": 104, "name": "Priya", "marks": 78}
]


def add_student(student_id, name, marks):
    if not isinstance(marks, (int, float)):
        return "Invalid marks: marks must be numeric."

    if marks < 0 or marks > 100:
        return "Invalid marks: marks must be between 0 and 100."

    for student in students:
        if student["id"] == student_id:
            return "Student ID already exists."

    students.append({
        "id": student_id,
        "name": name,
        "marks": marks
    })

    return "Student added successfully."


# Q2. Search for a student by ID.
# Answer:
# Loop through the list and compare each student's ID.


def search_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return "Student not found."


# Q3. Update a student's marks.
# Answer:
# Validate the marks first, then find the student and update "marks".


def update_marks(student_id, marks):
    if not isinstance(marks, (int, float)):
        return "Marks must be numeric."

    if marks < 0 or marks > 100:
        return "Marks must be between 0 and 100."

    for student in students:
        if student["id"] == student_id:
            student["marks"] = marks
            return "Marks updated successfully."

    return "Student not found."


# Q4. Delete a student by ID.
# Answer:
# Find the student by ID and remove it from the list.


def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return "Student deleted successfully."

    return "Student not found."


# Q5. Display all students.
# Answer:
# Loop through the list and print each dictionary.


def display_students():
    if not students:
        print("No students available.")
        return

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}"
        )


# Q6. Find the student with the highest marks.
# Answer:
# Compare the marks of all students and keep the highest record.


def highest_marks_student():
    if not students:
        return "No students available."

    highest = students[0]

    for student in students[1:]:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest


# BONUS: Get students above a marks threshold.
# Example: get_students_above(80) -> Ravi, Kiran


def get_students_above(threshold):
    if not isinstance(threshold, (int, float)):
        return "Threshold must be numeric."

    if threshold < 0 or threshold > 100:
        return "Threshold must be between 0 and 100."

    result = []

    for student in students:
        if student["marks"] > threshold:
            result.append(student)

    return result



# 2. CONCEPT QUESTIONS — FUNCTIONS & SCOPE


# Q7. What is the difference between local scope and global scope?
#
# Answer:
# Local scope refers to variables created inside a function.
# They are normally accessible only inside that function.
#
# Global scope refers to variables created outside functions.
# They can be accessed from different parts of the program.


# Q8. Why is using global variables everywhere considered a bad practice?
#
# Answer:
# Using global variables everywhere can make code:
# - difficult to understand
# - difficult to test
# - difficult to debug
# - difficult to maintain
#
# Functions may also accidentally change shared data.
# Passing required data as parameters usually creates cleaner code.


# Q9. What is the purpose of passing data into a function instead
# of using a global variable?
#
# Answer:
# Passing data through parameters makes functions:
# - reusable
# - independent
# - easier to test
# - easier to understand
#
# Example:


def add(a, b):
    return a + b


# Q10. What is the difference between a function that returns a value
# and a function that modifies a data structure?
#
# Answer:
# A function that returns a value gives a result back to the caller.
#
# A function that modifies a data structure changes an existing
# mutable object such as a list or dictionary.


def calculate_total(a, b):
    return a + b


sample_list = []


def add_name(items, name):
    items.append(name)


# Think About This:
#
# students = []
#
# def add_student(name):
# students.append(name)
#
# add_student("Ravi")
# print(students)
#
# Is students local or global inside add_student()?
#
# Answer:
# students is a GLOBAL variable because it was created outside
# the function.
#
# What changes if students is passed as a parameter?
#
# Answer:
# The function becomes more explicit and does not depend on a
# global variable.


def add_student_using_parameter(students_list, name):
    students_list.append(name)


# Interview Follow-up:
#
# Q: Which approach would you prefer in a real application, and why?
#
# Answer:
# Passing data through parameters is generally preferred because
# it reduces hidden dependencies and makes functions easier to
# test, reuse, and maintain.



# 3. DEBUGGING CHALLENGE — UPDATING A DICTIONARY


# Given code:
#
# student = {
# "id": 101,
# "name": "Ravi",
# "marks": 80
# }
#
# def update_marks(student, marks):
# if marks >= 0 and marks <= 100:
# student["mark"] = marks
# return True
# return False
#
# update_marks(student, 95)
# print(student["marks"])


# Q11. Predict what happens when the program runs.
#
# Answer:
# The function creates/updates a key called "mark" with value 95.
# The original key "marks" still contains 80.
#
# Therefore:
#
# print(student["marks"])
#
# prints:
#
# 80


# Q12. Find the logical error.
#
# Answer:
# The dictionary contains "marks", but the function uses "mark".
#
# "mark" and "marks" are different dictionary keys.


# Q13. Fix the code.
#
# Answer:


student = {
    "id": 101,
    "name": "Ravi",
    "marks": 80
}


def update_student_marks(student, marks):
    if 0 <= marks <= 100:
        student["marks"] = marks
        return True

    return False


# Q14. Explain why the error occurred.
#
# Answer:
# Python dictionaries use exact key names.
# "mark" is not the same key as "marks".
# Therefore, student["mark"] = 95 creates a separate key instead
# of updating student["marks"].


# Q15. Modify the function so it returns a meaningful
# success/failure message.
#
# Answer:


def update_marks_with_message(student, marks):
    if not isinstance(marks, (int, float)):
        return "Failed: Marks must be numeric."

    if marks < 0 or marks > 100:
        return "Failed: Marks must be between 0 and 100."

    if "marks" not in student:
        return "Failed: Marks key is missing."

    student["marks"] = marks

    return "Success: Marks updated successfully."


# BONUS:
#
# Q: What would happen if the dictionary did not contain the key
# "marks"? How could you make the function safer?
#
# Answer:
# Accessing student["marks"] when the key does not exist can cause
# a KeyError.
#
# We can safely check first:
#
# if "marks" not in student:
# return "Marks key is missing."
#
# Or use:
#
# student.get("marks")


# 4. MINI CHALLENGE — WORD ANALYZER

# Q16. How do you find the total number of words?
#
# Answer:
# Split the sentence into words and use len().
#
# Example:
# words = sentence.split()
# total_words = len(words)


# Q17. How do you find the total number of characters
# excluding spaces?
#
# Answer:
# Count characters while ignoring spaces.


# Q18. How do you find the longest word?
#
# Answer:
# Start with the first word and compare the length of each word.


# Q19. How do you find the shortest word?
#
# Answer:
# Start with the first word and replace it whenever a shorter
# word is found.


# Q20. How do you find the number of unique words?
#
# Answer:
# Convert the words into a set because a set stores unique values.


def analyze_sentence(sentence):
    words = sentence.split()

    if not words:
        return {
            "words": 0,
            "characters": 0,
            "longest_word": None,
            "shortest_word": None,
            "unique_words": 0
        }

    characters = 0

    for char in sentence:
        if char != " ":
            characters += 1

    longest_word = words[0]
    shortest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

    return {
        "words": len(words),
        "characters": characters,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "unique_words": len(set(words))
    }


# Input:
# "Python makes programming interesting"
#
# Expected:
# Words: 4
# Characters excluding spaces: 34
# Longest word: programming
# Shortest word: makes
# Unique words: 4


# BONUS:
# Make the analysis case-insensitive and ignore punctuation
# such as .,!? when identifying unique words.


import string


def analyze_sentence_bonus(sentence):
    cleaned = sentence.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = cleaned.lower().split()

    if not words:
        return {
            "words": 0,
            "characters": 0,
            "longest_word": None,
            "shortest_word": None,
            "unique_words": 0
        }

    longest_word = words[0]
    shortest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

    return {
        "words": len(words),
        "characters": sum(len(word) for word in words),
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "unique_words": len(set(words))
    }



# 5. MINI INTERVIEW ROUND


# Q21. What is the difference between a list of dictionaries
# and a dictionary of dictionaries?
#
# Answer:
#
# List of dictionaries:
#
# students = [
# {"id": 101, "name": "Ravi"},
# {"id": 102, "name": "Anil"}
# ]
#
# Dictionary of dictionaries:
#
# students = {
# 101: {"name": "Ravi", "marks": 85},
# 102: {"name": "Anil", "marks": 72}
# }
#
# A list stores multiple dictionaries as elements.
# A dictionary of dictionaries uses keys to identify nested records.


# Q22. How do you check whether a key exists in a dictionary?
#
# Answer:
# Use the "in" operator.
#
# Example:
#
# if "name" in student:
# print("Name exists")
#
# Another safe option for retrieving a value is:
#
# student.get("marks")


# Q23. What is the difference between == and is?
#
# Answer:
# == compares VALUES.
# is checks whether two references point to the SAME OBJECT.
#
# Example:
#
# a = [1, 2]
# b = [1, 2]
#
# a == b -> True
# a is b -> False


# Q24. Why should input validation happen before processing data?
#
# Answer:
# Input validation:
# - prevents invalid data from being processed
# - reduces unexpected errors
# - protects database integrity
# - improves application stability
# - provides clear error messages
# - helps with security


# Q25. What is defensive programming?
#
# Answer:
# Defensive programming means writing code that expects invalid
# input, unexpected situations, and edge cases and handles them safely.
#
# Example:


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."

    return a / b


# Q26. Why should functions generally do one clear job?
#
# Answer:
# A function with one clear responsibility is:
# - easier to understand
# - easier to test
# - easier to debug
# - easier to reuse
# - easier to maintain
#
# Example:
# validate_student()
# add_student()
# search_student()
# delete_student()

# 6. THINK LIKE A BACKEND DEVELOPER


# Input received by a backend API:
#
# {
# "name": "Ravi",
# "age": "twenty",
# "marks": 150
# }


# Q: What validations should be performed before saving this data?
#
# Answer:
#
# 1. Check whether name is present.
# 2. Check whether age has the correct data type.
# 3. Check whether age is within a valid range.
# 4. Check whether marks are numeric.
# 5. Check whether marks are between 0 and 100.
# 6. Check whether required fields are missing.
# 7. Check for unexpected values.


def validate_student(data):
    required_fields = ["name", "age", "marks"]

    for field in required_fields:
        if field not in data:
            return f"{field} is required."

    if not isinstance(data["name"], str) or not data["name"].strip():
        return "Name must be a non-empty string."

    if not isinstance(data["age"], int):
        return "Age must be an integer."

    if not 1 <= data["age"] <= 120:
        return "Age must be between 1 and 120."

    if not isinstance(data["marks"], (int, float)):
        return "Marks must be numeric."

    if not 0 <= data["marks"] <= 100:
        return "Marks must be between 0 and 100."

    return "Validation successful."


# Q: Why is input validation especially important in backend development?
#
# Answer:
# Backend applications receive data from clients, so the backend
# should not assume that the input is correct.
#
# Validation protects:
# - data quality
# - application stability
# - security
# - database integrity
# - business rules



# 7. 60-SECOND DEVELOPER EXPLANATION


# Q: Explain one of today's programs in 60 seconds.
#
# Answer:
#
# "I created a Student Record Manager in Python using a list of
# dictionaries. Each dictionary represents one student and contains
# an ID, name, and marks. I separated the functionality into
# individual functions for adding, searching, updating, deleting,
# displaying students, and finding the highest marks. I added
# validation to make sure student IDs are unique and marks stay
# between 0 and 100. I also handled edge cases such as duplicate
# IDs, invalid marks, an empty list, missing students, and missing
# dictionary keys. If this became a real backend application, I
# would use a database, REST API validation, authentication,
# exception handling, logging, and automated tests."


# Q: What problem are you solving?
# Answer:
# Managing student records and performing CRUD-like operations.


# Q: What data structure did you choose?
# Answer:
# A list of dictionaries.


# Q: Why did you choose it?
# Answer:
# Each dictionary represents one student, while the list stores
# multiple student records.


# Q: How did you handle invalid input?
# Answer:
# I validate IDs, marks, data types, required fields, and valid ranges
# before processing the data.


# Q: What edge cases did you consider?
# Answer:
# Duplicate IDs, marks below 0, marks above 100, non-existing IDs,
# empty student list, missing dictionary keys, and incorrect data types.


# Q: What would you improve if this became a real application?
# Answer:
# I would add a database, REST APIs, schema validation,
# authentication, authorization, exception handling, logging,
# and automated tests.



# 8. DAY 5 MENTOR QUESTIONS


# Q: What happens if the user gives invalid input?
# Answer:
# Validate it before processing and return a meaningful error.


# Q: What happens if this data doesn't exist?
# Answer:
# Handle it safely and return a message such as "Student not found."


# Q: Can you turn this repeated logic into a function?
# Answer:
# Yes. Repeated validation or processing should be placed into
# reusable functions.


# Q: Why did you choose this data structure?
# Answer:
# A list of dictionaries represents multiple student records clearly,
# with each dictionary storing related student fields.



# 9. DAY 5 MINDSET


# Real applications don't receive perfect input.
#
# A good developer:
# - expects mistakes
# - validates data
# - handles edge cases
# - handles errors
# - fails gracefully
#
# Development flow:
#
# Understand -> Design -> Validate -> Implement -> Test
# -> Handle Errors -> Explain



# SIMPLE TEST


if __name__ == "__main__":

    print("=== Q1: ADD STUDENT ===")
    print(add_student(105, "Sita", 88))

    print("\n=== Q2: SEARCH STUDENT ===")
    print(search_student(103))
    print(search_student(999))

    print("\n=== Q3: UPDATE MARKS ===")
    print(update_marks(102, 80))

    print("\n=== Q4: DELETE STUDENT ===")
    print(delete_student(104))

    print("\n=== Q5: DISPLAY STUDENTS ===")
    display_students()

    print("\n=== Q6: HIGHEST MARKS ===")
    print(highest_marks_student())

    print("\n=== BONUS: ABOVE 80 ===")
    print(get_students_above(80))

    print("\n=== Q13/Q15: DICTIONARY UPDATE ===")
    test_student = {
        "id": 101,
        "name": "Ravi",
        "marks": 80
    }

    print(update_marks_with_message(test_student, 95))
    print(test_student)

    print("\n=== Q16-Q20: WORD ANALYZER ===")
    result = analyze_sentence(
        "Python makes programming interesting"
    )

    print("Words:", result["words"])
    print("Characters excluding spaces:", result["characters"])
    print("Longest word:", result["longest_word"])
    print("Shortest word:", result["shortest_word"])
    print("Unique words:", result["unique_words"])

    print("\n=== BONUS WORD ANALYZER ===")
    print(analyze_sentence_bonus(
        "Python, python makes programming interesting!"
    ))

    print("\n=== BACKEND VALIDATION ===")
    invalid_data = {
        "name": "Ravi",
        "age": "twenty",
        "marks": 150
    }

    print(validate_student(invalid_data))