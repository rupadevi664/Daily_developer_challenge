# Day 2 - Control Flow & Loops


#Take a number from the user and display whether the number is Positive, Negative, or Zero.


number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both are equal")

#Grade Calculator
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

#Print Numbers 1 to 10
for i in range(1, 11):
    print(i)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#Sum of Numbers

total = 0

for i in range(1, 101):
    total += i

print(total)


#7.Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

#Problem 8: Countdown
count = 10

while count >= 1:
    print(count)
    count -= 1

print("Blast Off!")

#Problem 9: Find a Student
students = ["Ravi", "Anu", "Kiran", "Rahul"]

search = input("Enter student name: ")

for student in students:
    if student == search:
        print("Student found")
        break
else:
    print("Student not found")


#Problem 10: Skip Multiples of 3
for i in range(1, 31):
    if i % 3 == 0:
        continue

    print(i)

#Problem 11: Numbered Task List

tasks = [
    "Learn Python",
    "Practice loops",
    "Build API"
]

for number, task in enumerate(tasks, start=1):
    print(number, task)


#Problem 12: Student Names and Marks

names = ["Ravi", "Anu", "Kiran"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
    print(name, mark)