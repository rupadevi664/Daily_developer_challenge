Day 6 — Functions, Arguments, Scope, Closures & Lambda


Python Full Stack Practice — Questions, Answers & Coding



This repository contains the Day 6 practice material for:



Functions

Parameters and Arguments

return

Positional Arguments

Keyword Arguments

Default Parameters

*args

**kwargs

Argument Unpacking

Local and Global Scope

LEGB Rule

global keyword

Nested Functions

Closures

Lambda Functions

map()

filter()

sorted()


The topics and exercises are based on the provided ST School material. The source PDF labels this material as Day 3; this repository is named Day 6 to match the requested GitHub day numbering.



1. What is a Function?

Answer

A function is a reusable block of code designed to perform a specific task.


Syntax

def function_name():
    # code

Example

def greet():
    print("Hello, ST School!")

greet()


2. Why Do We Use Functions?

Functions provide:



Code reusability

Better organization

Easier debugging

Maintainability

Better readability



3. Parameter vs Argument

Parameter

A parameter is a placeholder in the function definition.


def greet(name):
    print("Hello", name)

Here, name is the parameter.


Argument

An argument is the actual value passed to the function.


greet("Ravi")

Here, "Ravi" is the argument.


Remember

Parameter = placeholder


Argument = actual value



4. What is return?

return sends a value back to the caller.


def add(a, b):
    return a + b

result = add(10, 20)
print(result)

Output:


30


5. print() vs return

print()	return
Displays a value	Sends a value back
Mainly used for output	Can be stored in a variable
Result cannot directly be used for later computation	Result can be used in further expressions


6. What Happens If a Function Has No return?

If a function does not explicitly return a value, Python returns None.


def greet():
    print("Hello")

result = greet()
print(result)

Output:


Hello
None


7. Positional Arguments

Positional arguments are matched based on their position.


def student_info(name, age):
    print(name)
    print(age)

student_info("Ravi", 21)

"Ravi" goes to name and 21 goes to age.



8. Keyword Arguments

Keyword arguments specify the parameter name.


def student_info(name, age):
    print(name)
    print(age)

student_info(age=21, name="Ravi")

The order does not matter because the parameter names are specified.



9. Default Parameters

A default parameter has a fallback value.


def greet(name="Student"):
    print("Hello", name)

greet()
greet("Ravi")

If no argument is supplied, "Student" is used.



10. Rules for Default Parameters

Required parameters should generally come before parameters with default values.


Correct

def greet(name, message="Hello"):
    print(message, name)

A required parameter after a default parameter causes a syntax error.



11. What is *args?

*args allows a function to receive an unknown number of positional arguments.


def add(*args):
    print(args)

add(10, 20, 30)

args is stored as a tuple.


(10, 20, 30)


12. Using *args

def add(*args):
    total = 0

    for number in args:
        total += number

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))


13. Why is *args Useful?

Use *args when the number of positional arguments is unknown.


def calculate_total(*prices):
    return sum(prices)

print(calculate_total(100, 200))
print(calculate_total(100, 200, 300, 400))


14. What is **kwargs?

**kwargs allows a function to receive an unknown number of keyword arguments.


def student_info(**kwargs):
    print(kwargs)

student_info(
    name="Ravi",
    age=21,
    city="Hyderabad"
)

kwargs is stored as a dictionary.



15. Using **kwargs

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(
    name="Ravi",
    age=21,
    course="Python"
)


16. *args vs **kwargs

Feature	*args	**kwargs
Handles	Positional arguments	Keyword arguments
Stores data as	Tuple	Dictionary
Example	10, 20, 30	name="Ravi", age=21


17. Combining Parameters, *args and **kwargs

A common parameter order is:


normal parameters → *args → **kwargs

Example:


def example(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

example(
    "Ravi",
    10,
    20,
    age=21,
    city="Hyderabad"
)


18. What is Argument Unpacking?

Argument unpacking expands a collection into function arguments.


* Unpacking

numbers = [10, 20, 30]

def add(a, b, c):
    return a + b + c

print(add(*numbers))

The list is expanded into positional arguments.


** Unpacking

student = {
    "name": "Ravi",
    "age": 21
}

def student_info(name, age):
    print(name, age)

student_info(**student)

The dictionary is expanded into keyword arguments.



19. What is Scope?

Scope determines where a variable can be accessed.


Scope = Where a variable is visible and accessible


20. Local Scope

A variable created inside a function has local scope.


def greet():
    name = "Ravi"
    print(name)

greet()

name is local to greet().


Trying to use it outside the function causes a NameError.



21. Global Scope

A variable created outside functions has global scope.


name = "Ravi"

def greet():
    print(name)

greet()

A global variable can be read inside the function.



22. Local vs Global

name = "Ravi"

def greet():
    name = "Anu"
    print(name)

greet()
print(name)

Output:


Anu
Ravi

The local and global name variables are separate.



23. LEGB Rule

Python searches for a name approximately in this order:


L → Local
E → Enclosing
G → Global
B → Built-in

Therefore:


Local → Enclosing → Global → Built-in


24. Enclosing Scope

An enclosing variable belongs to an outer function.


def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()

x is not local to inner(), but it exists in the enclosing outer() function.



25. Built-in Scope

Python provides built-in names such as:


print()
len()
sum()
max()
min()
type()


26. global Keyword

The global keyword allows a function to assign to a global variable.


count = 0

def increment():
    global count
    count += 1

increment()
print(count)

For larger applications, excessive global state should be avoided.


Prefer passing data into functions and returning results when practical.



27. What is a Nested Function?

A function defined inside another function is called a nested function.


def outer():

    def inner():
        print("Hello from inner")

    inner()

outer()


28. What is a Closure?

A closure occurs when an inner function remembers and uses variables from its enclosing function even after the enclosing function has finished executing.


def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner

function = outer()
function()

The inner() function still remembers message.


Mental Model

Outer function
      ↓
Creates variable
      ↓
Returns inner function
      ↓
Inner function remembers variable
      ↓
Closure


29. Why Are Closures Useful?

Closures can be useful for:



Creating customized functions

Maintaining state

Data hiding / encapsulation patterns

Callback functions

Decorators

Functional programming techniques


Closures are particularly useful when learning decorators and frameworks such as FastAPI.



30. Practical Closure Example

def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))

Output:


20
30

double remembers factor=2.


triple remembers factor=3.



31. What is a Lambda Function?

A lambda is a small anonymous function.


Normal Function

def square(x):
    return x * x

Lambda

square = lambda x: x * x

print(square(5))

Output:


25


32. Lambda Syntax

lambda arguments: expression

Example:


lambda x: x * 2


33. Lambda with Multiple Parameters

add = lambda a, b: a + b

print(add(10, 20))

Output:


30


34. Lambda with Conditional Expression

check_age = lambda age: "Adult" if age >= 18 else "Minor"

print(check_age(20))

Output:


Adult


35. Lambda with sorted()

students = [
    ("Ravi", 85),
    ("Anu", 92),
    ("Kiran", 75)
]

students.sort(key=lambda student: student[1])

print(students)

The list is sorted using the second item of each tuple — the marks.



36. Lambda with map()

numbers = [1, 2, 3, 4]

squares = list(
    map(lambda x: x * x, numbers)
)

print(squares)

Output:


[1, 4, 9, 16]

map() applies a function to each item.



37. Lambda with filter()

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)

Output:


[2, 4, 6]

filter() keeps items for which the condition is True.



38. When Should We Use Lambda?

Use lambda when:



The function is very small.

The logic is simple.

It is used once or locally.

It makes sorting, filtering, or mapping easier to read.


Avoid lambda for complicated logic. A normal def function is clearer when the expression becomes difficult to understand.



39. Practice Exercises — Questions + Answers

Exercise 1 — Greeting Function

Question

Create greet(name) that displays Hello Ravi.


Answer

def greet(name):
    print("Hello", name)

greet("Ravi")


Exercise 2 — Calculator Functions

Question

Create add(), subtract(), multiply(), and divide().


Answer

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


print(add(10, 20))
print(subtract(20, 10))
print(multiply(10, 20))
print(divide(20, 10))


Exercise 3 — Default Parameter

Question

Create greet(name, message="Welcome") and test it with and without the second argument.


Answer

def greet(name, message="Welcome"):
    print(message, name)


greet("Ravi")
greet("Ravi", "Hello")


Exercise 4 — *args

Question

Create calculate_sum(*numbers) that accepts any number of numbers and returns the sum.


Answer

def calculate_sum(*numbers):
    return sum(numbers)


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40))


Exercise 5 — **kwargs

Question

Create display_profile(**details) and display all supplied profile information.


Answer

def display_profile(**details):
    for key, value in details.items():
        print(key, ":", value)


display_profile(
    name="Ravi",
    age=21,
    city="Hyderabad",
    course="Python"
)


Exercise 6 — Student Result

Question

Create calculate_result(name, *marks) and calculate total, average, and result.


Answer

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


Exercise 7 — Scope

Question

Create a global variable and a local variable with the same name. Observe the output inside and outside the function.


Answer

name = "Ravi"


def show_name():
    name = "Anu"
    print("Inside:", name)


show_name()
print("Outside:", name)

Output:


Inside: Anu
Outside: Ravi


Exercise 8 — Closure

Question

Create multiplier(factor), return an inner function, and create double and triple.


Answer

def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))

Output:


20
30


Exercise 9 — Lambda

Question

Create a lambda function that calculates the square of a number.


Answer

square = lambda x: x * x

print(square(5))

Output:


25


Exercise 10 — Lambda + filter()

Question

Use filter() and lambda to find numbers greater than 20 from:


[10, 15, 20, 25, 30, 35]

Answer

numbers = [10, 15, 20, 25, 30, 35]

result = list(
    filter(lambda x: x > 20, numbers)
)

print(result)

Output:


[25, 30, 35]


Exercise 11 — Lambda + Sort

Question

Sort students by marks using lambda.


Answer

students = [
    ("Ravi", 85),
    ("Anu", 92),
    ("Kiran", 75)
]

students.sort(key=lambda student: student[1])

print(students)

Output:


[('Kiran', 75), ('Ravi', 85), ('Anu', 92)]


40. Interview Questions and Answers

1. What is a function?

A function is a reusable block of code designed to perform a specific task.


2. Why do we use functions?

For code reusability, organization, debugging, maintainability, and readability.


3. Difference between parameter and argument?

A parameter is a placeholder in the function definition. An argument is the actual value passed to the function.


4. What is return?

return sends a value back to the caller.


5. Difference between print() and return?

print() displays a value, while return sends a value back so it can be stored or used in further expressions.


6. What happens if a function does not return anything?

It returns None.


7. What are positional arguments?

Arguments matched to parameters based on their position.


8. What are keyword arguments?

Arguments specified using parameter names.


Example:


student_info(name="Ravi", age=21)

9. What are default parameters?

Parameters with fallback values.


def greet(name="Student"):
    print(name)

10. Why should required parameters come before default parameters?

Because a required parameter after a default parameter causes a syntax error.


11. What is *args?

It allows a function to receive an unknown number of positional arguments.


12. What type does *args store?

Tuple.


13. What is **kwargs?

It allows a function to receive an unknown number of keyword arguments.


14. What type does **kwargs store?

Dictionary.


15. Difference between *args and **kwargs?

*args handles positional arguments and stores them as a tuple.


**kwargs handles keyword arguments and stores them as a dictionary.


16. Can *args and **kwargs be used together?

Yes.


def example(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

17. What is argument unpacking?

Argument unpacking expands a collection into individual function arguments.


18. What does * do when calling a function?

It expands an iterable into positional arguments.


19. What does ** do when calling a function?

It expands a dictionary into keyword arguments.


20. What is scope?

Scope determines where a variable can be accessed.


21. What is local scope?

The scope of a variable created inside a function.


22. What is global scope?

The scope of a variable created at module level, outside functions.


23. What is the LEGB rule?

LEGB means:


Local → Enclosing → Global → Built-in

24. What is the global keyword?

It allows a function to assign to a global variable.


25. Why should excessive global variables be avoided?

Shared global state can cause unexpected changes and make debugging difficult.


26. What is a nested function?

A function defined inside another function.


27. What is a closure?

A closure is an inner function that remembers and uses variables from its enclosing scope even after the enclosing function has finished executing.


28. Why are closures useful?

They can create customized functions, maintain state, support data hiding patterns, callbacks, decorators, and functional programming techniques.


29. What is a lambda function?

A small anonymous function.


30. What is lambda syntax?

lambda arguments: expression

31. Difference between lambda and normal function?

A lambda is intended for small, simple expressions, while a normal def function is clearer for larger or more complex logic.


32. When should lambda be used?

When the function is small, simple, and often used once or locally, especially with sorting, filtering, or mapping.


33. What is map()?

map() applies a function to each item in an iterable.


34. What is filter()?

filter() keeps items for which a condition is True.


35. How is lambda commonly used with sorted()?

A lambda can be supplied as the key function.


students.sort(key=lambda student: student[1])

36. Can a function return another function?

Yes.


def outer():
    def inner():
        print("Hello")
    return inner

This pattern is used in closures.


37. How are functions useful in FastAPI applications?

FastAPI backends can organize application logic into functions such as:


create_user()
get_user()
update_user()
delete_user()
validate_email()
hash_password()
verify_password()
calculate_price()
calculate_tax()
generate_invoice()


41. Quick Revision Cheat Sheet

Concept	Remember
def	Creates a function
Function call	Executes a function
Parameter	Placeholder in function definition
Argument	Actual value passed
return	Sends a value back
Default parameter	Parameter with fallback value
Positional argument	Matched by position
Keyword argument	Matched by parameter name
*args	Variable number of positional arguments
**kwargs	Variable number of keyword arguments
*args type	Tuple
**kwargs type	Dictionary
Scope	Where a variable is accessible
Local	Current function scope
Enclosing	Outer function scope
Global	Module-level scope
Built-in	Python built-in names
LEGB	Local → Enclosing → Global → Built-in
Closure	Inner function remembers enclosing variables
Lambda	Small anonymous function
map()	Transform/apply function to items
filter()	Select items
sorted(key=...)	Sort using a key function


42. Final Mental Model

INPUT
  ↓
FUNCTION
  ↓
PROCESS
  ↓
OUTPUT

normal parameters
       ↓
default parameters
       ↓
*args
       ↓
**kwargs

LEGB
Local → Enclosing → Global → Built-in

Outer function
      ↓
Variable
      ↓
Inner function
      ↓
Remembers variable
      ↓
Closure

lambda x: x * 2
        ↓
Small one-expression function


43. Common Beginner Mistakes


Defining a function but forgetting to call it.

Confusing parameters and arguments.

Forgetting return when a result is needed.

Confusing *args and **kwargs.

Forgetting that *args is a tuple.

Forgetting that **kwargs is a dictionary.

Creating too many global variables.

Using global when passing and returning values would be cleaner.

Making lambda expressions too complicated.

Forgetting that a closure retains access to enclosing variables.



44. GitHub Structure

Recommended repository structure:


Day_6_Functions_Arguments_Scope_Closures_Lambda/
│
├── README.md
└── day_6_functions.py


45. How to Run

Open the terminal inside the folder and run:


python day_6_functions.py

If your system uses python3:


python3 day_6_functions.py


46. GitHub Push Commands

git init
git add .
git commit -m "Add Day 6 Functions Arguments Scope Closures Lambda"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main

Replace:


YOUR_GITHUB_REPOSITORY_URL

with your GitHub repository URL.



Learning Flow

Functions
   ↓
Parameters & Arguments
   ↓
Return
   ↓
Positional / Keyword Arguments
   ↓
Default Parameters
   ↓
*args / **kwargs
   ↓
Argument Unpacking
   ↓
Scope
   ↓
LEGB
   ↓
Nested Functions
   ↓
Closures
   ↓
Lambda
   ↓
map / filter / sorted

These concepts form an important foundation for later topics such as modules, packages, exception handling, OOP, decorators, and FastAPI.0