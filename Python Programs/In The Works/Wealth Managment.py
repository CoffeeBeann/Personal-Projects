# Ian Coffey
# Wealth Managment.py
# To Manage A Users Wealth

# Import Libraries
from tkinter import *
import time
import tkinter.messagebox

# Canvas Setup
root = Tk()
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(width = 400, height = 400)
canvas.pack()
root.title('Wealth Managment')

# Establish Global Vars
global UserName
global Annual_Income
global Savings

# Establish Start Control
def Start():
    Main()
    
# Start Screen Setup
Background = canvas.create_rectangle(-10,-10,500,500, fill = 'grey')
Start_Box = canvas.create_rectangle(100,150,300,250, fill = 'white')
Wealth_Managment = canvas.create_text(200,125, fill = 'blue', text = 'Wealth Managment', font = ("arial", 20))
Developed_By = canvas.create_text(200,175, text = 'Developed By: Ian Coffey', font = ("arial", 12))
Start = Button(root, text = "Begin", fg = 'blue', borderwidth = 2, relief = 'raised', command = Start)
Start.place(x = 180, y = 200)

# Add Border
Left_Side = canvas.create_rectangle(0,0,25,500, fill = 'black')
Right_Side = canvas.create_rectangle(380,0,500,500, fill = 'black')
Top_Side = canvas.create_rectangle(0,0,400,25, fill = 'black')
Bottom_Side = canvas.create_rectangle(0,500,400,375, fill = 'black')

# Initialize Corner Menu

def Quit(): # Quit Function

    question = tkinter.messagebox.askquestion("Warning", "Are You Sure You Would Like To Quit?") # Establish Question

    if question == "yes":
        exit()
    else:
        if question == "no":
           pass

# Establish Sub Menus
Mainmenu = Menu(root)
root.configure(menu = Mainmenu)
subMenu = Menu(Mainmenu)
Mainmenu.add_cascade(label = "Menu",menu = subMenu)
subMenu.add_command(label = "Quit", command = Quit)

def Main():

    def Buffer():

        def Savings():

            def SaveBalance_Expense_Prompt():

                def Add():

                    # Save Entry Into Vars
                    ExpenseName_Input = ExpenseName_Entry.get()
                    ExpenseCost_Input = ExpenseCost_Entry.get()

                    # Append To Expense List
                    Expenses_Name.append(str(ExpenseName_Input))
                    Expenses_Cost.append(str(ExpenseCost_Input))

                    ExpenseName_Entry.delete(0, END)
                    ExpenseCost_Entry.insert(0, "")

                    ExpenseCost_Entry.delete(0, END)
                    ExpenseName_Entry.insert(0, "")
                    

                def Next():

                    def Managment():

                        pass

                        # Current Window Widgets
                        Next_Page.place(x = 1000, y = 1000)
                        NameListBox_Label.place(x = 1000, y = 1000)
                        CostListBox_Label.place(x = 1000, y = 1000)
                        Name_ListBox.place(x = 1000, y = 1000)
                        Cost_ListBox.place(x = 1000, y = 1000)

                        # Create New Window Widgets
                        
                        Expenses_List = Listbox(root)
                        
                        

                    # Move Current Window Widgets
                    ExpenseLabel.place(x = 1000, y = 1000)
                    canvas.delete(Example_Box)
                    canvas.delete(ExampleBox_Text)
                    ExpenseName.place(x = 1000, y = 1000)
                    ExpenseCost.place(x = 1000, y = 1000)
                    ExpenseName_Example.place(x = 1000, y = 1000)
                    ExpenseCost_Example.place(x = 1000, y = 1000)
                    Car_Label.place(x = 1000, y = 1000)
                    Car_Cost.place(x = 1000, y = 1000)
                    ExpenseName_Entry.place(x = 1000, y = 1000)
                    ExpenseCost_Entry.place(x = 1000, y = 1000)
                    AddExpense.place(x = 1000, y = 1000)
                    Next.place(x = 1000, y = 1000)

                    # Create New Window Widgets (ListBoxes)
                    Name_ListBox = Listbox(root)
                    Name_ListBox.place(x = 65, y = 110)
                    Cost_ListBox = Listbox(root)
                    Cost_ListBox.place(x = 215, y = 110)

                    # Create Labels
                    NameListBox_Label = Label(root, text = "Expense Name:", borderwidth = 2, relief = 'solid', font = ('arial',10))
                    CostListBox_Label = Label(root, text = "Expense Cost:", borderwidth = 2, relief = 'solid', font = ('arial',10))
                    NameListBox_Label.place(x = 65, y = 85)
                    CostListBox_Label.place(x = 215, y = 85)

                    # Create Button
                    Next_Page = Button(root, text = 'Next', fg =  'blue', command = Managment)
                    Next_Page.place(x = 185, y  = 300)

                    for index in range(0, len(Expenses_Name)):
                        
                        # Insert Value
                        Cost_ListBox.insert(index, Expenses_Name[index])

                    for index in range(0, len(Expenses_Cost)):

                        # Insert Value
                        Name_ListBox.insert(index, Expenses_Cost[index])

                global Savings
                
                Savings = Savings_Entry.get()

                # Move Current Window Widgets
                Savings_Label.place(x = 1000, y = 1000)
                Savings_Warning.place(x = 1000, y = 1000)
                Savings_Entry.place(x = 1000, y = 1000)
                Savings_Enter.place(x = 1000, y = 1000)

                # Create New Window Widgets (Labels)
                ExpenseLabel = Label(root, text = 'Enter Expenses', borderwidth = 2, relief = 'solid', font = ('arial',20))
                ExpenseLabel.place(x = 100, y = 75)
                ExpenseName = Label(root, text = 'Expense Name:', borderwidth = 2, relief = 'solid', font = ('arial',10))
                ExpenseName.place(x = 100, y = 135)
                ExpenseCost = Label(root, text = 'Expense Cost:', borderwidth = 2, relief = 'solid', font = ('arial',10))
                ExpenseCost.place(x = 100, y = 155)

                # Create Example
                Example_Box = canvas.create_rectangle(100,225,300,325, fill = 'light grey')
                ExampleBox_Text = canvas.create_text(140,212, fill = 'Black', text = 'Example:', font = ("arial", 15))
                ExpenseName_Example = Label(root, text = 'Expense Name:', borderwidth = 2, relief = 'solid', font = ('arial',10))
                ExpenseName_Example.place(x = 115, y = 250)
                ExpenseCost_Example = Label(root, text = 'Expense Cost:', borderwidth = 2, relief = 'solid', font = ('arial',10))
                ExpenseCost_Example.place(x = 115, y = 280)
                Car_Label = Label(root, text = 'Car', borderwidth = 2, relief = 'solid', font = ('arial',10))
                Car_Label.place(x = 225, y = 250)
                Car_Cost = Label(root, text = '5000', borderwidth = 2, relief = 'solid', font = ('arial',10))
                Car_Cost.place(x = 217, y = 280)

                # Create New Window Widgets (Entry)
                ExpenseName_Entry = Entry(root)
                ExpenseName_Entry.place(x = 215, y = 156)
                ExpenseCost_Entry = Entry(root)
                ExpenseCost_Entry.place(x = 215, y = 136)

                # Create New Window Widgets (Buttons)
                AddExpense = Button(root, text = 'Add Expense', fg = 'blue', command = Add)
                Next = Button(root, text = 'Next', fg = 'blue', command = Next)
                Next.place(x = 250, y = 335)
                AddExpense.place(x = 100, y = 335)

                # Establish Control
                #Control = 0

                # Establish Expense List
                Expenses_Name = []
                Expenses_Cost = []
            
            # Move Current Window Widgets
            Choice_1.place(x = 1000, y = 1000)
            Choice_2.place(x = 1000, y = 1000)
            IncomeLabel.place(x = 1000, y = 1000)

            # Create New Window Widgets
            Savings_Label = Label(root, text = "Enter Savings Balance", borderwidth = 2, relief = 'solid', font = ('arial',20))
            Savings_Warning = Label(root, text = "Don\'t Include \'$\' or \',\'", borderwidth = 2, relief = 'solid', font = ('arial',15))
            Savings_Label.place(x = 65, y = 75)
            Savings_Warning.place(x  = 105, y = 115)

            # Create New Entry Widget
            Savings_Entry = Entry(root)
            Savings_Entry.place(x = 140, y = 200)

            # Create Enter Button
            Savings_Enter = Button(root, text = "Enter", fg = 'blue', borderwidth = 2, relief = 'raised', command = SaveBalance_Expense_Prompt)
            Savings_Enter.place(x = 140, y = 225)   
            
        def Saving_Annual_Income():

            def SaveInc_Annual():

                global Annual_Income
                
                # Save Annual Income
                Annual_Income = AnnualInc_Entry.get()

                # Move Current Window Widgets
                AnnualInc_Label.place(x = 1000, y = 1000)
                AnnualInc_Warning.place(x = 1000, y = 1000)
                AnnualInc_Entry.place(x = 1000, y = 1000)
                AnnualInc_Enter.place(x = 1000, y = 1000)

                Savings()
            
            # Move Current Window Widgets
            Choice_1.place(x = 1000, y = 1000)
            Choice_2.place(x = 1000, y = 1000)
            IncomeLabel.place(x = 1000, y = 1000)

            # Create New Window Widgets (Label)
            AnnualInc_Label = Label(root, text = "Enter Annual Income", borderwidth = 2, relief = 'solid', font = ("arial",20))
            AnnualInc_Warning = Label(root, text = "Don\'t Include \'$\' or \',\'", borderwidth = 2, relief = 'solid', font = ('arial',15))
            AnnualInc_Label.place(x = 75, y = 75)
            AnnualInc_Warning.place(x  = 110, y = 115)

            # Create New Window Widgets (Entry)
            AnnualInc_Entry = Entry(root)
            AnnualInc_Entry.place(x = 140, y = 200)

            AnnualInc_Enter = Button(root, text = "Enter", fg = 'blue', borderwidth = 2, relief = 'raised', command = SaveInc_Annual)
            AnnualInc_Enter.place(x = 140, y = 225)
            
        # Prompt User For Income Type
        Choice_1 = Button(root, text = "I Have A Stable Income", fg = 'blue', borderwidth = 2, relief = 'raised', command = Saving_Annual_Income)
        Choice_2 = Button(root, text = "I Am A Freelancer", fg = 'blue', borderwidth = 2, relief = 'raised', command = Savings)
        Choice_1.place(x = 100, y = 175)
        Choice_2.place(x = 100, y = 210)
        
        # Place Label
        IncomeLabel = Label(root, text = "Enter Income Type", borderwidth = 2, relief = "solid", font = ('arial',20))
        IncomeLabel.place(x = 85, y = 75)
        
    def Save_Name():
        global UserName
        
        UserName = UserName_Entry.get() # Saves Username

        # Move Ojects
        UserName_Label.place(x = 1000, y = 1000) 
        UserName_Enter.place(x = 1000, y = 1000)
        UserName_Entry.place(x = 1000, y = 1000)

        Buffer()
        
    # Delete Main Screen Objects
    canvas.delete(Start_Box)
    canvas.delete(Wealth_Managment)
    canvas.delete(Developed_By)
    Start.destroy() # Destroy Button

    # Establish Entry Widget For User Name Input
    UserName_Entry = Entry(root)
    UserName_Entry.place(x = 140, y = 200)

    # Initialize Label Next To Widget
    UserName_Label = Label(root, text = "Enter User Name", borderwidth = 2, relief = "solid", font = ('arial',20))
    UserName_Label.place(x = 100, y = 75)
    
    # Initialize Entry Button
    UserName_Enter = Button(root, text = "Enter", fg = 'blue', borderwidth = 2, relief = 'raised', command = Save_Name)
    UserName_Enter.place(x = 140, y = 225)

# Create Loop
root.mainloop()
