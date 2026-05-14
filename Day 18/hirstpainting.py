###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

def extract_colors():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))

def draw_painting():
    tim = Turtle()
    tim.shape("turtle")
    tim.speed("fastest")
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    screen = tim.screen.colormode(255)
    for _ in range(10):
        for _ in range(10):
            tim.dot(20, random.choice(rgb_colors))
            tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

extract_colors()
draw_painting()

my_screen = Screen()
my_screen.exitonclick()