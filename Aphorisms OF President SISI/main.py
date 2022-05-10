from tkinter import *
from tkinter import messagebox

#button_functions
def open_page():
    window.destroy()
    import page1


def close_page():
    user_choice = messagebox.askyesno('Confirmation', message='Do you want to quit this application?')
    if user_choice:
        messagebox.showinfo('Exiting..', 'Exiting Application')
        window.destroy()
    else:
        messagebox.showinfo('', 'Thanks For Staying')

#closing_function
def on_close():
    response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
    if response:
        window.destroy()

#window_setup
window = Tk()
window.title("Aphorisms of President SISI")
window.resizable(False, False)
window.protocol('WM_DELETE_WINDOW', on_close)
window.iconbitmap('images/p_sisi.ico')

window.geometry("981x588")
window.configure(bg="#FFFFFF")

#Canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=588,
    width=981,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="images/background.png")
background = canvas.create_image(
    490.5, 294.0,
    image=background_img)

#buttons
img0 = PhotoImage(file=f"images/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=close_page,
    relief="flat")

b0.place(
    x=643, y=309,
    width=166,
    height=48)

img1 = PhotoImage(file=f"images/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=open_page,
    relief="flat")

b1.place(
    x=643, y=212,
    width=166,
    height=48)

window.mainloop()
