from importlib.resources import path
import pathlib
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import customtkinter

root_tk = customtkinter.CTk()
root_tk.geometry(f"{800}x{700}")
root_tk.title("Dera's Car Wash")



q=[]
size = 100

def enqueue(carPlate):
    global size
    if len(q)== size: # check wether the stack is full or not
       print("Queue is full!")
    else:
        carPlate=input("Enter the element:")
        q.append(carPlate)

def dequeue(carPlate):
    if not q or len(q)==0:
        print("Queue is Empty!!!")
    else:
        e=q.pop(0)
        print("element removed!!:",e)



frame = customtkinter.CTkFrame(master=root_tk,
                               width=650,
                               height=200,
                               corner_radius=15)
frame.pack(padx=20, pady=20)

#frame.configure(fg_color='', bg_color=..., corner_radius=...)

logo_label = Label(master=frame, text = "\nDERA'S CAR WASH", font=('Century Gothic', 60))
logo_label.pack()

greet = Label(master=frame, text="Premium wash experience for your automobile", font=('Century Gothic', 18))
greet.pack()

version_info = Label(master=frame, text="\n\nVersion 1.0.1.1\n", font=('Century Gothic', 13))
version_info.pack()

# Home Screen Menu Buttons
# Define frame to hold buttons for executing functions in the CLI and interacting with the GUI

frame_2 = customtkinter.CTkFrame(master=root_tk, width=250, height=240, corner_radius=15)
frame_2.pack()

button_1 = customtkinter.CTkButton(master=frame_2, text="Add Automobile", width=190, height=40,
                                   compound="right")
button_1.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_2 = customtkinter.CTkButton(master=frame_2, text="Check Next in Queue", width=190, height=40,
                                   compound="right", fg_color="#006400", hover_color="#228B22",
                                   )
button_2.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_3 = customtkinter.CTkButton(master=frame_2, text="View Finances", width=190, height=40,
                                   compound="right", fg_color="#006400", hover_color="#228B22",
                                   )
button_3.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_4 = customtkinter.CTkButton(master=frame_2, text="Remove Automobile", width=190, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                   )
button_4.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")


button_5 = customtkinter.CTkButton(master=frame_2, text="Close Car Wash", width=190, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                   )
button_5.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")




root_tk.mainloop()