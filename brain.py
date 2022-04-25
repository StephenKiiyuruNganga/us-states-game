from turtle import Screen, Turtle
import pandas


FONT = ("atlan", 10, "normal")
FONT_COLOUR = "red"
ALIGNMENT = "center"


class Brain(Turtle):
    def __init__(self, file):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(FONT_COLOUR)
        self.df = self.get_data(file)
        self.screen = Screen()
        self.answers = []

    def get_data(self, file):
        return pandas.read_csv(file)

    def write_text(self, text, x_cor=0, y_cor=0):
        """ writes text on screen

        Arguments:
        :text: the text to be displayed
        :x_cor: x coordinate for the text. Default 0
        :y_cor: y coordinate for the text. Default 0
        """
        self.goto(x=x_cor, y=y_cor)
        self.write(text, align=ALIGNMENT, font=FONT)

    def check_answer(self, answer):
        converted_ans = answer.title()
        answer_df = self.df[self.df.state == converted_ans]

        if len(answer_df):
            self.write_text(answer_df.state.item(),
                            int(answer_df.x),
                            int(answer_df.y))
            self.answers.append(answer_df.state.item())

    def get_answer(self):
        title = f"{len(self.answers)}/{len(self.df)} Correct" if len(
            self.answers) > 0 else "Guess the state"
        return self.screen.textinput(title=title,
                                     prompt="What's another state's name?")

    def save_notes(self):
        all_states = self.df.state.to_list()
        missing_sates = set(all_states).difference(self.answers)

        summary_dict = {"missing_sates": sorted(list(missing_sates))}
        df = pandas.DataFrame(summary_dict)
        df.to_csv("./missing_states.csv")
