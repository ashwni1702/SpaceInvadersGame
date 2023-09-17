from turtle import Turtle

class PlayerShip(Turtle):
    STARTING_POSITION = (0, -370)
    MOVE_DISTANCE = 30
    X_LEFT_SCREEN = -360
    X_RIGHT_SCREEN = 360

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.6, stretch_len=2)
        self.penup()
        self.color("white")
        self.go_to_start()

    def go_to_start(self):
        self.goto(PlayerShip.STARTING_POSITION)

    def go_right(self):
        if self.xcor() < PlayerShip.X_RIGHT_SCREEN:
            self.forward(PlayerShip.MOVE_DISTANCE)

    def go_left(self):
        if self.xcor() > PlayerShip.X_LEFT_SCREEN:
            self.backward(PlayerShip.MOVE_DISTANCE)

class Shooter(Turtle):
    STARTING_POSITION = (0, -370)
    SHOOT_DISTANCE = 40

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.1, 0.5)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(Shooter.STARTING_POSITION)

    def move(self):
        self.forward(Shooter.SHOOT_DISTANCE)
