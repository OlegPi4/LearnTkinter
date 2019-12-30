from tkinter import *

root = Tk()
root.title('TEST')
text = Text(width = 30, height = 6, bg = "darkgreen", fg="white",
            wrap = WORD, font=('Arial', 10))

f_top = Frame()
f_bot = Frame()
l = Label(width=30, height=10, text="Свойства метки")
b1 = Button(f_top, width = 6, height = 3, bg = 'yellow', text='1')
b2 = Button(f_top, width = 6, height = 3, bg = 'orange', text='2')
b3 = Button(f_bot, width = 6, height = 3, bg = 'lightgreen', text='3')
b4 = Button(f_bot, width = 6, height = 3, bg = 'lightblue', text='4')
f_top.pack()
f_bot.pack()

b1.pack(side=LEFT, padx=5, pady=3)
b2.pack(side=LEFT, padx=3, pady=3)
b3.pack(side=LEFT, padx=5, pady=3)
b4.pack(side=LEFT, padx=3, pady=3)
text.pack(side = LEFT)
scroll = Scrollbar(command = text.yview())
scroll.pack(side = RIGHT, fill=Y)
text.config(yscrollcommand = scroll.set)
root.mainloop()