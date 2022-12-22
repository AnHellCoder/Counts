import math as mt
import matplotlib.pyplot as plt
from tkinter import * #Импортируем все данные библиотеки для пользования без явного обозначения самой библиотеки

def calculate(): #Функция расчёта графика
    data = inbox.get() #Считываем данные из потока inbox

    rads, m = data.split()
    rads, m = float(rads), float(m)

    if(rads > 1.57 or m < 0): #Снаряд должен обладать массой и лететь вперёд может лишь под отклонением менее 90 градусов
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

        errorWindow.mainloop() #Вывод сообщения об ошибке

    a = 1 / m #Сила, действующая на снаряд равна 1. Отсюда, зная массу, вычисляем его ускорение.
    g = 9.8 #Ускорение свободного падения
    h = 0.19 #Снаряд начинает полёт с начальной высоты 0.19 м.

    #Принимая вал за центр окружности, а снаряд за точку на ней
    #считаем радиус равным 0.13 м (т.к. расстояние от вала до снаряда равно 0.13 м),
    #а ускорение, придаваемое снаряду принимаем, принимаем за тангенциальное
    #(до начала полёта движение снаряда можно считать движением по окружности)
    beta = a / 0.13

    #Выражаем время, которое прошло до начала полёта
    #через формулу перемещения тела
    #по окружности при равноускоренном движении
    t = mt.sqrt((1.57 - rads) / (beta / 2))

    V = a * t #Начальная корость полёта

    Vx = V * mt.cos(rads) #Скорость полёта вдоль оси x
    Vy = V * mt.sin(rads) #Скорость полёта вдоль оси y

    x, y = [], [] #Списки координат в разные моменты времени
    flag = h #начальная высота полёта
    i = 0 #Количество пройденного времени

    while(flag > 0): #Список координат пополняется, пока снаряд не упадёт на землю
        x.append(Vx * i) #Формула перемещения тела из точки 0 в момент i
        y.append(h + Vy * i - (g * i**2)/2) #Формула перемещения тела из начальной высоты по оси y в момент i

        flag = h + Vy * i - (g * i**2)/2 #Положение тела на оси y в момент i
        i += 0.001 #Инкремент времени на 1 мс
    
    plt.plot(x, y)
    plt.xlabel('Расстояние полёта')
    plt.ylabel('Высота полёта')

    plt.show() #Отрисовка графика

root = Tk() #Создание окна интерфейса
root.title('Расчёт траектории полёта')
root.geometry('856x200')

canv = Canvas(root, height=300, width=250) #Создание 'холста'
canv.pack()

frame = Frame(root, bg='white') #Создание внутреннего окошка для виджетов
frame.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)

#Создание текстового поля с просьбой ввести данные
greetings = Label(frame, text='Введите угол отклонения при метании в радианах и массу снаряда в килограммах', bg='white')
greetings.config(font=500)
greetings.pack()

inbox = Entry(frame, bg='white')
inbox.pack() #Создание текстбокса для воода данных

calc = Button(frame, text='Рассчитать', bg='white', command=calculate) #Создание кнопки для расчёта графика
calc.pack()

root.mainloop() #Вывод окошка