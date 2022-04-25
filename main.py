import turtle
from brain import Brain

screen = turtle.Screen()
screen.title("U.S. State Game")
# map_img = "./countries.gif"
map_img = "./blank_states_img.gif"
# screen.setup(width=1000, height=1000)
turtle.addshape(map_img)
turtle.shape(map_img)

""" TIP:

How to get desired coordinates for your maps
"""


# def save_coor(x, y):
#     coordinate = (x, y)
#     print(coordinate)

#     with open(file="./cor_list.txt", mode="a") as file:
#         file.write(str(coordinate))


# turtle.onscreenclick(save_coor)
# turtle.mainloop()

brain = Brain("./50_states.csv")

while len(brain.answers) < 50:
    answer = brain.get_answer()

    if answer == "exit":
        brain.save_notes()
        break

    brain.check_answer(answer)
