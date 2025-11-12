import turtle
import math


screen = turtle.Screen()
screen.bgcolor("black")


pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def heart_line(t, color):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.pencolor(color)
    
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    
    pen.goto(x * 10, y * 10)  


def pink_shade(i, total):
    base = 255
    step = int(200 * (i / total))
    r = 255
    g = base - step
    b = base - step // 2
    return (r/255, g/255, b/255)

lines = 120

for i in range(lines):
    t = math.pi * 2 * (i / lines)
    color = pink_shade(i, lines)
    screen.colormode(1.0)
    heart_line(t, color)

turtle.done()