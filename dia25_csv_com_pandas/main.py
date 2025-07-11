from turtle import Turtle, Screen
import pandas

screen = Screen()

image = "blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)
screen.setup(725, 491)
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed('fastest')

states = pandas.read_csv("50_states.csv")

statesanswered = []

while True:
    answer_state = (screen.textinput(title="GUESS THE STATE", prompt="WHATS ANOTHER STATE NAME?")).title()
    if answer_state == 'Exit':
        print("QUITTING")
        screen.exitonclick()
        break
    if answer_state in states.state.values:
        if answer_state not in statesanswered:
            statesanswered.append(answer_state)
            turtle.goto(int(states[states.state == answer_state].x.iloc[0]),int(states[states.state == answer_state].y.iloc[0]))
            turtle.write(answer_state)
            screen.title(f"U.S. STATE GAME ({len(statesanswered)}/50)")
        else:
            print("ALREADY ANSWERED")
        if len(statesanswered) == 50:
            print("YOU WON")
            screen.exitonclick()
            break
    else:
        print("TRY AGAIN")


screen.mainloop()
