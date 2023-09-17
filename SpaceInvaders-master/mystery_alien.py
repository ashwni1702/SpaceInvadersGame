from turtle import Turtle
import random

class MysteryAlien(Turtle):
    STARTING_POINT = (-400, 340)
    MOVE_SPEED = 15

    def __init__(self):
        """Initiates class MysteryAlien, inherits from Turtle super class, sets initial attributes"""
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 3)
        self.penup()
        self.color("#191D88")
        self.hideturtle()
        self._move_speed = MysteryAlien.MOVE_SPEED
        self.goto(MysteryAlien.STARTING_POINT)

    def trigger(self):
        """Method is randomized. If MysteryAlien is not visible, shows it and moves it across the screen. Randomizes
        the attribute _move_speed."""
        random_chance = random.randint(1, 40)
        if random_chance == 1 and not self.isvisible():
            self.goto(MysteryAlien.STARTING_POINT)
            self.showturtle()
            self._move_speed += random.randint(-10, 5)

    def move(self):
        """Moves MysteryAlien horizontally across the screen. If it reaches the right screen limit, hides and moves
        back to the starting point."""
        self.forward(self._move_speed)
        screen_width = self.screen.window_width()
        if self.xcor() > screen_width / 2:
            self.hideturtle()
            self.goto(MysteryAlien.STARTING_POINT)
            self._move_speed = MysteryAlien.MOVE_SPEED

    def get_move_speed(self):
        """Getter method for _move_speed."""
        return self._move_speed
