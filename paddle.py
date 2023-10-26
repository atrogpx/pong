from turtle import Screen, Turtle

screen = Screen()


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        screen.tracer(0)
        self.penup()
        self.goto(position)

    def go_up(self):
        x = self.xcor()
        y = self.ycor() + 20
        self.goto(x, y)

    def go_down(self):
        x = self.xcor()
        y = self.ycor() - 20
        self.goto(x, y)
