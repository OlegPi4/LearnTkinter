from tkinter import *

class Name_Color:
    def __init__(self, master, colors_text, command):
        self.b = Button(bg = colors_text, width = 5, height=2, command=self.sign)
        self.b.pack(side=LEFT)
        self.c = command
        self.t = colors_text
    def sign(self):
        l['text'] = self.c
        e.delete(0, END)
        e.insert(0, str(self.t))

colors_cod = ['#ff0000','#ff7d00','#ffff00','#00ff00','#007dff','#0000ff','#fd00ff']
colors_text = ["red", "orange", "yellow", "green", "blue", "dark blue", "purple"]

root = Tk()
root.title("Цвета")
l = Label(text='', width=20, height=1, font=('Arial', 12), bg='#a8a8a8')
e = Entry(font=('Arial', 12), justify='center')
l.pack(expand=1, fill=Y)
e.pack()

for c in range(len(colors_cod)):
    c = Name_Color(root, colors_cod[c], colors_text[c])

root.mainloop()