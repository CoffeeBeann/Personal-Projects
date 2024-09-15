# Ian Coffey
# Class Test.py
# To Test Classes In Python


class Contatcs:
        def __init__(object,name,phone): # Default Constructor
                object.name = name
                object.phone = phone
		
        def Display_Name(object,name):
                return(object.name)
                
        def Display_Phone(object,phone):
                return(object.phone)

User_Contact = input("Enter Name: ")
	
	
