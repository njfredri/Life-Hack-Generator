from tkinter import *
import time
import threading
import fileinput
import sys
import textGenerator
import os
from winsound import *

killThreads = False
window = Tk()
window.title("MCCM")

Label (window, text="Lets Craft These 5 Minute Crafts!!!", font="none 12 bold").grid(row=0, column=0, sticky=W)

filename = Entry(window, width=15)
filename.grid(row=0, column = 1, sticky=W)

def saveFile():
    #print(filename.get())
    if not os.path.exists("output"):
        os.mkdir("output")
    open("output/" + filename.get() + ".txt", "w")
    with open("temp.txt") as f:
        with open("output/" + filename.get() + ".txt", "w") as f1:
            for line in f:
                f1.write(line)
            f1.close()
            f.close()
    #window.title(filename.get())

def genText():
    tg = textGenerator.textGenerator()
    tg.generateText()
    readyFile = open("ready.txt", "w")
    readyFile.write("yo")
    readyFile.close()

tgThread = threading.Thread(target=genText)

def startgentext():
    tempfile = open('temp.txt','w')
    tempfile.truncate(0)
    tempfile.close()
    tgThread.start()
    

Button(window, text="Save File", width = 10, command=saveFile).grid(row = 1, column = 1, sticky=W)

output = Text(window, width = 100, height = 20, font="none 15", wrap=WORD)
output.grid(row = 5, column = 0, columnspan=5)
output.insert(END, "Try Generating some life hacks!")

def updateText():
    dots = 1
    while not os.path.isfile("ready.txt"):
        print("generating, waiting for file generation...")
        output.delete('1.0', END)
        output.insert(END, "Generating" + (dots*"."))
        time.sleep(0.3)
        dots += 1
        dots = dots % 4
    output.delete('1.0', END)
    os.remove("ready.txt")
    f = open("temp.txt", "r")
    output.insert(END, f.read())
    f.close()

def startUpdateTextThread():
    fileThread = threading.Thread(target=updateText)
    fileThread.start()
    startgentext()

Button(window, text="Generate", width = 9, command=startUpdateTextThread).grid(row= 1, column = 0, sticky = W)

def close_window():
    #killThreads = True
    window.destroy()
    exit()
Button(window, text="Exit", width = 12, command=close_window).grid(row=1, column = 4)

play = lambda: PlaySound('monkey-rap.wav', SND_FILENAME | SND_ASYNC)
button = Button(window, text = 'Play Music', height = 2, command = play)
button.grid(row = 0, column = 4)
window.mainloop()