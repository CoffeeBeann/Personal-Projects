#Guessing Game/Ian Coffey/

import random
import time

AInum = random.randint(0,1000)

while True:
    print()
    USnum = input("Guess A Number: ")
    if int(USnum) > AInum:
        print()
        print("Guess Lower.")
        print()
    elif int(USnum) < AInum:
        print()
        print("Guess Higher.")
        print()
    else:
        print()
        print("YOU ARE CORRECT!!")
        print()
        time.sleep(3)
        break
