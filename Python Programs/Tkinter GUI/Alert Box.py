from tkinter import *
import tkinter.messagebox
root = Tk()
root.geometry("1x1")

tkinter.messagebox.showinfo("This is An Alert Box")

question = tkinter.messagebox.askquestion("Question 1", "Is This A Test")

if question == "yes":
    tkinter.messagebox.showinfo("Correct", "You Are Correct")
else:
    if question == "no":
        tkinter.messagebox.showinfo("Wrong", "This is in Fact A Test")


