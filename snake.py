import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=2

pos_list = []
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape("square")

turtle.hideturtle()

for s in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stamp_ID=snake.stamp()
    stamp_list.append(stamp_ID)
UP_ARROW="Up"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
LEFT_ARROW="Left"
TIME_STEP=100
SPACEBAR="space"

UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP

UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

def up():
    global direction
    direction=UP
    #move_snake()
    print("You pressed the up key! :)")
def down():
    global direction
    direction=DOWN
    #move_snake()
    print("You pressed the down key! :)")
def left():
    global direction
    direction=LEFT
    #move_snake()
    print("You pressed the left key! :)")
def right():
    global direction
    direction=RIGHT
    #move_snake()
    print("You pressed the right key! :)")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("you moved right! :D")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left! :D")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up! :D")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print("You moved down! :D")
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    #special place
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos >=RIGHT_EDGE:
        print("You hit the right edge! Game Over!")
        quit()
    elif new_x_pos <=LEFT_EDGE:
        print("You hit the left edge! Game Over!")
        quit()
    elif new_y_pos <=DOWN_EDGE:
        print("You hit the bottom edge! Game Over!")
        quit()
    elif new_y_pos >=UP_EDGE:
        print("You hit the top edge! Game Over!")
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

food = turtle.clone()
food.shape("circle")

food_pos=[(100,100),(-100,100),(-100,-100),(100,-100)]
food_stamps=[]

    
    