from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/chinese_vocab.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_word, text=current_card["Character"], fill="black")
    canvas.itemconfig(card_pinyin, text=current_card["Pinyin"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


def flip_card(event):
    if canvas.itemcget(card_title, "text") == "Chinese":
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["Definition"], fill="white")
        canvas.itemconfig(card_pinyin, text="", fill="white")
        canvas.itemconfig(card_background, image=card_back_img)
    else:
        canvas.itemconfig(card_title, text="Chinese", fill="black")
        canvas.itemconfig(card_word, text=current_card["Character"], fill="black")
        canvas.itemconfig(card_pinyin, text=current_card["Pinyin"], fill="black")
        canvas.itemconfig(card_background, image=card_front_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
card_pinyin = canvas.create_text(400, 350, text="", font=("Arial", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

# Bind the <Button-1> event to the canvas
canvas.bind("<Button-1>", flip_card)

window.mainloop()