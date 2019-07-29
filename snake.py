import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos=snake.pos()
    pos_list.append(snake_pos)
    snake_stamp=snake.stamp()
    stamp_list.append(snake_stamp)
for position in range(0,8):
        x_pos=snake.xcor()
        y_pos=snake.ycor()
        x_pos+=SQUARE_SIZE
        snake.goto(x_pos,y_pos)
        new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position        

snake.direction = "Up"

def up():
    snake.direction="Up" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")
def down():
    snake.direction="Down"
    move_snake()
    print('You pressed the down key!')
def right():
    snake.direction='Right'
    move_snake()
    print('You pressed the right key')
def left():
    snake.direction='Left'
    move_snake()
    print('You pressed the right key')
    
turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down,'Down')
turtle.onkeypress(right,'Right')
turtle.onkeypress(left,'left')
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print('You moved down')
    elif snake.direction=='Right':
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('You moved right')
    elif snake.direction=='left':
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved left')
    else:
    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this

new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position
 
turtle.mainloop()


