number_as_string = input("Enter number: ")
number = int(number_as_string)
if number > 0:
    print("Great job! I will tell the god of heaven to send you there when you die.")
if number < 0:
    print("Sorry, This number will break your laptop.")
if number == 0:
    print("Great job! you found the secret number!")
    number = number + 5
    print("The new number is " + str(number))
if number > 5:
    print("Your number is greater than 5!")
if number < -5:
    print("Oh, and I forgot, your whole house is going to bun in 24 hours no matter what material it is made out of.")