# Mile To Kilometer Calculator/Ian Coffey/

import time
import os

try:
    def main():
        os.system('cls')
        print()
        print("Mile To Kilometer Calculator")
        print()
        while True:
            print()
            miles = input("Enter Distance: ")
            print()
            if int(miles) == 1:
                print("Error")
                print()
                time.sleep(3)
                main()
            # Conversion (Miles To Kilometers)
            kilo = int(miles)*1.609
            # Display
            print(str(int(kilo)) + " Kilometers")
    while True:
        main()

except:
    print()
    print("Error")
    print()
    time.sleep(2)
    main()
    

