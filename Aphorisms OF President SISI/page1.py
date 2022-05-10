from tkinter import *
from data import article_data
from pprint import pprint
import random
from tkinter import messagebox

#button_function
def get_quote():
    rand_quot = random.choice(article_data)
    quote = rand_quot[0].replace("-", " ").replace(".", " ").strip()

    canvas.itemconfig(quote_text, text=quote)

#window_setup
window = Tk()
window.title("Aphorisms of President SISI")
window.config(padx=50, pady=50)
window.resizable(False, False)
window.iconbitmap('images/p_sisi.ico')

#closing_function
def on_close():
    response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
    if response:
        window.destroy()


window.protocol('WM_DELETE_WINDOW', on_close)

#Canvas
canvas = Canvas(width=400, height=306)
background_img = PhotoImage(file="images/bg.png")
canvas.create_image(200, 150, image=background_img)
quote_text = canvas.create_text(200, 145, text="!.... سيادة الرئيس السيسى يقول",
                                font=("time new roman", 15, "bold"), fill="black", width=250, anchor=CENTER,
                                justify=RIGHT)
canvas.grid(row=0, column=0)

#button
p_SiSi_img = PhotoImage(file="images/p_sisi.png")
p_Sisi_button = Button(image=p_SiSi_img, highlightthickness=0, command=get_quote)
# p_Sisi_button["border"] = "0"
p_Sisi_button.grid(row=1, column=0)

window.mainloop()
