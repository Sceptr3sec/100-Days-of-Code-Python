from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
directions = [0, 90, 180, 270]

def random_direction():
    for _ in range(200):
        timmy.forward(30)
        timmy.speed("fastest")
        timmy.setheading(random.choice(directions))

random_direction()
