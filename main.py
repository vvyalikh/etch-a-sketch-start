from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def draw_circle():
    """draws circle counterclockwise"""
    tim.circle(100, 45)


def draw_circle1():
    """draws circle clockwise"""
    tim.circle(-100, 45)


def turn_left():
    new_heading = tim.heading()+20
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading()-20
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="b", fun=draw_circle)
screen.onkey(key="a", fun=draw_circle1)
screen.onkey(key="c", fun=clear)
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.exitonclick()
