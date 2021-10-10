from tkinter import*
import random

window = Tk()

window.minsize(750,650)
window.maxsize(750,650)
window.title("Dice roll stimulator")

button=Button(window,text='ROLL THE DICE',font=('italian',27),command=lambda:roll())
button.pack()

label = Label(window,font=('bold',300))
def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()


window.mainloop()
