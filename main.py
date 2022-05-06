from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

s = ""
d = ""


def comboAction(event):
    global s
    global d
    s = comboFrom.get()
    d = comboTo.get()

# Fonction binary
def decimalbinary(x):
    bin_x = bin(x)[2:]
    return bin_x

def binarydecimal(x):
    x = int(x, 2)
    return x

# Fonction octal
def decimaloctal(x):
    oct_x = oct (x)[2:]
    return oct_x

def octaldecimal(x):
    x = int(x, 8)
    return x

# Fonction hexaecimal
def decimalhexadecimal(x):
    hex_x = hex(x)[2:]
    return hex_x

def hexadecimaldecimal(x):
    x = int(x, 16)
    return x


def convert():
    global s
    global d
    if s == "Decimal" and d == "Binary":
            nb = int(fielNumber.get())
            result = decimalbinary(nb)
            fieldResult.delete('1.0', END)
            fieldResult.insert(END, result)
            lblTitle['text'] = 'Convert {} number to {} number'.format (s, d)
            lblNumber['text'] = '{} number'.format (s)
            lblResult['text'] = '{} number'.format (d)


    elif s == "Binary" and d == "Decimal":
            nb = fielNumber.get()
            result = binarydecimal(nb)
            fieldResult.delete('1.0', END)
            fieldResult.insert(END, result)
            lblTitle['text'] = 'Convert {} number to {} number'.format (s, d)
            lblNumber['text'] = '{} number'.format (s)
            lblResult['text'] = '{} number'.format (d)

    elif s == "Decimal" and d == "Octal":
            nb = int(fielNumber.get())
            result = decimaloctal(nb)
            fieldResult.delete('1.0', END)
            fieldResult.insert(END, result)
            lblTitle['text'] = 'Convert {} number to {} number'.format (s, d)
            lblNumber['text'] = '{} number'.format (s)
            lblResult['text'] = '{} number'.format (d)

    elif s == "Octal" and d == "Decimal":
            nb = fielNumber.get()
            result = octaldecimal(nb)
            fieldResult.delete('1.0', END)
            fieldResult.insert(END, result)
            lblTitle['text'] = 'Convert {} number to {} number'.format (s, d)
            lblNumber['text'] = '{} number'.format (s)
            lblResult['text'] = '{} number'.format (d)

    elif s == "Decimal" and d == "Hexadecimal":
            nb = int(fielNumber.get())
            result = decimalhexadecimal(nb)
            fieldResult.delete('1.0', END)
            fieldResult.insert(END, result)
            lblTitle['text'] = 'Convert {} number to {} number'.format (s, d)
            lblNumber['text'] = '{} number'.format (s)
            lblResult['text'] = '{} number'.format (d)

    elif s == "Hexadecimal" and d == "Decimal":
            nb = fielNumber.get()
            result = hexadecimaldecimal(nb)
            fieldResult.delete('1.0', END)
            fieldResult.insert(END, result)
            lblTitle['text'] = 'Convert {} number to {} number'.format(s, d)
            lblNumber['text'] = '{} number'.format (s)
            lblResult['text'] = '{} number'.format (d)

root = tk.Tk()
root.geometry('400x500')
root.resizable(width=False,height=False)
root.configure(bg='#3c3f41')
root.title('Converter')
lblTitle = Label(root, text='Converter', font=("Segoe UI", 15), bg="#3c3f41", fg='#ccc')
lblTitle.pack()
lblFrom = Label(root, text="From", font=("Segoe UI", 18), bg="#3c3f41", fg='#ccc')
lblFrom.place(x=20, y=120)
list = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']

comboFrom = ttk.Combobox(root, values=list,font=("Segoe UI", 18))
comboFrom.place(x=20, y=160, width=170, height=30)
comboFrom['state'] = 'readonly'
comboFrom.current(0)
comboFrom.bind("<<ComboboxSelected>>", comboAction)

lblTo = Label(root, text="To", font=("Segoe UI", 18), bg="#3c3f41", fg='#ccc')
lblTo.place(x=210, y=120)

comboTo = ttk.Combobox(root, values=list,font=("Segoe UI", 18))
comboTo.place(x=210, y=160, width=170, height=30)
comboTo['state'] = 'readonly'
comboTo.current(1)
comboTo.bind("<<ComboboxSelected>>", comboAction)



lblNumber= Label(root, text="Enter Number", font=("Segoe UI", 18), bg="#3c3f41", fg='#ccc')
lblNumber.place(x=20, y=200)
fielNumber = Entry(root, font=("Segoe UI", 18))
fielNumber.place(x=20, y=240, width=235, height=40)
btn = Button(root, text="= Convert", font=("Segoe UI", 18), bg='#0069d9', fg="#fff", command=lambda: convert())
btn.place(x=260, y=240, width=120, height=40)


lblResult= Label(root, text="Result", font=("Segoe UI", 18), bg="#3c3f41", fg='#ccc')
lblResult.place(x=20, y=300)
fieldResult = Text(root, font=("Segoe UI", 25))
# fieldResult.config(state=En
fieldResult.place(x=20, y=340, width=360, height=60)

lbl= Label(root, text="Application créée par RedCoding", font=("Segoe UI", 8), bg="#3c3f41", fg='#ccc')
lbl.place(x=100, y=480)

root.mainloop()
