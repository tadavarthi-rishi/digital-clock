import time
from tkinter import *

canvas = Tk()
canvas.title('Digital clock')
canvas.geometry('300x200')
label = Label(canvas,font = ('Helvetica',20,'bold'),bg='red',fg='white')
label.grid(row = 1, column = 1)
def clock():
    input = time.strftime('%H:%M:%S')
    label.config(text=input)
    label.after(100,clock)
clock()
canvas.mainloop()
    