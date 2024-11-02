import time
def intro():
    print("Forever will you be mine!")
    time.sleep(3)
    print("*snore*")
    time.sleep(1)
    print("Let's go!")
    time.sleep(1)
    print("Be quick!")
    time.sleep(3)
    print("Whoa!")
    time.sleep(2)


def wrong_answer():
    print("\nWrong answer.")
    time.sleep(1)
    print("\nYou are going to have to restart the game.")
    time.sleep(1)
    print("\nTo help you, I will give you the answer.")
    time.sleep(1)
    print("\n144.")
    time.sleep(1)
    print("\nCopy and paste the following to get into the game:")
    time.sleep(1)
    print("\ncd python")
    time.sleep(1)
    print("\nThen type:")
    time.sleep(1)
    print("\npython game.py")
    time.sleep(1)
    print("\nBye now.")

def corect_answer():
    print("Correct!")
    print("Let's get going, we don't have much time until the giant finds out we escaped.")
    time.sleep(1)
    print("Oh gosh, we have to go to the question bridge to escape.")
    time.sleep(1)
    print("Hey you!")
    time.sleep(1)
    print("Answer this question if you want to escape.")
    time.sleep(1)


intro()

print("What is 12 x 12?")
question1 = input("")

if question1 != "144":
    wrong_answer()
   

if question1 == "144":
    corect_answer()

    print("Solve for n:")
    print("\n5 - n = 2")
    question2 = input("n = ")
    if question2 != "3":
        print("\nWrong answer.")
    time.sleep(1)
    print("\nYou are going to have to restart the game.")
    time.sleep(1)
    print("\nTo help you, I will give you the answer.")
    time.sleep(1)
    print("\n3.")
    time.sleep(1)
    print("\nCopy and paste the following to get into the game:")
    time.sleep(1)
    print("\ncd python")
    time.sleep(1)
    print("\nThen type:")
    time.sleep(1)
    print("\npython game.py")
    time.sleep(1)
    print("\nBye now.")
if question2 == "3":
    print("Correct!")