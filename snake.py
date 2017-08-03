import turtle
import random

turtle.tracer(1,0)

SIZE_X=700
SIZE_Y=400
SIZE_X2=800
SIZE_Y2=500
turtle.setup(SIZE_X2,SIZE_Y2)

RIGHT_BORDER = 300
LEFT_BORDER = -300
UP_BORDER = 200
DOWN_BORDER = -200

#this block draws the borders:
turtle.penup()
box=turtle.clone()
box.shape("blank")
box.goto(LEFT_BORDER,UP_BORDER)
box.pd()
box.pensize(8)
box.color("blue")
box.goto(RIGHT_BORDER,UP_BORDER)
box.goto(RIGHT_BORDER,DOWN_BORDER)
box.goto(LEFT_BORDER,DOWN_BORDER)
box.goto(LEFT_BORDER,UP_BORDER)
SQUARE_SIZE=20
START_LENGTH=1
score=0

#List definition:
pos_list = []
stamp_list=[]
food_pos=[]
food_stamps=[]

#This block makes the snakes:
snake=turtle.clone()
snake.shape("circle")
snake.color("red")
turtle.hideturtle()

#This block saves all snake positions during
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

UP_EDGE=200
DOWN_EDGE=-200
RIGHT_EDGE=300
LEFT_EDGE=-300

def up():
    global direction
    if direction != DOWN:
        direction=UP
        #move_snake()
        print("You pressed the up key! :)")
def down():
    global direction
    if direction != UP:
        direction=DOWN
    #move_snake()
    print("You pressed the down key! :)")
def left():
    global direction
    if direction != RIGHT:
        direction=LEFT
    #move_snake()
    print("You pressed the left key! :)")
def right():
    global direction
    if direction != LEFT:
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

    if snake.pos() in food_pos:
        global score
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        score=score+1
        turtle.clear()
        turtle.write("Apples Eaten: "+str(score),font=("David",20),align="center")
        #stamp_list.append(snake.pos())
        make_food()
        print("You have eaten the food!")
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos >=RIGHT_EDGE:
        print("You hit the right edge! Game Over!")
        quit()
    if new_x_pos <=LEFT_EDGE:
        print("You hit the left edge! Game Over!")
        quit()
    if new_y_pos <=DOWN_EDGE:
        print("You hit the bottom edge! Game Over!")
        quit()
    if new_y_pos >=UP_EDGE:
        print("You hit the top edge! Game Over!")
        quit()
    if snake.pos() in pos_list[:-1]:
        quit()
        
    #if snake.pos() in stamp_list[0:-1]:
        #quit()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

turtle.register_shape("apple.gif")
food = turtle.clone()
food.shape("apple.gif")
food_pos=[food.pos()]
food_stamps=[]


for this_food_pos in food_pos:
    food.goto(this_food_pos)
    fd_stamp=food.stamp()
    food_stamps.append(fd_stamp)
    food.hideturtle()

def make_food():
    min_x=-int(SIZE_X/3/SQUARE_SIZE)+1
    max_x=int(SIZE_X/3/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/3/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/3/SQUARE_SIZE)+1

    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())
if food.pos() in pos_list[:-1]:
    food.clearstamp()
    make_food()



    

    
        
    

    
    
    
