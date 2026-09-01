# PYTHON FULL STACK — DAY 2
# Control Flow & Loops

For ST School Python Full Stack Students

---

# 1. Learning Objectives

- Understand control flow in Python.
- Use if, elif, and else.
- Write conditions using comparison and logical operators.
- Understand nested conditions.
- Use Python's match statement.
- Understand loops and why they are needed.
- Use for and while loops.
- Use break and continue.
- Use enumerate() to get index and value together.
- Use zip() to iterate over multiple sequences.
- Solve real-world problems using control flow and loops.

---

# 2. What is Control Flow?

Normally, a Python program executes instructions from top to bottom.

Real applications need to make decisions and repeat work.

Control flow determines which code runs, when it runs, and how many times it runs.

Example:

print("Step 1")
print("Step 2")
print("Step 3")

Control Flow → Decisions + Repetition

---

# 3. Types of Control Flow

## Conditional Statements

- if
- elif
- else
- match

## Loops

- for
- while
- break
- continue
- enumerate()
- zip()

---

# 4. Why Do We Need Conditions?

Imagine a login system.

The application must decide whether the username and password are correct.

If they are correct, login is allowed; otherwise it is rejected.

---

# 5. The if Statement

The if statement executes code only when a condition is True.

Example:

age = 20

if age >= 18:
    print("You are eligible to vote")

If age is 20, the condition 20 >= 18 is True, so the indented block runs.

---

# 6. Python Indentation

Indentation is part of Python syntax.

It identifies a block of code.

Four spaces are the normal convention.

## Correct

if age >= 18:
    print("Adult")

## Incorrect

if age >= 18:
print("Adult")

---

# 7. if with Comparison Operators

Conditions can use:

- >
- <
- >=
- <=
- ==
- !=

Example:

marks = 75

if marks >= 40:
    print("Pass")

---

# 8. if with Logical Operators

## and

Both conditions must be true.

Example:

if age >= 18 and age <= 60:
    print("Eligible")

## or

At least one condition must be true.

Example:

if day == "Saturday" or day == "Sunday":
    print("Weekend")

## not

Reverses a Boolean result.

Example:

if not is_logged_in:
    print("Please login")

---

# 9. The if-else Statement

Use if-else when there are two possible outcomes.

Example:

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

---

# 10. Real-World Example — Login

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

---

# 11. The if-elif-else Statement

Use if-elif-else when there are more than two possibilities.

Example:

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

---

# 12. How if-elif-else Works

Python checks conditions from top to bottom.

The first True condition executes, then the remaining conditions are skipped.

---

# 13. Order of Conditions Matters

This is incorrect for grade classification because a high mark may match the first condition too early.

Example:

marks = 95

if marks >= 40:
    print("Pass")
elif marks >= 90:
    print("Excellent")

Better:

if marks >= 90:
    print("Excellent")
elif marks >= 40:
    print("Pass")

---

# 14. Nested if

An if statement inside another if statement is called a nested if.

Example:

age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

Sometimes nested conditions can be simplified:

if age >= 18 and has_id:
    print("Entry allowed")

---

# 15. Conditional Expression

A conditional expression is a short form of if-else for simple decisions.

Example:

age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)

Use this only when it keeps the code easy to read.

---

# 16. What is match?

Python's match statement provides pattern matching and is available from Python 3.10 onwards.

Example:

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

case _ is a catch-all/default pattern.

---

# 17. match vs if-elif

Use if/elif when conditions involve ranges or complex logical expressions.

Use match when matching a value against clear cases makes the code easier to understand.

Example:

choice = "add"

match choice:
    case "add":
        print("Addition")
    case "subtract":
        print("Subtraction")
    case "multiply":
        print("Multiplication")
    case _:
        print("Invalid")

---

# 18. match with Multiple Alternatives

Example:

day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid day")

---

# 19. What is a Loop?

A loop allows us to execute a block of code repeatedly.

Loops are useful for processing:

- Lists
- Database records
- API results
- Files
- Totals
- Searches
- Repeated tasks

Loop → Repeat a block of code

---

# 20. Types of Loops

There are two main types of loops:

1. for loop
2. while loop

---

# 21. for Loop

A for loop is commonly used to iterate over a sequence or iterable.

Example:

students = ["Ravi", "Anu", "Kiran"]

for student in students:
    print(student)

---

# 22. How a for Loop Works

The loop processes each item one by one.

Ravi → run block

Anu → run block

Kiran → run block

---

# 23. Looping Through a String

Example:

name = "Python"

for character in name:
    print(character)

Output:

P
y
t
h
o
n

---

# 24. range()

range() is commonly used with for loops.

Example:

for i in range(5):
    print(i)

Output:

0
1
2
3
4

The stop value is excluded.

---

# 25. range(start, stop)

Example:

for i in range(1, 6):
    print(i)

Output:

1
2
3
4
5

---

# 26. range(start, stop, step)

Example:

for i in range(1, 10, 2):
    print(i)

Output:

1
3
5
7
9

---

# 27. Reverse Loop

Example:

for i in range(5, 0, -1):
    print(i)

Output:

5
4
3
2
1

---

# 28. Loop with a Condition

Example:

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        print(number)

Output:

2
4
6

---

# 29. while Loop

A while loop runs while its condition remains True.

Example:

count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5

---

# 30. Understanding while

The basic flow is:

Check condition
→ True
→ Run code
→ Update value
→ Check again
→ False
→ Stop

---

# 31. Infinite Loops

Be careful when the condition can never become False.

## Infinite loop example:

count = 1

while count <= 5:
    print(count)

The condition variable is never updated.

## Correct:

count = 1

while count <= 5:
    print(count)
    count += 1

---

# 32. for vs while

| for | while |
|---|---|
| Commonly iterates over a sequence/iterable | Repeats while a condition is true |
| Useful when iterating through known data | Useful when repetition depends on a condition |
| Often simpler for collections | Useful when iteration count is not known beforehand |

---

# 33. break

break immediately stops the loop.

Example:

for number in range(1, 10):
    if number == 5:
        break
    print(number)

Output:

1
2
3
4

---

# 34. Real-World break Example

Example:

students = ["Ravi", "Anu", "Kiran", "Rahul"]

for student in students:
    if student == "Kiran":
        print("Student found")
        break

---

# 35. continue

continue skips the current iteration and moves to the next iteration.

Example:

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

Output:

1
2
4
5

---

# 36. break vs continue

break → STOP THE LOOP

continue → SKIP THIS ITERATION → CONTINUE LOOP

---

# 37. enumerate()

enumerate() is useful when we need both the index and the value.

Example:

students = ["Ravi", "Anu", "Kiran"]

for index, student in enumerate(students):
    print(index, student)

Output:

0 Ravi
1 Anu
2 Kiran

---

# 38. enumerate() Starting from 1

Example:

students = ["Ravi", "Anu", "Kiran"]

for index, student in enumerate(students, start=1):
    print(index, student)

Output:

1 Ravi
2 Anu
3 Kiran

---

# 39. Real-World enumerate() Example

tasks = [
    "Learn Python",
    "Practice loops",
    "Build API"
]

for number, task in enumerate(tasks, start=1):
    print(number, task)

Output:

1 Learn Python
2 Practice loops
3 Build API

---

# 40. zip()

zip() allows us to iterate over multiple sequences together.

Example:

names = ["Ravi", "Anu", "Kiran"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(name, mark)

Output:

Ravi 85
Anu 90
Kiran 78

---

# 41. How zip() Works

Ravi → 85

Anu → 90

Kiran → 78

---

# 42. zip() with Three Lists

Example:

names = ["Ravi", "Anu", "Kiran"]
ages = [21, 22, 20]
cities = ["Hyderabad", "Chennai", "Bangalore"]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)

---

# 43. Important zip() Behavior

When iterables have different lengths, normal zip() stops when the shortest iterable is exhausted.

Example:

names = ["Ravi", "Anu", "Kiran"]
marks = [85, 90]

for name, mark in zip(names, marks):
    print(name, mark)

Output:

Ravi 85
Anu 90

Kiran has no matching mark, so it is not processed.

---

# 44. Nested Loops

A loop inside another loop is called a nested loop.

Example:

for i in range(3):
    for j in range(3):
        print(i, j)

Nested loops are useful for:

- Tables
- Matrices
- Combinations
- Pattern problems

---

# 45. Multiplication Table

Example:

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

Output:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

---

# 46. Combining for, if and continue

Example:

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 != 0:
        continue
    print(number)

Output:

2
4
6

---

# 47. Combining for, if and break

Example:

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        break
    print(number)

Output:

10
20

---

# 48. Real-World Example — Login Attempts

correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password")
    attempts += 1

---

# 49. Real-World Example — Student Grades

students = ["Ravi", "Anu", "Kiran"]
marks = [85, 72, 35]

for student, mark in zip(students, marks):
    if mark >= 40:
        print(student, "Pass")
    else:
        print(student, "Fail")

Output:

Ravi Pass
Anu Pass
Kiran Fail

---

# 50. Real-World Example — Finding a Product

products = ["Laptop", "Phone", "Tablet", "Watch"]

search = "Tablet"

for product in products:
    if product == search:
        print("Product found")
        break

---

# 51. Common Beginner Mistakes

- Missing indentation after if/for/while.
- Creating an infinite while loop by never updating the condition variable.
- Confusing break and continue.
- Putting broad conditions before specific conditions.
- Forgetting that range() excludes the stop value.
- Using a loop when a simpler direct operation would be clearer.
- Assuming zip() fills missing values when lengths differ.

---

# 52. Practice Exercises

## Exercise 1 — Positive, Negative or Zero

Take a number from the user and display Positive, Negative, or Zero.

### Answer:

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

---

## Exercise 2 — Largest of Two Numbers

Take two numbers and determine which is larger.

### Answer:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both are equal")

---

## Exercise 3 — Grade Calculator

Take marks and display:

- A for 90–100
- B for 75–89
- C for 60–74
- D for 40–59
- Otherwise Fail

### Answer:

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")

---

## Exercise 4 — Print Numbers

Use a for loop to print numbers 1 to 10.

### Answer:

for i in range(1, 11):
    print(i)

---

## Exercise 5 — Even Numbers

Print all even numbers between 1 and 50.

### Answer:

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

---

## Exercise 6 — Sum of Numbers

Calculate the sum of numbers from 1 to 100.

### Answer:

total = 0

for i in range(1, 101):
    total += i

print(total)

Output:

5050

---

## Exercise 7 — Multiplication Table

Take a number and print its multiplication table from 1 to 10.

### Answer:

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

---

## Exercise 8 — Countdown

Using while, print 10 to 1 and then print Blast Off!

### Answer:

count = 10

while count >= 1:
    print(count)
    count -= 1

print("Blast Off!")

---

## Exercise 9 — Find a Student

Search a list of students and use break when the requested student is found.

### Answer:

students = ["Ravi", "Anu", "Kiran", "Rahul"]

search = input("Enter student name: ")

for student in students:
    if student == search:
        print("Student found")
        break
else:
    print("Student not found")

---

## Exercise 10 — Skip Multiples of 3

Print 1 to 30 but skip numbers divisible by 3 using continue.

### Answer:

for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)

---

## Exercise 11 — enumerate()

Print a numbered task list using enumerate(..., start=1).

### Answer:

tasks = [
    "Learn Python",
    "Practice loops",
    "Build API"
]

for number, task in enumerate(tasks, start=1):
    print(number, task)

---

## Exercise 12 — zip()

Combine student names and marks using zip() and display each pair.

### Answer:

names = ["Ravi", "Anu", "Kiran"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(name, mark)

---

# 53. Interview Questions

## 1. What is control flow?

Control flow determines which code runs, when it runs, and how many times it runs.

## 2. What is an if statement?

An if statement executes code when a condition is True.

## 3. Difference between if and if-else?

if handles a condition when it is True. if-else provides two possible outcomes.

## 4. What is elif?

elif means "else if" and is used to check another condition.

## 5. How does if-elif-else work?

Python checks conditions from top to bottom. The first True condition executes.

## 6. Why does condition order matter?

Because Python checks conditions from top to bottom. A broad condition can prevent a more specific condition from being checked.

## 7. What is nested if?

An if statement inside another if statement is called nested if.

## 8. What is a conditional expression?

It is a short form of if-else for simple decisions.

## 9. What is match?

match provides pattern matching and is available from Python 3.10 onwards.

## 10. Which Python version introduced match?

Python 3.10.

## 11. What does case _ mean?

case _ is a catch-all/default pattern.

## 12. Difference between if-elif and match?

Use if-elif for ranges or complex logical expressions. Use match for clear value-based cases.

## 13. What is a loop?

A loop repeatedly executes a block of code.

## 14. Why are loops needed?

Loops allow us to repeat code without writing the same code multiple times.

## 15. Difference between for and while?

for is commonly used to iterate over an iterable. while repeats while a condition is True.

## 16. What does range() do?

range() generates a sequence of numbers and is commonly used with for loops.

## 17. Why does range(5) produce 0–4?

Because the stop value in range() is excluded.

## 18. What is an infinite loop?

An infinite loop occurs when a loop condition never becomes False.

## 19. What is break?

break immediately stops the loop.

## 20. What is continue?

continue skips the current iteration and moves to the next iteration.

## 21. Difference between break and continue?

break stops the loop.

continue skips the current iteration.

## 22. What is enumerate()?

enumerate() provides both index and value while iterating.

## 23. Why use enumerate()?

It allows us to get the index and value together without manually maintaining a counter.

## 24. What is zip()?

zip() allows us to iterate over multiple sequences together.

## 25. What happens when zip() receives iterables of different lengths?

Normal zip() stops when the shortest iterable is exhausted.

## 26. What is a nested loop?

A loop inside another loop is called a nested loop.

## 27. How can you search a list using a loop?

Iterate through the list, compare each item with the search value, and use break when the item is found.

## 28. How can you skip values while looping?

Use continue.

## 29. How can you stop after finding an item?

Use break after finding the item.

## 30. Can break and continue be used in both for and while loops?

Yes. Both break and continue can be used in for and while loops.

---

# 54. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| if | Execute code when condition is true |
| elif | Check another condition |
| else | Execute when previous conditions are false |
| match | Match a value against patterns/cases |
| case _ | Default/catch-all case |
| for | Iterate over an iterable |
| while | Repeat while condition is true |
| break | Stop the loop |
| continue | Skip current iteration |
| range() | Generate a sequence of numbers |
| enumerate() | Get index + value |
| zip() | Combine items from multiple iterables |
| Nested loop | Loop inside another loop |

---

# 55. Final Mental Model

## Program Flow

PROGRAM
→ MAKE A DECISION
→ TRUE / FALSE
→ EXECUTE APPROPRIATE BLOCK

## Loop Flow

LOOP
→ CHECK CONDITION
→ RUN CODE
→ NEXT ITERATION
→ CHECK AGAIN

---

# Final Summary

Conditions help your program make decisions.

Loops help your program repeat work.

break stops a loop.

continue skips one iteration.

enumerate() gives index + value.

zip() lets you process multiple sequences together.

These concepts are the foundation for writing real business logic in Python.

Next major topics:

Strings
→ Lists
→ Tuples
→ Sets
→ Dictionaries
→ Functions

Followed by advanced Python concepts and FastAPI backend development.

---

# END OF DAY 2

## Control Flow & Loops

Python Full Stack – ST School