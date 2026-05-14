from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
for _ in range(100):
    tim.forward(100)
    tim.penup()
    tim.forward(10)
    tim.pendown()