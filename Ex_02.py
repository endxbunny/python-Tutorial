from tkinter import *
import random
from tkinter import messagebox

def motionMouse(event):
    btnyes.place(x=random.randint(0, 500), y=random.randint(0, 500))

def no():
    messagebox.showinfo("Thanks bro", "Goodbye")
    quit()

root = Tk()
root.geometry("680x600")
root.title("survey")
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text="Are you gay?", font="Arial 20 bold", bg='white')
label.pack()

btnYes = Button(root, text='No', font='Arial 28 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)

btnNo = Button(root, text='Yes', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=100)

root.mainloop()