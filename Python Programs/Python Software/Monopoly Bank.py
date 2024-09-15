import time
import os

def main():
    def one_player():
        def add():
            global money
            os.system('cls')
            print('\n'*5)
            edit_choice = input(' Value : ')
            money = int(money) + int(edit_choice)
            balance_1()
        def sub():
            global money
            os.system('cls')
            print('\n'*5)
            edit_choice = input(' Value : ')
            money = int(money) - int(edit_choice)
            balance_1()
        def balance_1():
            global player_name
            global money
            os.system('cls')
            print('\n'*5)
            print()
            print('     ' + '='*100)
            print(' '*50 + str(player_name) +  "\'s Balance: " + str(money))
            print('     ' + '='*100)
            print('\n'*2)
            print('Enter [1] = Add')
            print('Enter [2] = Subtract')
            print()
            if int(money) < 1:
                os.system('cls')
                print('\n'*5)
                print(' '*5 + 'YOU ARE BANKRUPT : YOU LOSE')
                print()
                back = input('Press Enter To Continue: ')
                if str(back) == '' or str(back) != '':
                    main()
                else:
                    pass
            balance_edit = input(': ')
            if int(balance_edit) == 1:
                add()
            elif int(balance_edit) == 2:
                sub()
            else:
                pass
        global money
        global player_name
        money = 0
        player_name = ''
        os.system('cls')
        print('\n'*5)
        print('     ' + '='*100)
        print('     ' + '-'*45 + ' Monopoly ' + '='*45)
        print('     ' + '='*100)
        print('\n'*3)
        print('Enter Player Name')
        player_name = input(': ')
        os.system('cls')
        print('\n'*5)
        print('     ' + '='*100)
        print('     ' + '-'*45 + ' Monopoly ' + '='*45)
        print('     ' + '='*100)
        print('\n'*3)
        print('Enter Starting Amount Of Money')
        money = input(': ')
        balance_1()
        
    def two_player():
        def balance_2():
            os.system('cls')
            global money_1
            global money_2
            
            def sub_1_value():
                global money_1
                os.system('cls')
                print('\n'*5)
                edit_choice = input(' Value : ')
                money_1 = int(money_1) - int(edit_choice)
                balance_2()
                
            def sub_2_value():
                global money_2
                os.system('cls')
                print('\n'*5)
                edit_choice = input(' Value : ')
                money_2 = int(money_2) - int(edit_choice)
                balance_2()
                
            def sub_choice():
                os.system('cls')
                print('\n'*5)
                print('     ' + '='*100)
                print(' '*50 + '(Player 1 )  ' + str(player_name_1) +  "\'s Balance: " + str(money_1))
                print('     ' + '='*100)
                print('\n'*2)
                print('     ' + '='*100)
                print(' '*50 + '(Player 2 )  ' + str(player_name_2) +  "\'s Balance: " + str(money_2))
                print('     ' + '='*100)
                print('\n'*2)
                print('Player 1 or 2 ?')
                sub_choice = input(": ")
                if int(sub_choice) == 1:
                    sub_1_value()
                if int(sub_choice) == 2:
                    sub_2_value()
            
            def add_1_value():
                global money_1
                os.system('cls')
                print('\n'*5)
                edit_choice = input(' Value : ')
                money_1 = int(money_1) + int(edit_choice)
                balance_2()
            def add_2_value():
                global money_2
                os.system('cls')
                print('\n'*5)
                edit_choice = input(' Value : ')
                money_2 = int(money_2) + int(edit_choice)
                balance_2()

            def add_choice():
                os.system('cls')
                print('\n'*5)
                print('     ' + '='*100)
                print(' '*50 + '(Player 1 )  ' + str(player_name_1) +  "\'s Balance: " + str(money_1))
                print('     ' + '='*100)
                print('\n'*2)
                print('     ' + '='*100)
                print(' '*50 + '(Player 2 )  ' + str(player_name_2) +  "\'s Balance: " + str(money_2))
                print('     ' + '='*100)
                print('\n'*2)
                print('Player 1 or 2 ?')
                add_choice = input(": ")
                if int(add_choice) == 1:
                    add_1_value()
                if int(add_choice) == 2:
                    add_2_value()
                
                    
            print('\n'*5)
            print('     ' + '='*100)
            print(' '*50 + '(Player 1 )  ' + str(player_name_1) +  "\'s Balance: " + str(money_1))
            print('     ' + '='*100)
            print('\n'*2)
            print('     ' + '='*100)
            print(' '*50 + '(Player 2 )  ' + str(player_name_2) +  "\'s Balance: " + str(money_2))
            print('     ' + '='*100)
            print('\n'*2)
            print('Enter [1] = Add')
            print('Enter [2] = Subtract')
            print('\n'*2)
            choice = input(": ")
            if int(choice) == 1:
                add_choice()
            elif int(choice) == 2:
                sub_choice()

                
        global money_1
        global money_2
        global player_name_1
        global player_name_2

        money_1 = 0
        money_2 = 0
        player_name_1 = ''
        player_name_1 = ''

        os.system('cls')
        print('\n'*5)
        print('     ' + '='*100)
        print('     ' + '-'*45 + ' Monopoly ' + '='*45)
        print('     ' + '='*100)
        print('\n'*3)
        print('Enter Player 1 Name')
        player_name_1 = input(': ')

        os.system('cls')
        print('\n'*5)
        print('     ' + '='*100)
        print('     ' + '-'*45 + ' Monopoly ' + '='*45)
        print('     ' + '='*100)
        print('\n'*3)
        print('Enter Player 2 Name')
        player_name_2 = input(': ')

        os.system('cls')
        print('\n'*5)
        print('     ' + '='*100)
        print('     ' + '-'*45 + ' Monopoly ' + '='*45)
        print('     ' + '='*100)
        print('\n'*3)
        print('Enter Starting Amount Of Money')
        money_1 = input(': ')
        money_2 = money_1

        balance_2()
 
    os.system('cls')
    print('\n'*5)
    print('     ' + '='*100)
    print('     ' + '-'*45 + ' Monopoly ' + '='*45)
    print('     ' + '='*100)
    print('\n'*3)
    print('Enter # Of Players | Max 2')
    player_num = input(': ')
    if int(player_num) == 1:
        one_player()
    elif int(player_num) == 2:
        two_player()
    else:
        pass
main()
