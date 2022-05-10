from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# words_read_csv_file
try:
    data = pandas.read_csv("words_to_learn.csv")
    dict_data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/arabic_words.csv")
    dict_data = data.to_dict(orient="records")


# Button_functions

def next_word():
    global timer, random_words
    window.after_cancel(timer)
    random_words = random.choice(dict_data)
    new_word = random_words["ENGLISH"]
    my_canvas.itemconfig(img_card, image=front_img)
    my_canvas.itemconfig(target_word, text=new_word)
    my_canvas.itemconfig(card_title, text="English")
    timer = window.after(3000, fliper)
    my_canvas.itemconfig(target_word, text=new_word, fill="black")
    my_canvas.itemconfig(card_title, text="English", fill="black")


# flipping_card_functions

def fliper():
    global random_words
    new_word = random_words["ARABIC"]
    my_canvas.itemconfig(img_card, image=back_end_img)
    my_canvas.itemconfig(target_word, text=new_word, fill="white")
    my_canvas.itemconfig(card_title, text="Arabic", fill="white")


# is_known_function

def is_known():
    global random_words
    dict_data.remove(random_words)
    data = pandas.DataFrame(dict_data)
    data.to_csv("data\words_to_learn.csv", index=False)
    next_word()


# Window_GUI

window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.iconbitmap('images/translate.ico')
window.resizable(False, False)

timer = window.after(3000, fliper)

# Canvas
my_canvas = Canvas(width=800, heigh=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_end_img = PhotoImage(file="images/card_back.png")
img_card = my_canvas.create_image(400, 263, image=front_img)
card_title = my_canvas.create_text(400, 120, text="", font=("Arial", 40, "italic"))
target_word = my_canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))
my_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known,borderwidth=0)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word,borderwidth=0)
wrong_button.grid(row=1, column=0)

next_word()

window.mainloop()
