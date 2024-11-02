def greet(first_name, last_name):
    print(f"hi, {first_name} {last_name}")

def add(num_one, num_two):
    num_one = int(num_one)
    num_two = int(num_two)
    total = num_one + num_two
    return str(total)

def subtract(num_one, num_two):
    num_one = int(num_one)
    num_two = int(num_two)
    total = num_one - num_two
    return str(total)

def multiply(num_one, num_two):
    num_one = int(num_one)
    num_two = int(num_two)
    total = num_one * num_two
    return str(total)

def divide(num_one, num_two):
    num_one = float(num_one)
    num_two = float(num_two)
    total = num_one / num_two
    return str(total)

def validate_inputs(num_one, num_two):
    if not num_one or not num_two:
        print("\nPlease enter a valid number.")
        return False
    return True

first_name = input("Enter your first name")
last_name = input("Enter your last name")
greet(first_name, last_name)

forever = 1
while forever != 0:
    answer = input("\nWhat would you like to do? ")
    if answer == "quit":
        forever = 0
    elif answer == "add"