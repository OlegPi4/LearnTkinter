import turtle, time, random
joe = turtle.Turtle()
def position_curs(x, y):
    joe.up()
    joe.goto(x, y)
    joe.down()
def starFill(n, dlina):
    colors = random.choice(['green', 'purple', 'red', 'white', 'yellow', 'blue'])
    joe.color(colors)
    joe.left(random.randint(10,90))
    joe.begin_fill()
    if n%2 !=0:
        for i in range(n):
            joe.forward(dlina)
            angle = n//2 * 360/n # используется для нечетного количества вершин
            joe.left(angle)
    joe.end_fill()
window = turtle.Screen()
window.bgcolor('black')
window.setup(700, 500)
joe.speed(20)
joe.hideturtle() # гасим ку рсор
for i in range(5):
    x = random.randint(-325,325)
    y = random.randint(-225,225)
    position_curs(x, y)
    size = random.randint(10, 25)
    vershina = random.choice([5,7,9])
    starFill(vershina, size)
def move(x, y):
    """
    функция рисует звездочку по щелчку мышки
    в координатах х, у
     """
    position_curs(x, y)
    size = random.randint(10, 25)
    vershina = random.choice([5,7,9])
    starFill(vershina, size)

window.onclick(move) #вызов по клику мышки
window.listen()      #ожидание клика мышки
window.mainloop()    #ожидание закрытия окна






