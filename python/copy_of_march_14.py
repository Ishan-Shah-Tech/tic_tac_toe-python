# input a word and print it one character at a time

word = input("Please enter a word: ")
print("The word you entered is: " + word)

counter = len(word) # "how far we are in the printing"
total_word_length = len(word)

while counter > total_word_length:
    print("The counter is: " + str(counter))
    print("Counter = index")
    print("The word[counter] is: " + word[counter])
    counter = counter - 1
    
# word = dog
# counter is set to 0
# we enter while loop
# during loop 1:
#     we increase counter by 1, counter now equals 1
#     we print counter
#     we exit loop
# We enter loop again, because counter is less than total_word_length:
#     we increase coutner by 1 again, counter now equals 2
#     we print counter
#     we exit loop
# we enter loop again, because counter is still less than total_word_length which is 3:
#     we increase counter by 1 again, counter now equals 3
#     we print counter
#     we exit loop
# we dont enter loop again

# print(total_word_length)\]

# print(word[7])

# caterpillar

# what is the total length of caterpillar 
# what is the last index of caterpillar
print(word)