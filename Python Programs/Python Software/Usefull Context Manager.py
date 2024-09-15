from contextlib import contextmanager
import os
global counter
global dot
import time
counter = 0
dot = ''


def input_animation():
    os.system('cls')
    global counter
    global dot
    print('='*50)
    print('\n' * 5)
    print("     Enter File Name: ")
    print('\n' * 5)
    print('='*50)
    file = input(': ')
    for i in range(0,9):
        os.system('cls')
        counter += 1
        if counter == 1:
            dot = '.'
        elif counter == 2:
            dot = '..'
        elif counter == 3:
            dot = '...'
        elif counter == 4:
            counter = 1
            dot = '.'
        else:
            pass
        print('='*60)
        print('\n'*5)
        print('     Aquiring File' + str(dot))
        print('\n'*5)
        print('='*60)
        time.sleep(float(0.5))

    os.system('cls')
    open_file(file)
          
def open_file(filename):
    f = open(filename)
    with open(filename, 'r+') as f:
        print('Enter Text : WARNING : Any Input Will Overwrite Existing Text In File')
        print('\n')
        f.write('\n')
        f.write(input(': '))
        f.close()
    os.system('cls')
    print('='*60)
    print('\n'*5)
    print('     Edit Complete')
    print('\n'*5)
    print('='*60)
    time.sleep(2)
    input_animation()
while True:
    input_animation()
