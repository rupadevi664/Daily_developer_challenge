def greet(name):
    print(name)

greet("rupa")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b
print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(divide(1,2))

def calculate_sum(**details):
    for keys,value in details.items():
        print(keys,":",value)
calculate_sum(name="rupa",age=12,course="cse")

def calculate_sum(*numbers):
    print(sum(numbers))

calculate_sum(1,2)
calculate_sum(1,23,3)
calculate_sum(23,34,54)

#lamdba
square=lambda x:x*x
print(square(5))

square=lambda x,y:x+y
print(square(5,10))

check_age=lambda age:"adult" if age>=18 else "minor"
print(check_age(20)) 

students = [
    ("Ravi", 75),
    ("Anu", 90),
    ("Kiran", 60),
    ("Priya", 85)
]

students.sort(key=lambda student: student[0])

print(students)