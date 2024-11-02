from dataclasses import replace


def validate_input(input_word):
    while len(input_word) > 1:
        print("\nInvalid value. Enter letter again.")
        input_word = input("Enter a letter: ")





word = input("Enter a word: ")
second_input = input("Enter a letter: ")
# second_input_length = len(second_input)
validate_input(second_input)

# while second_input_length > 1:
    # print("\nInvalid value. Enter letter again.")
    # second_input = input("Enter a letter: ")
    # second_input_length = len(second_input)

third_input = input("Enter another letter: ")
validate_input(third_input)

# character_in_word = len(word)
# print(character_in_word)
count_of_second_input = 0
    
word.replace(second_input, third_input)


print("There are " + str(count_of_second_input) + " " + second_input + "'s in the word " + word + ".")