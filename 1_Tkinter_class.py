from tkinter import *
"""упражнение с модулем Tkinter
"""
class Block:
    def __init__(self, master):
        self.e = Entry(master, width = 30)
        self.b = Button(master, text=' Преобразователь ')
        self.l = Label(master, bg = 'black', fg = 'white', width = 30)
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def setFunc(self, func):
        """
        привязка к кнопке функцию-обработчик
        :param func: функция
        """
        self.b['command'] = eval('self.' + func)
    def strToSortlist(self):
        """ функция разбивает текст на слова и сортирует
            по алфавиту и выводится в метке
        """
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)
    def strRevers(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

root = Tk()
first_block = Block(root)
first_block.setFunc('strToSortlist')

second_block = Block(root)
second_block.setFunc('strRevers')

root.mainloop()

