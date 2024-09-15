from tkinter import *
import time
import random
root = Tk()
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(width = 300, height = 300)
root.title('Geussing Game')
canvas.pack()
canvas.create_rectangle(0,0,510,510, fill = 'light blue')
bx = 130
by = 150

def sub_menu_func():
    print("Test")
Mainmenu = Menu(root)
root.configure(menu = Mainmenu)
subMenu = Menu(Mainmenu)
sub2 = Menu(subMenu)
Mainmenu.add_cascade(label = "Options",menu = subMenu)
subMenu.add_command(label = "Exit", command = sub_menu_func)
subMenu.add_separator()
subMenu.add_cascade(label = "Graphics", menu = sub2)
sub2.add_command(label = "Normal", command = sub_menu_func)
def main():
    for i in range(0,1):
        id.place(x = 1000, y = 1000)
        time.sleep(float(0.05))
        root.update()
    for i in range(0,40):
        canvas.move(ob_1,0,-5)
        canvas.move(ob_3,0,5)
        time.sleep(float(0.02))
        root.update()
    time.sleep(float(0.5))
    
    

id = Button(root,text = 'Start',fg  = 'green', command = main)
id.place(x = int(bx), y = int(by))

ob_1 = canvas.create_text(150,100, text = 'Number Guesser', fill = 'black', font = ("Times", 20))
ob_2 = canvas.create_rectangle(0,250,500,500, fill = 'light green')
ob_3 = canvas.create_line(55,115,245,115)

root.mainloop()
