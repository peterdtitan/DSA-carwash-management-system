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



def button_click_event():
    dialog = customtkinter.CTkInputDialog(master=None, text="Type in a number:", title="Test")
    enqueue(dialog)
    print(q)
    



frame_2 = customtkinter.CTkFrame(master=root_tk, width=250, height=240, corner_radius=15)
frame_2.pack()

button_1 = customtkinter.CTkButton(master=frame_2, text="Add Automobile", width=190, height=40,
                                   compound="right", command=button_click_event)
button_1.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_2 = customtkinter.CTkButton(master=frame_2, text="Check Next in Queue", width=190, height=40,
                                   compound="right", fg_color="#00FF00", hover_color="#90EE90",
                                   )
button_2.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_3 = customtkinter.CTkButton(master=frame_2, text="Remove Automobile", width=190, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                   )
button_3.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")


button_4 = customtkinter.CTkButton(master=frame_2, text="Close Car Wash", width=190, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                   )
button_4.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")


# Buttons for home screen functions



root_tk.mainloop()