import subprocess
from contextlib import contextmanager

def main():
    def over_write(file):
        f = open(file)
        with open(file, 'r+') as f:
            for i in range(0,100):
                f.write('\n' * 1000)
        f.close()
        if f.closed == True:
            pass
        else:
            subprocess.call('cls', shell =True)
            print('\n'*5)
            print("     ERROR: f.closed != True")
            print()
            
    def open_GUI():
        subprocess.call('cls', shell =True)
        print('='*100)
        print('\n' * 5)
        print('     : Enter File To Overwrite :')
        print('\n' * 5)
        print('='*100)
    def close_GUI():
        from time import sleep
        subprocess.call('cls', shell =True)
        print('='*100)
        print('\n' * 5)
        print('     : Overwrite Complete :')
        print('\n' * 5)
        print('='*100)
        choice = input("Press Any Key To Continue: ")
        if choice == '' or choice != '':
            subprocess.call('cls', shell =True)
            main()
    open_GUI()
    filename = input(": ")
    over_write(filename)
    close_GUI()
   
main()

        
        

        
    
    
    
    
    
    

