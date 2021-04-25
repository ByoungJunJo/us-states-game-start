# us-states-game-start
## Challenges
1. Get the x and y coordinate of each state
```
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
```
2. Set up the screen and classes
```
state = State()
screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
```
3. Convert the guess to Title case
```
def ask_state(self):
    self.answer_state = self.screen.textinput(title="Guess the States",
                                              prompt="What's another state's name?").title()
    self.add_guessed_states()
    self.hideturtle()
    self.penup()
    self.update_map()

```
4. Check if the guess is among the 50 states
```
def update_map(self):
    for state in self.states_list:
        if self.answer_state == state:
            self.answer_state_x_cor = int(self.df[self.df.state == self.answer_state].x)
            self.answer_state_y_cor = int(self.df[self.df.state == self.answer_state].y)
            self.goto(self.answer_state_x_cor, self.answer_state_y_cor)
            self.write(f"{self.answer_state}")
            self.scoreboard.increase_score()
            self.scoreboard.update_scoreboard()
            self.add_guessed_states()
```
5. Check whether the user wants to exit the game
```
def exit_game(self):
    if self.answer_state == "Exit":
        self.add_missed_states()
        self.is_game_on = False
```
6. Keep tracking the scores
```
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
```
7. Add any missed states by the user and give them into a csv file
```
def add_guessed_states(self):
    self.guessed_states.append(self.answer_state)

def add_missed_states(self):
    for state in self.states_list:
        if state not in self.guessed_states:
            self.missed_states.append(state)
    new_data = pd.DataFrame(self.missed_states)
    new_data.to_csv("states_to_learn.csv")
```
8. Finally, use a loop to allow the user to keep guessing
```
# In main.py
while state.is_game_on:
    if len(state.guessed_states) > 50:
        state.is_game_on = False
    else:
        state.update_map()
        state.ask_state()
        state.exit_game()
```        
## Lessons
- Compared to Angela's code, mine is complex. But it works!
- I'm proud of myself that I've completed this project with the object-oriented programming (OOP).
- As I said ealier, it's messier than the instructor's code, but it was a good way to practice both Pandas library and OOP.
- One thing I'd like to improve on is: My program keeps double-counting each correct state. Hence, I used `self.score += 0.5`.
