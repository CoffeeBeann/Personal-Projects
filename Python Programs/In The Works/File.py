import os
import logging
from contextlib import contextmanager
import time

def main():
    def log(file):
        logging.basicConfig(filename=file,level=logging.info,
                            format = '%(asctime)s:%(levelname)s:%(message)s')
        os.system('cls')
        open_GUI()
        
    def open_file_write(file):
        f = open(file)
        with open(file,'w') as f:
            f.write(input(": "))
            f.close()
        os.system('cls')
        open_GUI()
        
    def open_file_read(file):
        f = open(file)
        with open(file,'r').read() as f:
            print(file)
            f.close()
        os.system('cls')
        open_GUI()
        
    def Error():
        os.system('cls')
        print('\n'*5)
        print("     Invalid Syntax")
        time.sleep(2)
        open_GUI()
            
    def open_GUI():
        global counter
        os.system('cls')
        print('='*100)
        print('\n'*5)
        print('    File Manipulation')
        print('\n'*5)
        print('='*100)
        counter = 0
        num = ''
        for i in range(0,3):
            counter += 1
            if counter == 1:
                num = '1'
                print("Enter[" + num + '] : Log')
            elif counter == 2:
                num = '2'
                print("Enter[" + num + '] : Read')
            elif counter == 3:
                num = '3'
                print("Enter[" + num + '] : Write')
            else:
                pass
        print()
    def input_func():
        choice = input(': ')
        if int(choice) == 1:
            os.system('cls')
            print('='*100)
            print('\n'*5)
            print('     Enter File Name:')
            print('\n'*5)
            print('='*100)
            file = input(': ')
            log(file)
        elif int(choice) == 2:
            os.system('cls')
            print('='*100)
            print('\n'*5)
            print('     Enter File Name:')
            print('\n'*5)
            print('='*100)
            file = input(': ')
            open_file_read(file)
        elif int(choice) == 3:
            os.system('cls')
            print('='*100)
            print('\n'*5)
            print('     Enter File Name:')
            print('\n'*5)
            print('='*100)
            file = input(': ')
            open_file_write(file)
        else:
            Error()
    while True:
        open_GUI()
        input_func()
while True:
    main()

            
             
            
        
            
            
            
        


            
            
            
            

        
