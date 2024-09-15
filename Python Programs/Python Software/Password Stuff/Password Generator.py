from os import system
from time import sleep
from random import randrange
global n
n = 0
def main():
    def cls():
        system('cls')
    def open_gui():
        cls()
        print('\n'*2)
        print(' '*5 + '='*50)
        print('\n'*2)
        print(' '*20 + 'Password Generator')
        print('\n'*2)
        print(' '*5 + '='*50)
        print('\n')
        gen()
    def gen():
        global n
        n = input('# Of Digits In Password: ')
        print('\n')
        for x in range(0,int(n)):
            print(str(randrange(0,9)),end= ' ')
        print('\n'*2)
        action = input('Press Enter To Continue: ')
        if action == '':
            main()
        elif action != '':
            main()
        else:
            pass
    open_gui()
main()
            
        
