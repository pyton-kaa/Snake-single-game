from turtle import Turtle


def new_segment():
    segment = Turtle()
    segment.penup()
    segment.shape("square")
    segment.fillcolor("grey")
    segment.pencolor("white")
    return(segment)


# colors = ["white", "grey", "red", "orange", "yellow", "green", "blue", "purple", "brown", "pink", "black"]

class Snake:


    def __init__(self, length):
        segments = []
        positions = []
        for n in range(length):
            tail = new_segment()
            tail.fillcolor("grey")
            tail.pencolor("white")
            tail.setx(-20 * n)
            tail.sety(0)
            positions.append(tail.pos())
            segments.append(tail)
        self.segments = segments
        self.positions = positions
        

    def move(self, step):
        length = len(self.segments)
        for n in range(1, length):
            self.segments[length - n].setpos(self.segments[length - n - 1].pos())
            self.positions[length - n] = self.segments[length - n].pos()
        x_snake = self.segments[0].pos()[0]
        y_snake = self.segments[0].pos()[1]
        self.segments[0].setx(x_snake + step[0])
        self.segments[0].sety(y_snake + step[1])
        self.positions[0] = self.segments[0].pos()
        # print("move", direction)
    
    def eat(self, direction):
        tail = new_segment()
        tail.setpos(self.segments[-1].pos())
        tail.fillcolor("grey")
        self.move(direction)
        self.positions.append(tail.pos())
        self.segments.append(tail)
        # print("eat", direction)

    def crash(self):
        self.segments[0].pencolor("red")
        print("crash")

