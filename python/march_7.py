import time
# Ask user to input a char. into a var.
#character = input("Enter any character: ")
# Ask user to enter a num. put it into a var.
#num_string = input("Enter a number: ")
# Convert num. to an int.
#num_int = int(num_string)
# print char. num. times
# print(character)
# print(num_int)]
#sentence = ""
#for _num_int in range(num_int):
#    sentence = sentence + character
#    print(sentence)

# Ask user for number, act like counter-downer from number

num_string = input("Type a number: ")
num_int = int(num_string)

forever = 1
while forever != 0:
    print(num_int)
    num_int = num_int -1
#    time.sleep(5)
    if num_int == 0:
        forever = 0