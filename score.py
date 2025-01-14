from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.line = "|"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 200)
        self.write(self.line, align="center", font=("Arial", 70, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
