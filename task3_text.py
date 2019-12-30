from tkinter import *
from tkinter import messagebox
"""
В текстовом окне открывается файл из текущего каталога, заданый  в строке
и становится  доступен для редактирования. Кнопка "Открыть" - открывает заданый
файл, кнопка "Сохранить" - сохраняет изменения в файле, Очистить - очистка 
текстового окна
В текстовом окне заданы скролы по горизонтали и вертикали 
"""
def open_file():
    try:
        file = open(e.get(), 'r')
        text.delete(1.0, END)
        if file.name == e.get():
            for i in file:
                text.insert(END, i)
            file.close()

    except FileNotFoundError:
        messagebox.showerror("Ошибка, файл не найден!")
def save_file():
    try:
        str = text.get(1.0, END)
        file = open(e.get(), 'w')
        if not file.closed:
            file.write(str)
            messagebox.showinfo("Файл сохранен!")
            file.close()
    except FileNotFoundError:
        messagebox.showerror("Ошибка, файл не найден!")
def clear_text():
    text.delete(1.0, END)

root = Tk()
root.title("Редактируем файл")


f_top = Frame(root)
f_bot = Frame(root)
f_top.pack()
f_bot.pack(expand = 1, fill = BOTH)
e = Entry(f_top, width=30, bd=2, relief=GROOVE, font=('Arial', 10))
e.insert(0, '')
e.pack(side=LEFT)

b_open = Button(f_top, text='Открыть', command = open_file, font=('Arial', 10), bg="#cccccc")
b_open.pack(side = LEFT, pady=3, padx=3)
b_save = Button(f_top, text="Сохранить", command = save_file, font=('Arial', 10), bg="#cccccc")
b_save.pack(side = LEFT, pady=3, padx=3)
b_clear = Button(f_top, text="Очистить", command = clear_text, font=('Arial', 10,), bg="#cccccc")
b_clear.pack(side = LEFT, pady=3, padx=3)
scroll_y = Scrollbar(f_bot, orient = VERTICAL)
scroll_y.pack(side = RIGHT, fill = Y)
scroll_x = Scrollbar(f_bot, orient = HORIZONTAL)
scroll_x.pack(side = BOTTOM, fill = X, anchor = W)

text = Text(f_bot, width=60, height=20, yscrollcommand = scroll_y.set, xscrollcommand = scroll_x.set, wrap = NONE )
text.pack(expand = 1, fill = BOTH)
scroll_y.config(command = text.yview)
scroll_x.config(command = text.xview)

root.mainloop()