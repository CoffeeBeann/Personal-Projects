from os import system
from time import sleep

def main():
    def cls():
        system('cls')
    def gen():
        n = '9'
        check = True
        cls()
        print('\n'*2)
        d = input('# Of Digits In Password: ')
        print('\n'*2)
        password = input('Enter Password: ')
        for x in range(0,int(d)):
            n = str(n) + '9'
        while check:
            if int(n) == int(password):
                check = False
            else:
                pass
            n = int(n)
            n -= 1
            print(int(n),end = ' ')
        print('\n'*2)
        action = input('Press Enter To Continue: ')
        if action == ' ' or action != ' ':
            main()
    gen()
main()
        
            
        
