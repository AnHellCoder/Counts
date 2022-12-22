import math as mt
import matplotlib.pyplot as plt
from tkinter import *

def calculate():
    data = inbox.get()

    rads, m = data.split()
    rads, m = float(rads), float(m)

    if(rads > 1.57 or m < 0):
        errorWindow = Tk()
        errorWindow.title('Ошибка!')
        errorWindow.geometry('856x200')

        errorCanv = Canvas(errorWindow, height=300, width=250)
        errorCanv.pack()

        errorFrame = Frame(errorWindow, bg='white')
        errorFrame.place(relx=0.15, rely=0.15, relheight=0.9, relwidth=0.7)
        
        errorLab = Label(errorFrame, text='Данные введены неверно!', bg='white')
        errorLab.config(font=500)
        errorLab.pack()

        closeBtn = Button(errorFrame, text='Закрыть', bg='white', command=errorWindow.destroy)
        closeBtn.pack()

        errorWindow.mainloop()

    a = 1 / m
    g = 9.8
    h = 0.19

    beta = a / 0.13

    t = mt.sqrt((1.57 - rads) / (beta / 2))

    V = a * t

    Vx = V * mt.cos(rads)
    Vy = V * mt.sin(rads)

    x, y = [], []
    flag = h
    i = 0

    while(flag > 0):
        x.append(Vx * i)
        y.append(h + Vy * i - (g * i**2)/2)

        flag = h + Vy * i - (g * i**2)/2
        i += 0.001
    
    plt.plot(x, y)
    plt.xlabel('Расстояние полёта')
    plt.ylabel('Высота полёта')

    plt.show()

root = Tk()
root.title('Расчёт траектории полёта')
root.geometry('856x200')

canv = Canvas(root, height=300, width=250)
canv.pack()

frame = Frame(root, bg='white')
frame.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)

greetings = Label(frame, text='Введите угол отклонения при метании в радианах и массу снаряда в килограммах', bg='white')
greetings.config(font=500)
greetings.pack()

inbox = Entry(frame, bg='white')
inbox.pack()

calc = Button(frame, text='Рассчитать', bg='white', command=calculate)
calc.pack()

root.mainloop()

#############################################