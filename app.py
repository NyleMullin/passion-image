from auth import auth_token
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import requests
import datetime

# pip install openai
import openai

openai.api_key = auth_token

# Create App
app = tk.Tk()
app.geometry("1920x1080")
app.title("DALL E")
ctk.set_appearance_mode("dark")

main_image = tk.Canvas(app, width=1920, height=1080)
main_image.place(x=0, y=0)

# master = tk.Tk()

prompt_input = ctk.CTkEntry(
    master=None,
    height=40,
    width=512,
    font=("Arial", 20),
    text_color="black",
    fg_color="white",
    corner_radius=10,
    placeholder_text="Enter a prompt.",
)
prompt_input.place(x=1080, y=10)

def create_image():
    global tk_img
    global img

    prompt = prompt_input.get()
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url, stream=True).raw)
    tk_img = ImageTk.PhotoImage(img)
    main_image.create_image(0, 0, anchor=tk.NW, image=tk_img)

def save_image():
    global img
    date = datetime.datetime.now()
    prompt = prompt_input.get()[:10]
    label =  (prompt,"-", date)
    img.save(f"images/{label}.png")

magic_button = ctk.CTkButton(
    master=None,
    height=40,
    width=120,
    font=("Arial", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=create_image,
)
magic_button.configure(text="Create Image")
magic_button.place(x=1080, y=55)

save_button = ctk.CTkButton(
    master=None,
    height=40,
    width=120,
    font=("Arial", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=save_image,
)
save_button.configure(text="Save Image")
save_button.place(x=1250, y=55)

app.mainloop()