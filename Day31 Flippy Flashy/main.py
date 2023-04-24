# Import necessary libraries
from tkinter import *
import pandas as pd
import random

# Global variables and dictionaries...  "number_of_days" = Number of days spent learning 
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
todays_list = {}
number_of_days = 1    # 

# Makes sure you have scraped data to read, then adds to the "to_learn" dictionary
try:
    data = pd.read_csv("data/scraped_data.csv")
except FileNotFoundError:
    print("you need to input scraped word data")
else:
    to_learn = data.to_dict(orient="records")

# Gets the current days list to learn by inputing # of Days. ex. Day12 will gather #121-130 and input them into "todays_list"
def get_todays_list(number_of_days):
    global todays_list
    start_index = (number_of_days - 1) * 10
    end_index = start_index + 10
    todays_list = to_learn[start_index:end_index]
    try:
        review_words = pd.read_csv("data/review_words.csv")
    except FileNotFoundError:
        with open("data/review_words.csv", "w") as f:
            f.write("")
    else:
        review_words = data.to_dict(orient="records")
    


def next_card():
    global current_card
    current_card = random.choice(todays_list)
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
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

get_todays_list(number_of_days)
next_card()

todays_list_df = pd.DataFrame(todays_list)
print(todays_list_df.to_string(index=False))

# Bind the <Button-1> event to the canvas
canvas.bind("<Button-1>", flip_card)

window.mainloop()