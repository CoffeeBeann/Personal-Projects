from os import system
from time import sleep
def main():
    def cls():
        system('cls')
    def gen():
        cls()
        print('\n'*2)
        num = input('Enter Password: ')
        n = 0
        x = True
        while x:
            if int(n) == int(num):
                x = False
            else:
                pass
            print(str(n),end=' ')
            n += 1
        print('\n'*2)
        action = input('Press Enter To Continue: ')
        if action == ' ' or action != ' ':
            main()
    gen()
main()
            
            
