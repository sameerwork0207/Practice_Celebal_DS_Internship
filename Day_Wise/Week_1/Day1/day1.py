print("Day 1 Python Basics")

# Variables and data types
name = "Sameer"
age = 21
height = 5.9
is_intern = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Intern:", is_intern)

# Basic arithmetic
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Conditional statements
score = 78

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    print("Grade: C")

# Lists and loops
fruits = ["apple", "banana", "mango"]
print("First fruit:", fruits[0])

for fruit in fruits:
    print("Fruit:", fruit)

# Dictionary
student = {
    "name": "Sameer",
    "department": "AI/ML",
    "year": 2026,
}

print("Student name:", student["name"])
print("Student department:", student["department"])

# Function
def greet(user_name):
    return f"Hello, {user_name}!"


print(greet("Sameer"))


def square(number):
    return number * number


for number in range(1, 6):
    print(f"Square of {number} is {square(number)}")
