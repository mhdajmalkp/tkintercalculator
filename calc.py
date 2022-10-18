from tkinter import *

calc = Tk()

calc.title("Calculator")
calc.geometry('330x360')
calc.configure(bg="cornflowerblue")

#icon
img=PhotoImage(file='D:\\py tkinter\\calculator\\calculator.png')
calc.iconphoto(False,img)

# operation fuctions
def clearf():
    en.delete(0, "end")


def clear():
    en.delete(0, "end")


def delete():
    a = en.get()
    en.delete(len(a) - 1)


def result():
    re = en.get()
    re = eval(re)

    clearf()
    en.insert(0, re)


# entry  box
en = Entry(calc, font=("bold", 30), justify="right", borderwidth=5, relief="solid")
en.place(x=10, y=10, width=310, height=50)

# clear button
clear = Button(calc, text="C", font=("bold", 15), borderwidth=5, relief="raised", command=clear, bg="silver")
clear.place(x=10, y=80, width=220)

# delete button
de = Button(calc, text="del", font=("bold", 15), borderwidth=5, relief="raised", command=delete, bg="red")
de.place(x=240, y=80, width=80)

# number 1-3
n1 = Button(calc, text=1, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 1))
n1.place(x=10, y=130, width=70, height=50)

n2 = Button(calc, text=2, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 2))
n2.place(x=85, y=130, width=70, height=50)

n3 = Button(calc, text=3, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 3))
n3.place(x=160, y=130, width=70, height=50)

# no 4-6

n4 = Button(calc, text=4, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 4))
n4.place(x=10, y=185, width=70, height=50)

n5 = Button(calc, text=5, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 5))
n5.place(x=85, y=185, width=70, height=50)

n6 = Button(calc, text=6, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 6))
n6.place(x=160, y=185, width=70, height=50)

# no 7-0
n7 = Button(calc, text=7, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 7))
n7.place(x=10, y=240, width=70, height=50)

n8 = Button(calc, text=8, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 8))
n8.place(x=85, y=240, width=70, height=50)

n9 = Button(calc, text=9, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 9))
n9.place(x=160, y=240, width=70, height=50)

n0 = Button(calc, text=0, font=("bold", 15), borderwidth=5, relief="raised", command=lambda: en.insert("end", 0))
n0.place(x=10, y=295, width=70, height=50)

# operations
div = Button(calc, text="/", font=("bold", 15), borderwidth=2, relief="solid", bg="silver",
             command=lambda: en.insert("end", "/"))
div.place(x=240, y=130, width=80, height=50)

mul = Button(calc, text="X", font=("bold", 15), borderwidth=2, relief="solid", bg="silver",
             command=lambda: en.insert("end", "*"))
mul.place(x=240, y=185, width=80, height=50)

mins = Button(calc, text="-", font=("bold", 15), borderwidth=2, relief="solid", bg="silver",
              command=lambda: en.insert("end", "-"))
mins.place(x=240, y=240, width=80, height=50)

plus = Button(calc, text="+", font=("bold", 15), borderwidth=2, relief="solid", bg="silver",
              command=lambda: en.insert("end", "+"))
plus.place(x=240, y=295, width=80, height=50)

equal = Button(calc, text="=", font=("bold", 15), bg="silver", command=result, borderwidth=2, relief="solid")
equal.place(x=85, y=295, width=145, height=50)

calc.mainloop()
