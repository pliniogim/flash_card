from tkinter import *
from util import *

BACKGROUND_COLOR = "#B1DDC6"


# screen section
screen = Tk()
screen.title("Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas section
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526)
card_front = PhotoImage(data=CARD_FRONT)
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

# button section
# right button
r_button_img = PhotoImage(data=BUTTON_RIGHT)
r_button = Button(image=r_button_img, highlightthickness=0, bg=BACKGROUND_COLOR)

# wrong button
w_button_img = PhotoImage(data=BUTTON_WRONG)
w_button = Button(image=w_button_img, highlightthickness=0, bg=BACKGROUND_COLOR)

w_button.grid(row=1, column=0)
r_button.grid(row=1, column=1)





screen.mainloop()
