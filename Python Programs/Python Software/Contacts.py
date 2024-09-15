try:
    import os
    import logging
    class Contact:
        def __init__(self,fname,lname,phone):
            self.fname = fname
            self.lname = lname
            self.phone = phone
            self.email = fname + "." + lname + "@aol.com"
    def main():
        while True:
            print('''
            ================================================================================
            Contacts
            --------------------------------------------------------------------------------
            Enter New Contact By Filling In The Information Below.
            ================================================================================
            ''')
            first_name = input("             First Name: ")
            last_name = input("             Last Name: ")
            phone = input("             Phone Number: ")
            print('''
            ================================================================================
			Thank You : This Contact Has Been Saved In A Text File.
            ================================================================================
            ''')
            i = input("            Press Enter To Continue: ")
            if str(i) == "" or str(i) != "":
                os.system('cls')
            else:
                pass
            contact_1 = Contact(first_name,last_name,phone)
            logging.basicConfig(filename='Contacts.log',level=logging.INFO,
                    format = '%(asctime)s:%(levelname)s:%(message)s')
            logging.info( ' ' + contact_1.fname + ' ' + contact_1.lname + ' : ' + contact_1.phone)
    while True:
        main()
except:
    pass
