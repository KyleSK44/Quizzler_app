from tkinter import *

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text="YEETO SKEET0", font=("Arial",20,'italic'))
        self.canvas.grid(column=0, row = 1, columnspan=2)

        img_true = PhotoImage(file='images/true.png')
        img_false = PhotoImage(file="images/false.png")

        self.button_true = Button(image=img_true, highlightthickness=0, )
       # self.button_true.config(padx=20, pady=20)
        self.button_true.grid(column=0, row=3, pady=20, padx=20)


        self.button_false = Button(image=img_false, highlightthickness=0, )
        self.button_false.grid(column=1, row=3, pady=20, padx=20)

        score_lab = Label(text="score: 0", bg=THEME_COLOR,fg=WHITE, highlightthickness=0)
        score_lab.grid(column=1, row=0, padx=20, pady=20)

        self.window.mainloop()