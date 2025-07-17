import tkinter as tk
from tkinter import *


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm():
    pass

def hcf():
    pass


def extract_from_text(text):
    l = []
    for i in text.split(' '):
        try:
            l.append(float(i))
        except ValueError:
            pass    
    return l


def calculate():
    text = textin.get().upper()
    tokens = text.split(' ')
    result = None
    current_op = None
    
    for token in tokens:
        if token in operations:
            current_op = operations[token]
        else:
            try:
                num = float(token)
                if result is None:
                    result = num
                elif current_op:
                    result = current_op(result, num)
                    current_op = None
                else:
                    list.delete(0, END)
                    list.insert(END, 'Invalid syntax.')
                    return
            except ValueError:
                continue
            
    if result is not None:
        list.delete(0, END)
        list.insert(END, result)
    else:
        list.delete(0, END)
        list.insert(END, 'Invalid input.')

    
 

#operations defined
operations = {'ADD' : add, 'ADDITION' : add, 'PLUS' : add, '+' : add,
              'SUB' : sub, 'DIFFERENCE' : sub, 'MINUS' : sub, 'SUBTRACT': sub, 'DIFF' : sub,'-' : sub,
              'LCM' : lcm, 'HCF' : hcf, 
              'PRODUCT' : mul, 'MULTIPLICATION' : mul, 'MULTIPLY' : mul, '*' : mul,
              'DIVISION' : div, 'DIV' : div, 'DIVIDE' : div, '/' : div,
              'MOD' : mod, 'REMAINDER' : mod, 'MODULUS' : mod, '%' : mod,
              }


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Smart Calculator')
    root.geometry('500x300')
    root.configure(bg='lightskyblue')

    root.resizable(0, 0)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
    root.columnconfigure(2, weight=1)

    # UI kind of
    l1 = Label(root, text='I am a smart calculator', width=20)
    l1.grid(column=1, row=1, padx=5, pady=10)

    l2 = Label(root, text='My name is Calc-U', width=20)
    l2.grid(column=1, row=2, padx=5, pady=10)

    l3 = Label(root, text='What can I help you?', width=20)
    l3.grid(column=1, row=3, padx=5, pady=10)

    textin = StringVar()
    e1 = Entry(root, width=30, textvariable=textin)
    e1.grid(column=1, row=4, padx=5, pady=10)

    b1 = Button(root, text='Just this', command=calculate)
    b1.grid(column=1, row=5, padx=5, pady=10)

    list = Listbox(root, width=40, height=3)
    list.grid(column=1, row=6, padx=5, pady=10)

    root.mainloop()