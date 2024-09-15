
from os import system
def main():
    def cls():
        system('cls')
    cls()
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    print('\n'*2)
    name = input('Enter Word: ')
    name = list(name)
    for i in range(0,len(name)):
        if name[i] in vowels:
            name[i] = '*'
        else:
            pass
    print('\n'*2)
    name = ''.join(name)
    print(name)
    print('\n'*2)
    action = input('Press Enter To Continue: ')
    if action == ' ' or action != ' ':
        main()
if __name__ == '__main__':main()
    
