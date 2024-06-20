from tkinter import *
from util import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def flip_card():
    global current_card, timer_clc
    screen.after_cancel(timer_clc)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(cd_background, image=card_back_image)
    timer_clc = screen.after(3000, func=process_w)


def process_w():
    global current_card, timer_clc
    screen.after_cancel(timer_clc)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(cd_background, image=card_front_image)
    timer_clc = screen.after(3000, func=flip_card)


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    process_w()


def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# screen section
screen = Tk()
screen.title("Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer_clc = screen.after(3000, func=flip_card)

# canvas section
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)

card_front_image = PhotoImage(data=CARD_FRONT)
card_back_image = PhotoImage(data=CARD_BACK)
cd_background = canvas.create_image(400, 263, image=card_back_image)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

# button section
# right button
r_button_img = PhotoImage(data=BUTTON_RIGHT)
r_button = Button(image=r_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)

# wrong button
w_button_img = PhotoImage(data=BUTTON_WRONG)
w_button = Button(image=w_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)

w_button.grid(row=1, column=0)
r_button.grid(row=1, column=1)

next_card()

screen.mainloop()
