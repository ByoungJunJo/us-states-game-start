from turtle import Turtle, Screen
from scoreboard import Scoreboard
import pandas as pd

class State(Turtle):

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.scoreboard = Scoreboard()
        self.screen.title("U.S. States Game")
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        self.shape(self.image)
        self.df = pd.read_csv("50_states.csv")
        self.states_list = self.df.state.to_list()
        self.answer_state = 0
        self.is_game_on = True
        self.guessed_states = []
        self.missed_states = []

    def ask_state(self):
        # Convert the guess to Title case
        self.answer_state = self.screen.textinput(title="Guess the States",
                                                  prompt="What's another state's name?").title()
        self.add_guessed_states()
        self.hideturtle()
        self.penup()
        self.update_map()

    def update_map(self):
        # Check if the guess is among the 50 states
        for state in self.states_list:
            if self.answer_state == state:
                self.answer_state_x_cor = int(self.df[self.df.state == self.answer_state].x)
                self.answer_state_y_cor = int(self.df[self.df.state == self.answer_state].y)
                self.goto(self.answer_state_x_cor, self.answer_state_y_cor)
                self.write(f"{self.answer_state}")
                self.scoreboard.increase_score()
                self.scoreboard.update_scoreboard()
                self.add_guessed_states()

    def add_guessed_states(self):
        self.guessed_states.append(self.answer_state)

    def add_missed_states(self):
        for state in self.states_list:
            if state not in self.guessed_states:
                self.missed_states.append(state)
        new_data = pd.DataFrame(self.missed_states)
        new_data.to_csv("states_to_learn.csv")

    def exit_game(self):
        if self.answer_state == "Exit":
            self.add_missed_states()
            self.is_game_on = False