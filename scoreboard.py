from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Correct States: {self.score} out of 50 states", move=False, font=FONT, align="center")

    def increase_score(self):
        self.clear()
        self.score += 0.5
        self.update_scoreboard()