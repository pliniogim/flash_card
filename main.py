from tkinter import *
from util import *
import pandas
import random
import datetime

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
to_learn = pandas.DataFrame.to_dict(data, orient="records")


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="green")
    canvas.itemconfig(card_word, text=current_card["English"], fill="green")
    canvas.itemconfig(cv_card_back, image=card_background)


def process_w():
    global current_card, timer_clc
    screen.after_cancel(timer_clc)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    card_front = PhotoImage(data=CARD_FRONT)
    cv_card_front = canvas.create_image(400, 263, image=card_front)
    canvas.itemconfig(cv_card_front, image=card_front)
    timer_clc = screen.after(3000, func=flip_card)


# screen section
screen = Tk()
screen.title("Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer_clc = screen.after(3000, func=flip_card)

# canvas section
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)

card_background = PhotoImage(data=CARD_BACK)
cv_card_back = canvas.create_image(400, 263, image=card_background)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

# button section
# right button
r_button_img = PhotoImage(data=BUTTON_RIGHT)
r_button = Button(image=r_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=process_w)

# wrong button
w_button_img = PhotoImage(data=BUTTON_WRONG)
w_button = Button(image=w_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=process_w)

w_button.grid(row=1, column=0)
r_button.grid(row=1, column=1)

process_w()

screen.mainloop()
