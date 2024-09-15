import random
import time
from tkinter import *
root = Tk()
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(width = 500, height = 500)
canvas.pack()
canvas.create_rectangle(0,0,1000,1000, fill = 'light blue')
canvas.create_rectangle(510,500,0,400, fill = 'light green')
sun = canvas.create_oval(100,100,250,250, fill = 'yellow')
root.title('Game')
start = canvas.create_text(235,175, text = 'Game', font = ("Times",40))

head = canvas.create_oval(10,10,25,25)
body = canvas.create_line(18,25,18,40)
arms = canvas.create_line(10,28,27,28)
Left_leg = canvas.create_line(18,40,10,50)
Right_leg = canvas.create_line(18,40,25,50)

for i in range(0,1):
    canvas.move(head,0,-100)
    canvas.move(body,0,-100)
    canvas.move(arms,0,-100)
    canvas.move(Left_leg,0,-100)
    canvas.move(Right_leg,0,-100)
    canvas.move(sun,-150,-150)
    root.update()
def up(event):
    for i in range(0,10):
        canvas.move(head,0,-10)
        canvas.move(body,0,-10)
        canvas.move(arms,0,-10)
        canvas.move(Left_leg,0,-10)
        canvas.move(Right_leg,0,-10)
        time.sleep(float(0.03))
        root.update()
    for i in range(0,10):
        canvas.move(head,0,10)
        canvas.move(body,0,10)
        canvas.move(arms,0,10)
        canvas.move(Left_leg,0,10)
        canvas.move(Right_leg,0,10)
        time.sleep(float(0.03))
        root.update()
def Left_A(event):
    for i in range(0,10):
        canvas.move(head,-10,0)
        canvas.move(body,-10,0)
        canvas.move(arms,-10,0)
        canvas.move(Left_leg,-10,0)
        canvas.move(Right_leg,-10,0)
        root.update()
        time.sleep(float(0.03))
def Right_A(event):
    for i in range(0,10):
        canvas.move(head,10,0)
        canvas.move(body,10,0)
        canvas.move(arms,10,0)
        canvas.move(Left_leg,10,0)
        canvas.move(Right_leg,10,0)
        root.update()
        time.sleep(float(0.03))
root.bind("<Return>", up)
root.bind("<Left>", Left_A)
root.bind("<Right>", Right_A) 
def main():
    for i in range(0,100):
        canvas.move(start,-10,0)
        root.update()
        time.sleep(0.01)
    id.place(x = 1000, y = 1000)
    for i in range(0,45):
        canvas.move(head,0,10)
        canvas.move(body,0,10)
        canvas.move(arms,0,10)
        canvas.move(Left_leg,0,10)
        canvas.move(Right_leg,0,10)
        root.update()
        time.sleep(float(0.05))
id = Button(root, text = 'Start', fg = 'Black', command = main)
id.place(x = 235, y = 450)
root.mainloop()
