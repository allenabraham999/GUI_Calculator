from tkinter import *
import parser
import math
i = 0
def get_input(num):
    global i
    display.insert(i,num)
    i+=1
def clear_all():
    display.delete(0,END)

def undo_func():
    current_string = display.get()
    if len(current_string)>0 :
        new_string = current_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        display.insert(0,"Error")
# Python Program to Count Number of Digits in a Number using While loop
def number_counter(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return Count
def get_operation(opd):
    global i
    length = len(opd)
    display.insert(i,opd)
    i+=length

def fact():
    num = display.get()
    number = int(num[-1:])
    size = number_counter(number)
    undo_func()
    if number != 0:
        return math.factorial(number)
    else:
        return 1
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except EXCEPTION:
        clear_all()
        display.insert(0,"error")

window = Tk()
window.title("calculator")
display = Entry(window)
display.grid(row = 1, columnspan = 6)
Button(window,text="1",command = lambda:get_input(1)).grid(row = 2, column= 0)
Button(window,text="2",command = lambda:get_input(2)).grid(row = 2, column= 1)
Button(window,text="3",command = lambda:get_input(3)).grid(row = 2, column= 2)
Button(window,text="4",command = lambda:get_input(4)).grid(row = 3, column= 0)
Button(window,text="5",command = lambda:get_input(5)).grid(row = 3, column= 1)
Button(window,text="6",command = lambda:get_input(6)).grid(row = 3, column= 2)
Button(window,text="7",command = lambda:get_input(7)).grid(row = 4, column= 0)
Button(window,text="8",command = lambda:get_input(8)).grid(row = 4, column= 1)
Button(window,text="9",command = lambda:get_input(9)).grid(row = 4, column= 2)

Button(window, text = "AC",command= lambda:clear_all()).grid(row=5, column = 0)
Button(window, text = "0",command = lambda:get_input(0)).grid(row = 5, column = 1)
Button(window, text = "=",command = lambda:calculate()).grid(row = 5, column = 2)


Button(window, text = "+",command = lambda :get_operation("+")).grid(row = 2, column = 3)
Button(window, text = "-",command = lambda :get_operation("-")).grid(row = 3, column = 3)
Button(window, text = "*",command = lambda :get_operation("*")).grid(row = 4, column = 3)
Button(window, text = "/",command = lambda :get_operation("/")).grid(row = 5, column = 3)

Button(window, text = "pi",command =lambda : get_operation("*3.14")).grid(row = 2, column = 4)
Button(window, text = "%",command = lambda :get_operation("%")).grid(row = 3, column = 4)
Button(window, text = "(",command = lambda :get_operation("(")).grid(row = 4, column = 4)
Button(window, text = "exp",command = lambda :get_operation("**")).grid(row = 5, column = 4)


Button(window, text = "<-",command = lambda :undo_func()).grid(row = 2, column = 5)
Button(window, text = "x!",command = lambda :get_operation(f"{fact()}")).grid(row = 3, column = 5)
Button(window, text = ")",command = lambda :get_operation(")")).grid(row = 4, column = 5)
Button(window, text = "x^2",command = lambda :get_operation("**2")).grid(row = 5, column = 5)

window.mainloop()