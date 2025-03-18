import turtle
import pandas

def draw_state(state_data):
    """Draws the state on the map using its coordinates."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())

def save_missing_states(all_states, guessed_states):
    """Saves the states that were not guessed into a new CSV file."""
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("States_to_learn.csv") # Αποθηκεύει τις πολιτείες που δεν μαντεύτηκαν

def get_user_input(screen, guessed_states):
    """Displays the input prompt for the user to guess a state and returns the answer."""
    return screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", 
                            prompt="What's another state's name?").title()

def main():
    """The main function that runs the game, displays the states, and records the user's guesses."""
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    # Load the states data from the CSV
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    # Loop until all states are guessed
    while len(guessed_states) < 50:
        answer_state = get_user_input(screen, guessed_states)
        if answer_state == "Exit":
            # Save the states that were not guessed when the user chooses "Exit"
            save_missing_states(all_states, guessed_states)
            break
        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            draw_state(state_data)

if __name__ == "__main__":
    main()
