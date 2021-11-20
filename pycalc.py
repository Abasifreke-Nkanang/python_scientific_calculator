#Importing needed modules
from tkinter import*
import math
import tkinter.messagebox

root = Tk()

#sets the name on the top of the gui
root.title("Scientific Calculator")

#this sets the background colour to gray-white
root.configure(background = "white")


#sets the gui such that it cannot be resized
root.resizable(width = False, height = False)

#sets the geometry
root.geometry("480x568+350+90")

#this sets the container named calc where all the buttons are contained in
calc = Frame(root)

#this sets the grid display of the container(buttons)
calc.grid()

#creating a class, creating the different functions of the scientific calculator
class Calc():
    def __init__(self):
        self.total = 0
        self.current = " "
        self.input_value = True
        self.check_sum = False
        self.op = " "
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "div":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)


    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result :
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squareroot(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()

#creating a display in the gui of the calculator
txtDisplay = Entry(calc, 
                    font = ("Helvetica" , 20 , "bold"),
                    bg = "black",
                    fg = "white",
                    bd = 30,
                    width = 28,
                    justify = RIGHT )

txtDisplay.grid(
    row = 0,
    column = 0,
    columnspan = 4,
    pady = 1
)

txtDisplay.insert(0, "0")

#creating a number pad for the calculator

#First of all, storing all the numbers in a string variable
numberpad = "789456123"

#row count for placing the buttons in grid
index = 0

#creating an empty list to store each button and its specs
buttn = []
#button specifications
for a in range(2, 5):
    for b in range(3):
        buttn.append(Button(calc, 
                            width = 6,
                            height = 2,
                            bg = "white",
                            fg = "black",
                            font = ("helvetica", 20, "bold"),
                            bd = 4,
                            text = numberpad[index]    ))

        #set button in row and column, and separate them with a padding of 1 unit
        buttn[index].grid(row = a, column = b, pady = 1)

        #putting that number as a symbol on the button
        buttn[index]["command"] = lambda x = numberpad[index]: added_value.numberEnter(x)
        index += 1


#Placing all the buttons, operators in their respective positions in the grid
buttnClear = Button(calc, text = chr(67),
                            width = 6,
                            height = 2,
                            bg = "red",
                            font = ("Tahoma", 20, "bold"),
                            bd = 4,
                            command = added_value.clear_entry)
buttnClear.grid(row = 1, column = 0, pady = 1)

buttnAllClear = Button(calc, text = chr(67) + chr(69),
                            width = 6,
                            height = 2,
                            bg = "red",
                            font = ("Tahoma", 20, "bold"),
                            bd = 4,
                            command = added_value.all_clear_entry)
buttnAllClear.grid(row = 1, column = 1, pady = 1)
buttnsq = Button(calc, text = "\u221A",
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = added_value.squareroot)
buttnsq.grid(row = 1, column = 2, pady = 1)
buttnAdd = Button(calc, text = "+",
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = lambda: added_value.operation("add"))
buttnAdd.grid(row = 1, column = 3, pady = 1)
buttnSub = Button(calc, text = "-",
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = lambda: added_value.operation("sub"))
buttnSub.grid(row = 2, column = 3, pady = 1)
buttnMulti = Button(calc, text = "x",
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = lambda: added_value.operation("multi"))
buttnMulti.grid(row = 3, column = 3, pady = 1)
buttnDiv = Button(calc, text = "/",
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = lambda: added_value.operation("div"))
buttnDiv.grid(row = 4, column = 3, pady = 1)
buttnZero = Button(calc, text = "0",
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = lambda: added_value.numberEnter(0))
buttnZero.grid(row = 5, column = 0, pady = 1)
buttnDot = Button(calc, text = ".",
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = lambda: added_value.numberEnter("."))
buttnDot.grid(row = 5, column = 1, pady = 1)
buttnPM = Button(calc, text = chr(177),
                            width = 6,
                            height = 2,
                            bg = "powder blue",
                            font = ("Helvetica", 20, "bold"),
                            bd = 4,
                            command = added_value.mathPM)
buttnPM.grid(row = 5, column = 2, pady = 1)
buttnEquals = Button(calc, text = "=",
                            width = 6,
                            height = 2,
                            bg = "red",
                            font = ("Tahoma", 20, "bold"),
                            bd = 4,
                            command = added_value.sum_of_total)
buttnEquals.grid(row = 5, column = 3, pady = 1)

#ROW 1
buttnPi = Button(calc, text = "pi", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.pi)
buttnPi.grid(row = 1, column = 4, pady = 1)
buttnCos = Button(calc, text = "cos", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.cos)
buttnCos.grid(row = 1, column = 5, pady = 1)
buttnSin = Button(calc, text = "sin", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.sin)
buttnSin.grid(row = 1, column = 6, pady = 1)
buttnTan = Button(calc, text = "tan", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.tan)
buttnTan.grid(row = 1, column = 7, pady = 1)

#ROW 2
buttn2Pi = Button(calc, text = "2pi", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.tau)
buttn2Pi.grid(row = 2, column = 4, pady = 1)
buttnCosh = Button(calc, text = "cosh", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.cosh)
buttnCosh.grid(row = 2, column = 5, pady = 1)
buttnSinh = Button(calc, text = "sinh", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.sinh)
buttnSinh.grid(row = 2, column = 6, pady = 1)
buttnTanh = Button(calc, text = "tanh", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.tanh)
buttnTanh.grid(row = 2, column = 7, pady = 1)

#ROW 3
buttnLog = Button(calc, text = "log", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.log)
buttnLog.grid(row = 3, column = 4, pady = 1)
buttnExp = Button(calc, text = "exp", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.exp)
buttnExp.grid(row = 3, column = 5, pady = 1)
buttnMod = Button(calc, text = "Mod", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = lambda : added_value.operation("mod")
                                    )
buttnMod.grid(row = 3, column = 6, pady = 1)
buttnE = Button(calc, text = "e", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.e)
buttnE.grid(row = 3, column = 7, pady = 1)

#ROW 4
buttnLog10 = Button(calc, text = "log10", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.log10)
buttnLog10.grid(row = 4, column = 4, pady = 1)
buttnLog1p = Button(calc, text = "log1p", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.log1p)
buttnLog1p.grid(row = 4, column = 5, pady = 1)
buttnExpm1 = Button(calc, text = "expm1", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.expm1)
buttnExpm1.grid(row = 4, column = 6, pady = 1)
buttnLgamma = Button(calc, text = "lgamma", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.lgamma)
buttnLgamma.grid(row = 4, column = 7, pady = 1)

#ROW 5
buttnLog2 = Button(calc, text = "log2", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.log2)
buttnLog2.grid(row = 5, column = 4, pady = 1)
buttnDeg = Button(calc, text = "deg", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.degrees)
buttnDeg.grid(row = 5, column = 5, pady = 1)
buttnAcosh = Button(calc, text = "acosh", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.acosh)
buttnAcosh.grid(row = 5, column = 6, pady = 1)
buttnAsinh = Button(calc, text = "asinh", width = 6, height = 2,
                                    bg = "powder blue", fg = "black",
                                    font = ("Helvetica", 20, "bold"),
                                    bd = 4, command = added_value.asinh)
buttnAsinh.grid(row = 5, column = 7, pady = 1)

lblDisplay = Label(calc, text = "Scientific Calculator", 
                                    font = ("Tahoma", 30, "bold"),
                                    bg = "powder blue", fg = "black", justify = CENTER)
lblDisplay.grid(row = 0, column = 4, columnspan = 4)

#Creating the menubar of the calculator GUI
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?" )
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width = False, height = False)
    root.geometry("950x568+0+0")

def standard():
    root.resizable(width = False, height = False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

#menubar 1
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "standard", command = standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

#menubar 2
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
filemenu.add_command(label = "Cut")
filemenu.add_command(label = "Copy")
filemenu.add_separator()
filemenu.add_command(label = "Paste")

root.config(menu = menubar)

root.mainloop()
