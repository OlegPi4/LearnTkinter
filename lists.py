from tkinter import *
"""
использование Listbox
слева основной список, заполняеся со строки ввода кнопкой <add>
элементы основного списка удаляются кнопкой <delete>
справа - рабочий список формируется из елементов основного 
выбором елемента и нажатием кнопки < >>> > , удаление из рабочего списка - < <<< >
< save > сохраняет в текущем каталоге файлы list000.txt - основной список
list001.txt - рабочий список 
"""


def addItem():
    lbox.insert(END, entry.get())
    entry.delete(0, END)


def delList():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)


def saveList():
    f = open('list000.txt', 'w')
    f.writelines("\n".join(lbox.get(0, END)))
    f.close()
    f2 = open('list001.txt', 'w')
    f2.writelines("\n".join(lbox2.get(0, END)))
    f2.close()


def to_right():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox2.insert(0, lbox.get(i))

def to_left():
    select = list(lbox2.curselection())
    select.reverse()
    for i in select:
        lbox2.delete(i)

root = Tk()
root.title('Списки')
lbox = Listbox(selectmode=EXTENDED, font=('Arial', 10), bd=2, relief=GROOVE)
lbox.pack(side=LEFT, padx = 5, pady = 5)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f, font=('Arial', 10), bd=2, relief=GROOVE)
entry.pack(side = TOP, anchor=N)
badd = Button(f, text="  Add  ", font=('Arial', 10), command=addItem)
badd.pack(side = TOP, fill = X)
bdel = Button(f, text="Delete", font=('Arial', 10), command=delList)
bdel.pack(side = TOP, fill = X)
bsave = Button(f, text=" Save ", font=('Arial', 10), command=saveList)
bsave.pack(side = TOP, fill = X)
brig = Button(f, text="  >>>  ", font=('Arial', 10), command=to_right)
brig.pack(side = TOP, fill = X)
blef = Button(f,  text="  <<<  ", font=('Arial', 10), command=to_left)
blef.pack(side = TOP, fill = X)
lbox2 = Listbox(selectmode=EXTENDED, font=('Arial', 10), bd=2, relief=GROOVE)
lbox2.pack(side=RIGHT, padx = 5, pady = 5)
scroll2 = Scrollbar(command=lbox2.yview)
scroll2.pack(side=LEFT, fill=Y)
lbox2.config(yscrollcommand=scroll2.set)


root.mainloop()
