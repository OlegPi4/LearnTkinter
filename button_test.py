from tkinter import *
"""
описание Button
"""
root = Tk()

b1 = Button(text="Изменить", width = 10, height=2) # надпись на кнопке и размері кнопки

def change():
    b1['text'] = "Изменено"         #  текст после нажатия кнопки
    b1['bg'] = '#000000'            #  цвет фона
    b1['activebackground'] = '#555555'  #  цвет фона после нажатия
    b1['fg'] = '#ffffff'            #   цвет текста
    b1['activeforeground'] = '#ffffff'  # цвет текста после нажатия

b1.config(command=change)  # установка действия при нажатии кнопки (метод config)
b1.pack()                  #  допускается b1['command'] = change
root.mainloop()
