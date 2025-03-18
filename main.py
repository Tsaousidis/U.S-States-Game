import turtle
import pandas

def draw_state(state_data):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())

def save_missing_states(all_states, guessed_states):
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("States_to_learn.csv")

def get_user_input(screen, guessed_states):
    return screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", 
                            prompt="What's another state's name?").title()

def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = get_user_input(screen, guessed_states)
        if answer_state == "Exit":
            save_missing_states(all_states, guessed_states)
            break
        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            draw_state(state_data)

if __name__ == "__main__":
    main()
