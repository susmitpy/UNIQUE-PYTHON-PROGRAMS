#Make a calculator which will accept data in GUI and will Return data in GUI

#import
from tkinter import *
#define
def cal():

    num1 = e1.get()
    operator=e2.get()
    num2=e3.get()
    num1 = int(num1)
    num2=int(num2)
    #tell what occurs when
    if operator == '+':
        r = ("{0} + {1} = {2}".format(num1, num2, num1+num2))
    elif operator == '-':
        r = ("{0} - {1} = {2}".format(num1, num2, num1-num2))  
    elif operator == '*':
        r = ("{0} * {1} = {2}".format(num1, num2, num1*num2))
    elif operator == '/':
        r = ("{0} / {1} = {2}".format(num1, num2, num1/num2))
    elif operator == 'R':
        r = ("The remainder of {0}/{1} is {2}".format(num1, num2, num1%num2))
    elif operator == 'E':
        r = ("{0}^{1} = {2}".format(num1, num2, num1**num2))    
        
    #create output gui
    result = Tk()
    result.title("Answer")
    Label(result, text=r).pack()
    ok = Button(result, text="OK", command=result.destroy)
    ok.pack()

def clear():               #CLEAR THE CONTENTS
    e1.delete(0)
    e2.delete(0)
    e3.delete(0) 
    
#create input gui
enter = Tk()
enter.title("Calculator")
Label(enter, text="First Number").grid(row=0)
Label(enter, text="Operator(+,-,*,/,R(for finding remainder),E(for exponent)").grid(row=1)
Label(enter, text="Second Number").grid(row=2)
e1 = Entry(enter)
e2 = Entry(enter)
e3 = Entry(enter)
e1.grid(row = 0, column=1)
e2.grid(row = 1, column=1)
e3.grid(row = 2, column=1)
calculate = Button(enter, text="Calculate", command=cal)
qui = Button(enter, text="Quit", command = quit)
clr = Button(enter, text="Clear", command = clear)
calculate.grid(row=3)
clr.grid(row=3, column = 1)
qui.grid(row=3, column=2)


