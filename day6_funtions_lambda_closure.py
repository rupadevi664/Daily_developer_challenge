""" Day 6 - Functions, Arguments, Scope, Closures & Lambda Python Full Stack Practice Based on the provided ST School Functions, Arguments, Scope, Closures & Lambda material. """


# 1. GREETING FUNCTION
# create greet(name) that display hello ravi

def greet(name):
    print("Hello", name)


greet("Ravi")


# 2. CALCULATOR FUNCTIONS
# create add, subtract, multiply, divide functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Add:", add(10, 20))
print("Subtract:", subtract(20, 10))
print("Multiply:", multiply(10, 20))
print("Divide:", divide(20, 10))


# 3. DEFAULT PARAMETER
#create greet(name,message="welcome") and test it with and without the second argument

def welcome(name, message="Welcome"):
    print(message, name)


welcome("Ravi")
welcome("Ravi", "Hello")


# 4. *args
# create calculate_sum(*numbers) accepts any number of numbers and returns their sum

def calculate_sum(*numbers):
    return sum(numbers)


print("Sum:", calculate_sum(10, 20))
print("Sum:", calculate_sum(10, 20, 30, 40))



# 5. **kwargs
#create a display_profile **details accept any number of numbers and return the sum

def display_profile(**details):
    for key, value in details.items():
        print(key, ":", value)


display_profile(
    name="Ravi",
    age=21,
    city="Hyderabad",
    course="Python"
)



# 6. STUDENT RESULT
#crete calculate_result(name,*marks) and calculate total average,and result

def calculate_result(name, *marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


calculate_result("Ravi", 80, 75, 90, 85)



# 7. SCOPE - LOCAL VS GLOBAL
#create a global varaible and local variable with the same name.observe the output inside  and outside the function

name = "Global Ravi"


def show_name():
    name = "Local Anu"
    print("Inside function:", name)


show_name()
print("Outside function:", name)


# 8. GLOBAL KEYWORD
#create multipler(factor),return an inner function and create double and triple

count = 0


def increment():
    global count
    count += 1


increment()
increment()
print("Global count:", count)


# 9. CLOSURE
# create lamdba function that calculate the square of a number

def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor

    return multiply_by_factor


double = multiplier(2)
triple = multiplier(3)

print("Double:", double(10))
print("Triple:", triple(10))


# 10. LAMBDA - SQUARE
#use filter( ) lamdba  to find numbers greater than 20 from the list [10,15,20,25,30,35] 

square = lambda x: x * x

print("Square:", square(5))


# 11. LAMBDA + filter()
#sort students by marks using lamdba

numbers = [10, 15, 20, 25, 30, 35]

greater_than_20 = list(
    filter(lambda x: x > 20, numbers)
)

print("Numbers greater than 20:", greater_than_20)

# 12. LAMBDA + sort()


students = [
    ("Ravi", 85),
    ("Anu", 92),
    ("Kiran", 75)
]

students.sort(key=lambda student: student[1])

print("Students sorted by marks:", students)


# 13. LAMBDA + map()


numbers = [1, 2, 3, 4]

squares = list(
    map(lambda x: x * x, numbers)
)

print("Squares:", squares)



# 14. POSITIONAL AND KEYWORD ARGUMENTS


def student_info(name, age):
    print("Name:", name)
    print("Age:", age)


# Positional arguments
student_info("Ravi", 21)

# Keyword arguments
student_info(age=21, name="Ravi")



# 15. * UNPACKING


numbers = [10, 20, 30]


def add_three(a, b, c):
    return a + b + c


print("Unpacking with *:", add_three(*numbers))


# 16. ** UNPACKING


student = {
    "name": "Ravi",
    "age": 21
}


def print_student(name, age):
    print("Name:", name)
    print("Age:", age)


print_student(**student)


# 17. COMBINING NORMAL PARAMETER, *args AND **kwargs


def example(name, *args, **kwargs):
    print("Name:", name)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


example(
    "Ravi",
    10,
    20,
    age=21,
    city="Hyderabad"
)


# 18. *args + DEFAULT PARAMETER


def calculate_total(*prices, discount=0):
    total = sum(prices)
    discount_amount = total * discount / 100
    return total - discount_amount


print(
    "Final total:",
    calculate_total(100, 200, 300, discount=10)
)


# 19. **kwargs PRACTICAL EXAMPLE


def create_user(name, age, **details):
    print("Name:", name)
    print("Age:", age)

    for key, value in details.items():
        print(key, ":", value)


create_user(
    "Ravi",
    21,
    city="Hyderabad",
    course="Python",
    role="Student"
)


# 20. CLOSURE WITH CUSTOMIZED FUNCTIONS


def create_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double_number = create_multiplier(2)
triple_number = create_multiplier(3)

print("Double 15:", double_number(15))
print("Triple 15:", triple_number(15))