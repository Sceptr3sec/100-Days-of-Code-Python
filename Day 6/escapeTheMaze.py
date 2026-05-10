#This is supposed to be the solution to Reeborg's maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_right()

def turn_left():
    pass
def front_is_clear():
    pass
def at_goal():
    pass
def move():
    pass

