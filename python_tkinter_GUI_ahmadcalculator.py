from tkinter import *
from tkinter import ttk

def b1():
    text_area.insert(END, '1')
def b2():
    text_area.insert(END, '2')
def b3():
    text_area.insert(END, '3')
def b4():
    text_area.insert(END, '4')
def b5():
    text_area.insert(END, '5')
def b6():
    text_area.insert(END, '6')
def b7():
    text_area.insert(END, '7')
def b8():
    text_area.insert(END, '8')
def b9():
    text_area.insert(END, '9')
def b0():
    text_area.insert(END, '0')

def add_operator(operator):
    text_area.insert(END, operator)

def clear():
    text_area.delete("1.0", END)

def calculate():
    try:
        expression = text_area.get("1.0", END).strip()
        result = eval(expression) 
        text_area.delete("1.0", END)  
        text_area.insert(END, result)  
    except Exception as e:
        text_area.delete("1.0", END)
        text_area.insert(END, 'Error')

bgc = '#6000e7'

calc = Tk()
calc.title('CALCULATOR')
calc.geometry('700x700')
calc.config(bg='#37db5d')

label = Label(calc, text="""AHMAD'S CALCULATOR""", font=('Segeo UI', 40, 'bold'), bg='#37db5d')
label.place(x=30, y=30, height=50, width=640)

text_area = Text(calc, font=('Segeo UI',40,'bold'))
text_area.place(x=30, y=110, height=60, width=640)

button1 = Button(calc, text='1', font=('Segeo UI',80,'bold'), bg=bgc, command=b1)
button1.place(x=30, y=200, height=102, width=130)

button2 = Button(calc, text='2', font=('Segeo UI',80,'bold'), bg=bgc, command=b2)
button2.place(x=180, y=200, height=102, width=130)

button3 = Button(calc, text='3', font=('Segeo UI',80,'bold'), bg=bgc, command=b3)
button3.place(x=330, y=200, height=102, width=130)

button4 = Button(calc, text='4', font=('Segeo UI',80,'bold'), bg=bgc, command=b4)
button4.place(x=30, y=332, height=102, width=130)

button5 = Button(calc, text='5', font=('Segeo UI',80,'bold'), bg=bgc, command=b5)
button5.place(x=180, y=332, height=102, width=130)

button6 = Button(calc, text='6', font=('Segeo UI',80,'bold'), bg=bgc, command=b6)
button6.place(x=330, y=332, height=102, width=130)

button7 = Button(calc, text='7', font=('Segeo UI',80,'bold'), bg=bgc, command=b7)
button7.place(x=30, y=464, height=102, width=130)

button8 = Button(calc, text='8', font=('Segeo UI',80,'bold'), bg=bgc, command=b8)
button8.place(x=180, y=464, height=102, width=130)

button9 = Button(calc, text='9', font=('Segeo UI',80,'bold'), bg=bgc, command=b9)
button9.place(x=330, y=464, height=102, width=130)

button0 = Button(calc, text='0', font=('Segeo UI',80,'bold'), bg=bgc, command=b0)
button0.place(x=180, y=590, height=102, width=130)

button_modulo = Button(calc, text='%', font=('Segeo UI',80,'bold'), bg=bgc, command=lambda: add_operator('%'))
button_modulo.place(x=30, y=590, height=102, width=130)

button_clear = Button(calc, text='C', font=('Segeo UI',80,'bold'), bg=bgc, command=clear)
button_clear.place(x=330, y=590, height=102, width=130)

button_plus = Button(calc, text='+', font=('Segeo UI',80,'bold'), bg=bgc, command=lambda: add_operator('+'))
button_plus.place(x=480, y=200, height=102, width=130)

button_minus = Button(calc, text='-', font=('Segeo UI',80,'bold'), bg=bgc, command=lambda: add_operator('-'))
button_minus.place(x=480, y=332, height=102, width=130)

button_multi = Button(calc, text='x', font=('Segeo UI',80,'bold'), bg=bgc, command=lambda: add_operator('*'))
button_multi.place(x=480, y=464, height=102, width=130)

button_div = Button(calc, text='/', font=('Segeo UI',80,'bold'), bg=bgc, command=lambda: add_operator('/'))
button_div.place(x=480, y=590, height=102, width=130)

button_eq = Button(calc, text='=', font=('Segeo UI',80,'bold'), bg='#640000', command=calculate)
button_eq.place(x=622, y=200, height=490, width=70)

calc.mainloop()
