import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Illusion")
t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for x in range(360):
    t.pencolor(colors[x % len(colors)]) 
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(60)
turtle.done()





