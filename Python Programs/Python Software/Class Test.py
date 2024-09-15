# Ian Coffey
# Class Test.py
# To Test Classes In Python

class Contacts:
    def __init__(object,name,phone): # Default Constructor
        object.name = name
        object.phone = phone

    def Display_Name(name): # Display Name
        print("The Name Of This Contact Is: " + str(name))

    def Display_Phone(phone): # Display Phone
        print("The Phone # Of This Contact Is: " + str(phone))


Contacts('Ian', '719-426-8426')

Contacts.Display_Name('ian')
        
