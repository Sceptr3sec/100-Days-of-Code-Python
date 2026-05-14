from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(15)

screen = timmy.screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def random_walk():
    directions = [0, 90, 180, 270]
    for _ in range(200):
        timmy.forward(30)
        timmy.speed("fastest")
        timmy.setheading(random.choice(directions))
        timmy.color(random_color())

random_walk()

my_screen = Screen()
my_screen.exitonclick()