from tkinter import *

root = Tk()
root.geometry("200x300")
root.title("Calculator")
root.configure(bg = "gray78")

expression = StringVar()
is_result = False

def button_press(c):
    global is_result, expression
    if is_result:
        expression.set("")
        is_result = False
    s = expression.get()
    expression.set(s + str(c))


def button_delete():
    global is_result, expression
    s = expression.get()
    expression.set(s[:-1])


def button_clear():
    global is_result, expression
    expression.set("")


def calc_expr():
    global is_result, expression
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("ERROR")
    is_result = True

main_container = Frame(root, bg = "gray78")

text_field = Entry(main_container, width = 20, font=40, bg = "white", textvariable=expression, state=DISABLED)

input_container = Frame(main_container, bg = "gray78", width = 20)
add_button = Button(input_container, width = 5, height=3, command=lambda: button_press('+'), text = "+")
minus_button = Button(input_container, width = 5, height=3, command=lambda: button_press('-'), text = "-")
mult_button = Button(input_container, width = 5, height=3, command=lambda: button_press('*'), text = "*")
divide_button = Button(input_container, width = 5, height=3,command=lambda: button_press('/'), text = "/")

add_button.grid(row=0, column=0, pady=(5,0), padx=(0,5))
minus_button.grid(row=1, column=0, padx=(0,5))
mult_button.grid(row=2, column=0, padx=(0,5))
divide_button.grid(row=3, column=0, padx=(0,5), pady=(0,5))

one_button = Button(input_container, width = 5,height=3, command=lambda: button_press('1'), text = "1")
two_button = Button(input_container, width = 5, height=3, command=lambda: button_press('2'), text = "2")
three_button = Button(input_container, width = 5, height=3, command=lambda: button_press('3'), text = "3")
four_button = Button(input_container, width = 5, height=3, command=lambda: button_press('4'), text = "4")
five_button = Button(input_container, width = 5, height=3,command=lambda: button_press('5'), text = "5")
six_button = Button(input_container, width = 5, height=3, command=lambda: button_press('6'), text = "6")
seven_button = Button(input_container, width = 5, height=3, command=lambda: button_press('7'), text = "7")
eight_button = Button(input_container, width = 5, height=3, command=lambda: button_press('8'), text = "8")
nine_button = Button(input_container, width = 5, height=3, command=lambda: button_press('9'), text = "9")
zero_button = Button(input_container, width = 5, height=3, command=lambda: button_press('0'), text = "0")

one_button.grid(row=0, column=1, pady= (5,0))
two_button.grid(row=0, column=2, pady= (5,0))
three_button.grid(row=0, column=3, pady= (5,0))
four_button.grid(row=1, column=1)
five_button.grid(row=1, column=2)
six_button.grid(row=1, column=3)
seven_button.grid(row=2, column=1)
eight_button.grid(row=2, column=2)
nine_button.grid(row=2, column=3)
zero_button.grid(row=3, column=3)

left_button = Button(input_container, width = 5,height=3, command=lambda: button_press('('), text = "(")
right_button = Button(input_container, width = 5,height=3, command=lambda: button_press(')'), text = ")")

left_button.grid(row=3, column=1)
right_button.grid(row=3, column=2)

assist_container = Frame(main_container, bg = "gray78", width = 50)

back_button = Button(assist_container, width = 6, height=2, command=button_delete, text = "<-")
back_button.grid(row=0, column=0, padx=(0,5))

clear_button = Button(assist_container, width = 6, height=2, command=button_clear, text = "CLEAR")
clear_button.grid(row=0, column=1, padx=(5,5))

calc_button = Button(assist_container, width = 6, height=2, command=calc_expr, text = "=")
calc_button.grid(row=0, column=2, padx=(5, 0))


def pack_calculator():
    main_container.pack()
    text_field.pack()
    input_container.pack()
    assist_container.pack()


pack_calculator()

root.mainloop()