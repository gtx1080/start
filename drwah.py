import turtle
import time
turtle.color('red')
turtle.speed(0)
turtle.delay(0)
def draw(a,b,c):
    if c==3:
        return
    length=2**c
    turtle.penup()
    turtle.goto(a-length/2,b)
    turtle.pendown()
    turtle.goto(a+length/2,b)
    turtle.penup()
    turtle.goto(a-length/2,b+length)
    turtle.pendown()
    turtle.goto(a-length/2,b-length)
    turtle.penup()
    turtle.goto(a + length / 2, b + length)
    turtle.pendown()
    turtle.goto(a + length / 2, b - length)
    turtle.penup()
    draw(a-length/2,b+length,c-1)
    draw(a - length / 2, b - length, c - 1)
    draw(a + length / 2, b + length, c - 1)
    draw(a + length / 2, b - length, c - 1)
draw(0,0,8)