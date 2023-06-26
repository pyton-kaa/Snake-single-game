from time import sleep
import random
from turtle import Turtle, Screen
from snake import Snake
from food import Food

columns = 10
rows = 10
game_is_on = False

win = Screen()
win.setup(width = 20 * columns, height = 20 * rows)
# win.title("The Snake Game")
win.bgcolor("black")
win.tracer(0)

columns = int(win.numinput(title = "Choose the world size",
                       prompt = "Enter the initial distance to the left and right borders (integer between 7 and 30).\nIf you choose N, the board will have 2N+1 columns.",
                       minval = 7, maxval = 30))
rows = int(win.numinput(title = "Choose the world size",
                    prompt = "Enter the initial distance to the top and bottom borders (integer between 7 and 30).\nIf you choose N, the board will have 2N+1 rows.",
                    minval = 7, maxval = 30))

win.setup(width = 40 * columns + 50, height = 40 * rows + 100, startx = None, starty = None)

border = Turtle()
border.penup()
border.setpos(-20 * columns - 15, 20 * rows + 15)
border.seth(0)
border.pendown()
border.pencolor("white")
border.pensize(5)
border.fd(40 * columns + 30)
border.right(90)
border.fd(40 * rows + 30)
border.right(90)
border.fd(40 * columns + 30)
border.right(90)
border.fd(40 * rows + 30)
border.penup()
border.ht()
border.setpos(0, 20 * rows + 20)
border.write("The Snake Game", font = ('Verdana', 14, 'bold'), align='center')
border.goto(0, -20 * rows - 40)
win.update()

max_length = 10
if columns < 10:
    max_length = columns
initial_length = int(win.numinput(title = "Snake length", prompt = f"Select the initial length of the snake (between 2 and {max_length}):", minval = 2, maxval = max_length))
snacks = int(win.numinput(title = "Amount of food",
                          prompt = "Enter the number of snacks for the snake to eat during the game.\n If you choose '0', then the food never ends; you have to eat as much as possible before you crash."))
if snacks == 0:
    snacks = 5 * columns * rows
game_speed = int(win.numinput(title = "Game speed", prompt = "Select the speed of the game (between 1 and 10):", minval = 1, maxval = 10))

snake = Snake(initial_length)
food = Food(amount = snacks, columns = columns, rows = rows, snake = snake)
win.update()

step = (20,0)

def search(snake, food, rows, columns, step):
    x = snake.positions[0][0] + step[0]
    y = snake.positions[0][1] + step[1]
    if x < -20 * columns or y < -20 * rows or x > 20 * columns or y > 20 * rows:
        return("wall")
    elif (x,y) in snake.positions:
        return("snake")
    elif food.position == (x,y):
        return("food")
    else:
        return("free")
    

def turn_north():
    global step
    step = (0,20)

def turn_east():
    global step
    step = (20,0)
    
def turn_south():
    global step
    step = (0,-20)

def turn_west():
    global step
    step = (-20,0)

win.listen()    
win.onkeypress(turn_north, "Up")
win.onkeypress(turn_east, "Right")
win.onkeypress(turn_south, "Down")
win.onkeypress(turn_west, "Left")

counter = Turtle()
counter.ht()
counter.penup()
counter.pencolor('yellow')
counter.goto(0, 20)
for n in range(3):
    counter.write(f'{3-n}', font = ('Verdana', 24, 'bold'), align = 'center')
    sleep(1)
    counter.clear()
game_is_on = True
counter.goto(20 * columns + 10, 20 * rows + 20)
counter.write('Current score: 0', font = ('Verdana', 12, 'normal'), align = 'right')
score = 0

while(game_is_on):

    sleep(0.55 - 0.05 * game_speed)

    
    goal = search(snake, food, rows, columns, step)
    if goal in ["snake", "wall"]:
        snake.crash()
        # print(f"Position: {snake.positions[0]}. Step: {step}. Goal: {goal}.")
        game_is_on = False
        border.pencolor('red')
        border.write("Game over!", font = ('Verdana', 14, 'bold'), align = 'center')
        counter.clear()
        counter.write(f'Your final score: {score}', font = ('Verdana', 12, 'bold'), align = 'right')
    elif goal == "food":
        snake.eat(step)
        food.eat(columns, rows, snake)
        score += 1
        counter.clear()
        counter.write(f'Current score: {score}', font = ('Verdana', 12, 'normal'), align = 'right')
    elif goal == "free":
        snake.move(step)
    else:
        print("The search function failed!")

    if food.remaining == 0:
        game_is_on = False
        border.write("Congratulations! You win!", font = ('Verdana', 14, 'bold'), align = 'center')
    win.update()


win.exitonclick()