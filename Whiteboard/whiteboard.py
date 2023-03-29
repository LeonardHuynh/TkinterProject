from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

current_x = 0
current_y = 0
color = 'black'
def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y
    canvas.create_line((current_x,current_y,work.x,work.y), width=getCurrentValue(),fill=color,capstyle=ROUND,smooth=TRUE)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color

    color = new_color

def new_canvas():
    canvas.delete('all')
    displayPallete()

#imageIcon = PhotoImage(file="")
#root.iconphoto(False,imageIcon)

colorBox = PhotoImage(file="colorSection.png")
Label(root,image=colorBox,bg="#fff").place(x=10,y=20)

colors = Canvas(root,bg="#ffffff",width=37,height=300,bd=0)
colors.place(x=13,y=60)

eraser = PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=15,y=400)

def displayPallete():
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10,40,30,60),fill="green")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10,70,30,90),fill="brown4")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((10,100,30,120),fill="gray")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((10,130,30,150),fill="blue")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10,160,30,180),fill="red")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10,190,30,210),fill="orange")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10,220,30,240),fill="purple")
    colors.tag_bind(id,'<Button-1>', lambda x: show_color('purple'))

displayPallete()

canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

#Change the width of line
currentValue = tk.DoubleVar()
def getCurrentValue():
    return '{:.2f}'.format(currentValue.get())

def sliderChange(event):
    value_label.configure(text=getCurrentValue())


slider = ttk.Scale(root,from_=0,to=100,orient='horizontal',command=sliderChange,variable=currentValue)
slider.place(x=30,y=530)
#value
value_label = ttk.Label(root,text=getCurrentValue())
value_label.place(x=27,y=550)
root.mainloop()
