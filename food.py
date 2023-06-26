from turtle import Turtle, Screen
import random



def new_snack(columns, rows, snake):
    snack = Turtle()
    snack.penup()
    snack.shape("circle")
    snack.fillcolor("yellow")
    x = 20 * random.randint(-columns, columns)
    y = 20 * random.randint(-rows, rows)
    while (x, y) in snake.positions:
       x = 20 * random.randint(-columns, columns)
       y = 20 * random.randint(-rows, rows)
    snack.setpos(x, y)
    return(snack)


class Food:
    

    def __init__(self, amount, columns, rows, snake):
        snack = new_snack(columns, rows, snake)
        self.snack = snack
        self.position = snack.pos()
        self.remaining = amount

    def eat(self, columns, rows, snake):
        if self.remaining > 1:
            self.snack.ht()
            snack = new_snack(columns, rows, snake)
            self.snack = snack
            self.position = snack.pos()
            self.remaining -= 1
        else:
            self.snack.fillcolor('green')
            self.remaining -= 1

