# Ian Coffey
# Employee.py

# Import Libraries
from string import Template

class Employee(object, name, pay, phone):
    
    object.name = name
    object.pay = pay
    object.phone = phone

class temp(Template):
    delimiter = '</'

def Main():

    employee = []

    # Initialize Employees
    employee.append(dict(name = 'Ian', pay = "12000", phone = "7194268426"))
    
    root = temp("</{name} : </{pay} : </{phone}")

    pay = 0
    print("Employee Info: ")

    for index in employee:
        print(root.substitute(index))
        total += index["pay"]
        
    print("Total Emp Cost: " + str(pay))

if __name__ == "__main__":
    Main()
    
    
