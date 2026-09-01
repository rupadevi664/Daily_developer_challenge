# Day 3 — Python Functions, Strings & Problem Solving

# 1. Character Frequency

def character_frequency(text):
    frequency = {}

    for char in text:
        if char == " ":
            continue

        frequency[char] = frequency.get(char, 0) + 1

    return frequency


print("Character Frequency:")
print(character_frequency("hello"))
print(character_frequency("programming"))
print(character_frequency("hello world"))


# Bonus: Most Frequently Occurring Character

def most_frequent_character(text):
    frequency = {}

    for char in text:
        if char == " ":
            continue

        frequency[char] = frequency.get(char, 0) + 1

    if not frequency:
        return None

    return max(frequency, key=frequency.get)


print("\nMost Frequent Character:")
print(most_frequent_character("success"))
print(most_frequent_character("programming"))
print(most_frequent_character("hello"))


# 2. Functions — Parameter and Argument

def greet(name):
    print("Hello", name)


greet("Ravi")


# Return vs Print

def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


add_print(10, 20)

result = add_return(10, 20)
print(result)


# Interview Follow-up: Function without return

def test():
    x = 10


result = test()
print("Function without return:", result)


# 3. Debugging Challenge — Corrected Function

def calculate_total(price, quantity):
    total = price * quantity
    return total


result = calculate_total(100, 3)
discount = result * 0.10

print("\nCalculate Total:")
print(result)
print("Discount:", discount)


# Bonus — Return price, quantity and total

def calculate_total_details(price, quantity):
    total = price * quantity

    return {
        "price": price,
        "quantity": quantity,
        "total": total
    }


details = calculate_total_details(100, 3)

print("\nCalculation Details:")
print(details)
print("Total:", details["total"])


# 4. Password Validator

def validate_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


print("\nPassword Validator:")
passwords = [
    "Hello123",
    "hello",
    "HELLO123",
    "hello123",
    "HelloWorld"
]

for password in passwords:
    if validate_password(password):
        print(password, "-> Valid Password")
    else:
        print(password, "-> Invalid Password")


# Bonus — Password Validator with Special Character

def validate_password_with_special(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "@#$%!"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    return has_upper and has_lower and has_digit and has_special


print("\nPassword Validator With Special Character:")
print(validate_password_with_special("Hello123!"))
print(validate_password_with_special("Hello123"))
print(validate_password_with_special("hello"))


# 5. Function Returning Multiple Values

def calculate(a, b):
    return a + b, a - b, a * b


addition, subtraction, multiplication = calculate(10, 5)

print("\nMultiple Return Values:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)


# Local and Global Variables

name = "Rupa"  # Global variable


def show_variables():
    message = "Hello"  # Local variable

    print(name)
    print(message)


print("\nLocal and Global Variables:")
show_variables()


# Default Parameter

def calculate(a, b=10):
    return a + b


print("\nDefault Parameter:")
print(calculate(5))
print(calculate(5, 20))


# __name__ == "__main__"

def run_example():
    print("\nMain block executed.")


if __name__ == "__main__":
    run_example()


# 6. Mentor Challenge
# Treat "Hello" like "hello", ignore spaces and special characters.

def character_frequency_clean(text):
    frequency = {}

    for char in text.lower():
        if not char.isalpha():
            continue

        frequency[char] = frequency.get(char, 0) + 1

    return frequency


print("\nClean Character Frequency:")
print(character_frequency_clean("Hello"))
print(character_frequency_clean("Hello World!"))
print(character_frequency_clean("Python, Python!"))