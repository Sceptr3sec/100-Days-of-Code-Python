from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

screen = tim.screen.colormode(255)

def set_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.speed("fastest")
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(set_random_color())

draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()