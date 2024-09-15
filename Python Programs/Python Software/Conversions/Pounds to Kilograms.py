# Pounds To Kilograms/Ian Coffey/

import time
import os

try:
    def main():
        os.system('cls')
        print()
        print("Pounds To Kilograms Calculator")
        print()
        while True:
            lb = input("Enter Weight: ")
             # Conversion (Pounds To Kilograms)
            lb = int(lb)*0.45
             # Display
            print()
            print(str(int(lb)) + " Kilograms")
            print()
    while True:
        main()
        
except:
    # For Invalid Inputs(Ex: "vifdolodj")
    print()
    print("Error")
    print()
    time.sleep(3)
    main()
    

        
