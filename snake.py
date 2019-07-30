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
#Go to the top of your file, and after the line that says snake.direction = “Up”,  write:

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

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
turtle.onkeypress(left,'Left')
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
for this_food_pos in food_pos:
    food.goto(100,100)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)
    food.goto(-100,100)
    food2_stamp=food.stamp()
    food_stamps.append(food2_stamp)
    food.goto(-100,-100)
    food3_stamp=food.stamp()
    food_stamps.append(food3_stamp)
    food.goto(100,-100)
    food4_stamp=food.stamp()
    food_stamps.append(food4_stamp)
    food.hideturtle

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    turtle.ontimer(move_snake,TIME_STEP)

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
    elif snake.direction=='Left':
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved left')
    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this

    new_stamp()
    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()

    # The next three lines check if the snake is hitting the 
    # right edge.
    if x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif x_pos<=LEFT_EDGE:
        print('you hit the left edge! Game over!')
        quit()
    elif y_pos>= UP_EDGE:
        print('you hit the top edge! Game over!')
        quit()
    elif y_pos<= DOWN_EDGE:
        print('you hit the bottom edge! Game over!')
        quit()
        

turtle.mainloop()


