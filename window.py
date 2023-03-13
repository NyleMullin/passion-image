from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning to code in tkinter')

top = Toplevel()
top.title('Learning to code in tkinter')
my_image = ImageTk.PhotoImage(Image.open("images/('skier on a', '-', datetime.datetime(2023, 1, 20, 21, 1, 27, 873004)).png"))
my_label = Label(top, image=my_image).pack()

bottom = Toplevel()
bottom.title('Camera?')
time_image = ImageTk.PhotoImage(Image.open("images/('octane ren', '-', datetime.datetime(2023, 1, 20, 20, 30, 34, 280342)).png"))
time_label = Label(bottom, image=time_image).pack()


mainloop()