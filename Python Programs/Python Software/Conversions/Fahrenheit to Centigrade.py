# Fahrenheit To Centigrade/Ian Coffey/

import time
import os

try:
    def main():
        os.system('cls')
        print()
        print("Fahrenheit To Centigrade Calculator.")
        while True:
             print()
             temp= input("Enter Degrees: ")
             # Conversion (Fahrenheit To Centigrade)
             conv1 = int(temp)-32
             conv2 = int(conv1)/1.8
             temp = int(conv2)
             # Display
             print()
             print(str(temp) + " Degrees Celsius")
    while True:
        main()

except:
    # Invalid Inputs
    print()
    print("Error")
    time.sleep(3)
    main()



    
