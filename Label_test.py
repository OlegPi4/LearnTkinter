from tkinter import *
"""
описание Label
"""
root = Tk()
l1 = Label(text="Машинное обучение", font="Arial, 32") # надпись + вариант передачи шрифта
l2 = Label(text="      Вторая надпись      ", font=("Comic Sans MS", 24, "bold")) # надпись по другой вариант  задания шрифта
                                                                      # 3-е значение - стиль
l1.config(bd=20, bg='#ffaaaa') # размер границ в пикселях и цвет фона
l2.config(bd=20, bg='#aaff55') #
l1.pack()
l2.pack()

"""
создание кнопок по "ходу"
"""
def take():
    l['text'] = " Выдано "



Label(text="Пункт выдачи", font="Arial, 12").pack()
Button(text="Взять", font="Arial, 12", command=take).pack()
l = Label(width=10, height=2, font="Arial, 12")
l.pack()

e = Entry(width=50)
def insert():
    e.insert(0, "Text TEXT")
b = Button(text="Вставить текст", command=insert)
e.pack()
b.pack()
root.mainloop()