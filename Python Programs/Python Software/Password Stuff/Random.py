from os import system
from random import randrange

def main():
    def cls():
        system('cls')
    def gen():
        cls()
        num = '9'
        print('\n'*2)
        d = input('# Of Digits In Password: ')
        print('\n')
        password = input('Enter Password: ')
        cls()
        for x in range(0,int(d)-1):
            num = str(num) + '9'
        check = True
        while check:
            if int(num) == int(password):
                check = False
            else:
                pass
            print(randrange(0,int(num)),end = ' ')
        print('\n'*2)
        action = input('Press Enter To Continue: ')
        if action == ' ' or action != ' ':
            main()
        else:
            pass
    gen()
main()
            
        
        
