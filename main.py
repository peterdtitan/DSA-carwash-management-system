import matplotlib.pyplot as plt
import string
import os
import secrets 
import pandas as pd
from tkinter import *
import customtkinter
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import *


root_tk = customtkinter.CTk()
root_tk.geometry(f"{800}x{700}")
root_tk.title("Dera's Car Wash")



q=[]
customers=[]
charge=[]
counter=0
size = 100

def enqueue(carPlate):
    global size
    if len(q)== size: # check wether the stack is full or not
       print("Queue is full!")
    else:
        q.append(carPlate)

def cusEnqueue(customer):
    global size
    if len(customers)== size: # check wether the stack is full or not
       print("Queue is full!")
    else:
        customers.append(customer)


def dequeue():
    if len(q) != 0:
        e=q.pop(0) 
        root4 = customtkinter.CTk()
        root4.geometry(f"{300}x{200}")
        root4.title("Alert")

        label = customtkinter.CTkLabel(master=root4, text="Car with plate " + e + " is removed!")
        label.pack()

        next = customtkinter.CTkButton(master=root4, text="Okay",command=root4.destroy)
        next.pack(padx=20, pady=10)
    else:
        root5 = customtkinter.CTk()
        root5.geometry(f"{300}x{200}")
        root5.title("Error")

        label = customtkinter.CTkLabel(master=root5, text="Queue is already empty!\n")
        label.pack()

        next = customtkinter.CTkButton(master=root5, text="Okay",command=root5.destroy)
        next.pack(padx=20, pady=10)



def amount(price):
    global size
    if len(charge)== size: # check wether the stack is full or not
       print("Queue is full!")
    else:
        charge.append(price)



def add_automobile():
    prompt = 3
    for i in range(2):
        if i > 0:
            dialog = customtkinter.CTkInputDialog(master=None, text="Type in Plate number:", title="Automobile Plate")
            enqueue(dialog.get_input())
            prompt-=1
            if prompt == 2:
                dialog = customtkinter.CTkInputDialog(master=None, text="Customer First Name:", title="Customer First Name")
                cusEnqueue(dialog.get_input())
                prompt-=1
                if prompt == 1:
                    dialog = customtkinter.CTkInputDialog(master=None, text="Enter amount paid (wihtout $):", title="Amount charged")
                    amount(dialog.get_input())
                    prompt=0



def forward():
    global counter
    counter+=1
    if q[0] is empty:
        root5 = customtkinter.CTk()
        root5.geometry(f"{300}x{200}")
        root5.title("Error")

        label = customtkinter.CTkLabel(master=root5, text="End of queue!\n")
        label.pack()

        next = customtkinter.CTkButton(master=root5, text="Okay",command=root5.destroy)
        next.pack(padx=20, pady=10)
    else:
        queueControl()



def prev():
    global counter

    if counter != 0: 
        counter-=1
        queueControl()
    else:
        root5 = customtkinter.CTk()
        root5.geometry(f"{300}x{200}")
        root5.title("Error")

        label = customtkinter.CTkLabel(master=root5, text="Beginning of Queue!\n")
        label.pack()

        next = customtkinter.CTkButton(master=root5, text="Okay",command=root5.destroy)
        next.pack(padx=20, pady=10)


def queueControl():
        root2 = customtkinter.CTk()
        root2.geometry(f"{400}x{300}")
        root2.title("Manage Queue")

        qframe = customtkinter.CTkFrame(master=root2,
                               width=650,
                               height=200,
                               corner_radius=15)
        qframe.pack(padx=20, pady=20)

        global counter

        car = Label(master=qframe, text="\nNEXT CAR IS: " + q[counter], font=('Century Gothic', 20))
        car.pack()
        name = Label(master=qframe, text="\nCUSTOMER NAME IS: " + customers[counter] + "\n", font=('Century Gothic', 20))
        name.pack()

        next = customtkinter.CTkButton(master=root2, text="Next",command=lambda: [root2.destroy(), forward()])
        next.pack(padx=20, pady=10)
        previous = customtkinter.CTkButton(master=root2, text="Previous",command=lambda: [root2.destroy(), forward()])
        previous.pack(padx=20, pady=10)

        root2.mainloop()



def manage_queue():
    if len(q) != 0:
        queueControl()
    else:
        root5 = customtkinter.CTk()
        root5.geometry(f"{300}x{200}")
        root5.title("Error")

        label = customtkinter.CTkLabel(master=root5, text="Add items to queue first!\n")
        label.pack()

        next = customtkinter.CTkButton(master=root5, text="Okay",command=root5.destroy)
        next.pack(padx=20, pady=10)
  



def finances():
    cur = os.getcwd()
    filename = fd.askopenfilename(
        initialdir=cur)

    name, extension = os.path.splitext(filename)
    if extension == ".csv":
        root2 = customtkinter.CTk()
        root2.geometry(f"{600}x{500}")
        root2.title("Queue")

        df = pd.read_csv(filename)

        figure = plt.Figure(figsize=(6,5), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, root2)
        chart_type.get_tk_widget().pack()
        df = df[['Car Plate','Paid']].groupby('Car Plate').sum()
        df.plot(kind='bar', legend=True, ax=ax)
        ax.set_title('Money per Automobile')

        next = customtkinter.CTkButton(master=root2, text="Close Chart",command=root2.destroy)
        next.pack(padx=20, pady=10)

        print(df)
    else:
        root4 = customtkinter.CTk()
        root4.geometry(f"{200}x{100}")
        root4.title("Error")

        label = customtkinter.CTkLabel(master=root4, text="Please Select a .csv File!")
        label.pack()

        next = customtkinter.CTkButton(master=root4, text="Okay",command=root4.destroy)
        next.pack(padx=20, pady=10)


def remove():
    if len(q) !=0:
        root2 = customtkinter.CTk()
        root2.geometry(f"{400}x{300}")
        root2.title("Manage Queue")

        qframe = customtkinter.CTkFrame(master=root2,
                               width=650,
                               height=200,
                               corner_radius=15)
        qframe.pack(padx=20, pady=20)

        car = Label(master=qframe, text="\nNEXT CAR IS: " + q[0], font=('Century Gothic', 20))
        car.pack()
        name = Label(master=qframe, text="\nCUSTOMER NAME IS: " + customers[0] + "\n", font=('Century Gothic', 20))
        name.pack()

        button = customtkinter.CTkButton(master=frame_2, text="Remove Automobile", width=190, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                   command=dequeue)
        button.pack()

        cancel = customtkinter.CTkButton(master=root2, text="Previous",command=root2.destroy)
        cancel.pack(padx=20, pady=10)
    else:
        root4 = customtkinter.CTk()
        root4.geometry(f"{300}x{200}")
        root4.title("Alert")

        label = customtkinter.CTkLabel(master=root4, text="Enter items in queue first!\n")
        label.pack()

        next = customtkinter.CTkButton(master=root4, text="Okay",command=root4.destroy)
        next.pack(padx=20, pady=10)


def quit():
    print("Thanks for using the app!")
    N = 5
    ran =''.join(secrets.choice(string.ascii_uppercase + string.digits)
                                                  for i in range(N))

    if len(q) !=0:
        df = pd.DataFrame()
        df['Name']  = customers
        df['Car Plate'] = q
        df['Paid'] = charge

        df.to_csv(ran + '.csv',index=False)
    root_tk.destroy()


        
















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
                                   compound="right", command=add_automobile)
button_1.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_2 = customtkinter.CTkButton(master=frame_2, text="Manage Queue", width=190, height=40,
                                   compound="right", fg_color="#006400", hover_color="#228B22",
                                   command=manage_queue)
button_2.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_3 = customtkinter.CTkButton(master=frame_2, text="View Finances", width=190, height=40,
                                   compound="right", fg_color="#006400", hover_color="#228B22",
                                   command=finances)
button_3.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

button_4 = customtkinter.CTkButton(master=frame_2, text="Remove Automobile", width=190, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                   command=remove)
button_4.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")


button_5 = customtkinter.CTkButton(master=frame_2, text="Quit App", width=190, height=40,
                                   compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                   command=quit)
button_5.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")




root_tk.mainloop()

