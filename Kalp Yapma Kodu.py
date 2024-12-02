import math
import turtle

# x(t) fonksiyonu
def xt(t, scale):
    return scale * (16 * math.sin(t)**3)

# y(t) fonksiyonu
def yt(t, scale):
    return scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

# Turtle ayarları
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
t.pensize(2)
t.pencolor('red')
t.hideturtle()

# Kalbin çizimi
for scale in range(1, 16):
    t.penup()
    t.goto(xt(0, scale), yt(0, scale))
    t.pendown()
    for i in range(0, 100):  # Daha fazla hassasiyet için aralık artırıldı
        x = xt(i / 10, scale)
        y = yt(i / 10, scale)
        t.goto(x, y)

turtle.done()
