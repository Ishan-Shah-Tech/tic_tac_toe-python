COUNTER = 1
numbers = []

def add(num_one, num_two):
    num_one = int(num_one)
    num_two = int(num_two)
    total = num_one + num_two
    return str(total)

def check_user_input(user_input):
    if user_input == "1":
        num_one = input("Please enter the first number you would like to calculate. ")
        num_two = input("Please enter the second number you would like to calculate. ")
        print("The total is " + add(num_one, num_two))
    if user_input == "2":
        numbers.append(num_one)
        numbers.append(num_two)
        print(numbers)
    if user_input == "3":
        print("Not implemented")
    if user_input == "4":
        COUNTER = 0

    else:
        print("Enter a valid option please.")
        print("\n")

def ask_menu_questions():
    print("Menu items: ")
    print("1 - to add numbers: ")
    print("2 - to view numbers added: ")
    print("3 - to check if number exists: ")
    print("4 - to quit: \n") # work on first

while COUNTER > 0:
    ask_menu_questions()
    user_input = input("Please enter a menu option: ")
    check_user_input(user_input)
else:
    end_game = "true"