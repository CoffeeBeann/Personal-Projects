try:
    import os
    import time

    def read_file(filename, mode):
        readInfo = open(filename, mode).read()
        os.system('cls')
        print(readInfo)
        while True:
            pass

    def input_p():
        open_p()
        file = input(": ")
        read_file(file, 'r')
        
    def open_p():
        os.system('cls')
        print('='*60)
        print('\n'*5)
        print('     Enter File Name:')
        print('\n'*5)
        print('='*60)
    
    while True:
        input_p()
except:
    os.system('cls')
    print('='*60)
    print('\n'*5)
    print('     File Does Not Exist and/or Error Has Occured')
    print('\n'*5)
    print('='*60)
    time.sleep(3)
    input_p()

    
    
