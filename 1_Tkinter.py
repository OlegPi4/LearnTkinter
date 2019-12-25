# файл exempl1.py
"""первое упражнение с модулем Tkinter
"""
from tkinter import *
root = Tk()
e = Entry(width = 20)
b = Button(text=' Преобразователь ')
l = Label(bg = 'black', fg = 'white', width = 30)
def strToSortlist(event):
    """ функция разбивает текст на слова и сортирует
        по алфавиту и выводится в метке
    """
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortlist)
e.pack()
b.pack()
l.pack()
root.mainloop()