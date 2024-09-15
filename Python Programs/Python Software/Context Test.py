import time
import os
global appendInfo
global file
file = ''
appendInfo = ''

def main():
    def open_p():
        global file
        os.system('cls')
        print('='*50)
        print('\n'*5)
        print('    Enter File Name :')
        print('\n'*5)
        print('='*50)
        file = input(': ')
        file_input()
        
        
    def open_file(filename):
        global appendInfo
        global file
        f = open(filename)
        with open(filename, 'r+') as f:
            f.write('\n')
            f.write(appendInfo)
            f.close()

    def file_input():
        global file
        global appendInfo
        os.system('cls')
        print('Enter Text')
        print()
        appendInfo = input(': ')
        open_file(file)
    while True:
        open_p()
main()
        
            
            
