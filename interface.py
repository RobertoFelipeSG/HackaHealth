import tkinter as tk
import time
from tkinter import *
from tkinter import font
from tkinter import Button
from PIL import Image, ImageTk
from time import sleep

win = tk.Tk()

myFont = tk.font.Font(family = 'Helvetica', size = 30, weight = 'bold')

WIDTH, HEIGHT = 320, 320
images = {'A': 'Peppa-Pig.png'}#, 'B': 'myimage.jpg'}

entry = Text(win, width=30, height=8, font=("Helvetica", 30))
entry.grid(row=0, column=0, columnspan=11)
curBut = [-1,-1]
buttonL = [[]]

varRow = 1
varColumn = 0

#sec = 0 
#label = tk.Label(win, fg="dark green", font = myFont)
#label.grid(row=6, column=0)

#def clock(sec):
#	if sec!=0:
#		sec-=1
#		count = sec
#		label.configure(text=sec)
#		label.after(1000, clock(sec=sec))
#	if sec == 0:
#		sec = 5
 
def batch_resize():

	for k, v in images.items():
		v = Image.open(v).resize((WIDTH, HEIGHT), Image.ANTIALIAS)
		images[k] = ImageTk.PhotoImage(v)

def disp(button):
	button.invoke()

def leftKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red', highlightthickness=4)
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        curBut[:] = [0,10]
        buttonL[0][10].configure(highlightbackground='red', highlightthickness=4)
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        curBut[:] = [curBut[0], (curBut[1]-1)%11]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red', highlightthickness=4)

def rightKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red', highlightthickness=4)
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red', highlightthickness=4)
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        curBut[:] = [curBut[0], (curBut[1]+1)%11]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red', highlightthickness=4)

def upKey(event):
    if curBut == [-1,-1]:
        disp(buttonL[0][0])
    elif curBut[0] == 0:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        disp(buttonL[curBut[0]][curBut[1]])
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        disp(buttonL[curBut[0]][curBut[1]])

def downKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red', highlightthickness=4)
    elif curBut[0] == 3:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        curBut[:] = [(curBut[0]+1)%5, 0]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red', highlightthickness=4)
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
        curBut[:] = [(curBut[0]+1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red', highlightthickness=4)

def select(value, x, y):
    if curBut != [-1,-1]:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9', highlightthickness=4)
    curBut[:] = [x,y]
    buttonL[x][y].configure(highlightbackground='red', highlightthickness=4)
    if value == "<-":
        txt = entry.get("1.0", tk.END)
        entry.delete("1.0", tk.END)
        entry.insert(tk.END, txt[:-2])
    elif value == " Space ":
        entry.insert(tk.END, ' ')
    else:
        entry.insert(tk.END, value)

def exitProgram():
    print("Exit Button pressed")
    win.quit()

win.title("Peppa's Keyboard")
win.geometry('1300x720')

buttons = [    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Ent',
    ' Space ',]

batch_resize()

l1 = tk.Label(win)
image1 = images['A']
l1['image'] = image1	
l1.grid(row=0, column=12, rowspan=1	)


for button in buttons:
    if button != " Space ":
        but = tk.Button(win, text=button, width=2, height=1, bg="#ffb6c1",activebackground="#ffffff", font =myFont,	activeforeground="#000000", highlightthickness=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(but)
        but.grid(row=varRow, column=varColumn)
    if button == " Space ":
        but = tk.Button(win, text=button, width=10, height=1, bg="#000000", fg="#ffffff", highlightthickness=4, font =myFont, activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=4,
                       pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
        buttonL[varRow-1].append(but)
        but.grid(row=5, columnspan=11)
    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
        buttonL.append([])

win.bind('<Left>', leftKey)
win.bind('<Right>', rightKey)
win.bind('<Up>', upKey)
win.bind('<Down>', downKey)


win.mainloop()
