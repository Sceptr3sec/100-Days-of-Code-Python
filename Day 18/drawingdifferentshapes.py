from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def draw_triangle():
    for _ in range(3):
        tim.forward(100)
        tim.right(120)

def draw_hexagon():
    for _ in range(6):
        tim.forward(100)
        tim.right(60)

def draw_octagon():
    for _ in range(8):
        tim.forward(100)
        tim.right(45)

draw_square()
draw_triangle()
draw_hexagon()
draw_octagon()

my_screen = Screen()
my_screen.exitonclick()