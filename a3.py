# 8


def introduce(name, age=None):
    if age is not None:
        print("My name is", name + ".", "I am", age, "years old.")
    else:
        print("My name is", name + ".", "My age is secret.")

# Function calls
introduce("John", 20)
introduce("John")



# 9


# Function definition
def drop_minimum(*args):
    numbers = list(args)      
    minimum = min(numbers)    
    numbers.remove(minimum)   
    return numbers

# Function call
result = drop_minimum(5, -2, 8, 4, -5, 7, 10)
print(result)


# 10

# Function to find the maximum
def find_max(a, b, c):
    return max(a, b, c)

# Main function
def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    print(find_max(x, y, z))

# Call main function
main()




# 11

add = lambda a, b: a + b

print(add(10, 20))




# 12

fahrenheit = lambda c: (c * 9 / 5) + 32

print(fahrenheit(25.0))





# 13
try:
    with open("student.txt", "x") as file:
        file.write("Python is easy to learn.\n")
        file.write("File handling is important.\n")
        file.write("Practice makes perfect.\n")

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")

except Exception as e:
    print("Error:", e)




# 14
# a
with open("student.txt", "r") as file:
    content = file.read()

print(content)

# b

with open("student.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    print(f"Line {i}: {line.strip()}")






# 15

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total words:", len(words))




# 16

with open("student.txt", "a") as file:
    file.write("Python file handling becomes simple with practice.\n")

print("Line added successfully.")






# 17

numbers = [7, 4, 0, -2, 3]

print("List:", numbers)

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    print("IndexError: Invalid index.")

except Exception as e:
    print("Error:", e)






# 18


# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# main.py
import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))