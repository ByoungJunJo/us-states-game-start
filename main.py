import turtle as t
from state import State

## Get the x and y coordinate of each state
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Set up the screen and classes
state = State()
screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

# Use a loop to allow the user to keep guessing
while state.is_game_on:
    if len(state.guessed_states) > 50:
        state.is_game_on = False
    else:
        state.update_map()
        state.ask_state()
        state.exit_game()