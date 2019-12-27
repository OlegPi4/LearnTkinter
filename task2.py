from tkinter import *

class Name_Color:
    def __init__(self, master, colors_text, command):
        self.b = Button(text='', bg = colors_text, width = 20, font=('Arial', 10))
        self.b.config(command=self.sign)
        self.b.pack()
        self.c = command
        self.t = colors_text
    def sign(self):
        l['text'] = self.c
        self.b['text'] = self.t


colors_cod = ['#ff0000','#ff7d00','#ffff00','#00ff00','#007dff','#0000ff','#fd00ff']
colors_text = ["red", "orange", "yellow", "green", "blue", "dark blue", "purple"]

root = Tk()
root.title("Цвета и коды цветов")
l=Label(text=' '*42, font=('Arial', 12), bg='#a8a8a8')
l.pack()

for c in range(len(colors_cod)):
    c = Name_Color(root, colors_cod[c], colors_text[c])
root.mainloop()