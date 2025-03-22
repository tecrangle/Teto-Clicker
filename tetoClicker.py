from tkinter import *

teto = Tk()

teto.geometry("350x350")
teto.title("teto clicker")

label = Label(teto, text=("teto clicker game"), font=('Comic Sans MS', 18))
label.pack(padx=20, pady=20)

image = PhotoImage(file = "D:\\personal\\code\\python\\tetoClicker\\teto4.png")

# sets the base clicks to 0
totalClicks = 0
# function to increase the clicks
def addClick():
    global totalClicks
    totalClicks += 1
    clickLabel.configure(text = f"tetos clicked: {totalClicks}")
# is the counter
button = Button(teto, image = image, command = addClick)
button.pack()
clickLabel = Label(teto, text = "tetos clicked: 0", font = ('Comic Sans MS', 14))
clickLabel.pack(pady = 5)

teto.mainloop()