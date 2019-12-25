# calkul.py калькулятор
from tkinter import *
class Calkul:
    def __init__(self, master):
        FONT1 = ['Arial', 12]
        FONT2 = ['Arial', 9]
        self.e1 = Entry(master, width=10, font=FONT2)
        self.e2 = Entry(master, width=10, font=FONT2)
        self.b1 = Button(master, text='+', font=FONT1)
        self.b2 = Button(master, text='-', font=FONT1)
        self.b3 = Button(master, text='*', font=FONT1)
        self.b4 = Button(master, text='/', font=FONT1)
        self.l = Label(master, bg='black', fg='white', width=30, text='ввод цифр з клавиатури', font=FONT2)
        self.lrez = Label(master, bg='white', fg='red', width=20, font=FONT2)
        self.e1.pack()
        self.e2.pack()
        self.b1['command'] = self.add
        self.b2['command'] = self.substr
        self.b3['command'] = self.multipl
        self.b4['command'] = self.divid
        self.b1.pack(side = 'right')
        self.b2.pack(side = 'right')
        self.b3.pack(side = 'right')
        self.b4.pack(side = 'right')
        self.l.pack()
        self.lrez.pack()
    def add(self):
        self.oper = "add"
        self.calculat()
    def substr(self):
        self.oper = "sub"
        self.calculat()
    def divid(self):
        self.oper = "div"
        self.calculat()
    def multipl(self):
        self.oper = "mul"
        self.calculat()
    def calculat(self):
        try:
            num1 = float(self.e1.get())
            num2 = float(self.e2.get())
            if self.oper == "add":
                res = str(num1 + num2)
            elif self.oper == "sub":
                res = str(num1 - num2)
            elif self.oper == "div":
                res = str(num1 / num2)
            elif self.oper == "mul":
                res = str(num1 * num2)
        except Exception:
            res = "Ошибка!"
        self.lrez['text'] = res

root = Tk()
root.title('Калькулятор')
statr = Calkul(root)
root.mainloop()