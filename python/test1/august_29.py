import time
counter = 0


forever = 0
while forever != 1:
    time.sleep(1)
    print("Want Free robux or V-bucks? Visit Blox.get!")
    counter = counter + 1

    if counter == 10:
        forever = 1