import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(0)
tur.width(2)
tur.bgcolor('black')
tur.seth(20)
n = 100
for i in range(n):
    tur.begin_fill()
    tur.color(cs.hsv_to_rgb(i/10,i/n,0.8))
    tur.fillcolor(cs.hsv_to_rgb(i/10,i/n,1))
    tur.right(180)
    tur.circle(i*2.2,90)
    tur.end_fill()
    tur.right(59)
    tur.hideturtle()
tur.done()