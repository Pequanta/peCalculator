from tkinter import *
from util.operator import *
from util.tools import *
from PIL import ImageTk, Image
import math


class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.title("Qcalculator")
        self.geometry("400x600")
        self.configure(bg="silver")
        self.background = ImageTk.PhotoImage(Image.open("one.jpg"))
        
        
        self.di_frm = Frame(self)
        self.di_frm.configure(bd=5,relief="sunken")
        self.di_frm.place(relx= 0.04,rely=0.05, relwidth=0.92,relheight=0.08)
        self.n_entry = Entry(self.di_frm,font=("Arial",15,"bold"))
        self.n_entry.place(relwidth=1, relheight=1)
        

        self.n_keys_frm = Frame(self)
        self.n_keys_frm.configure(bg="silver")
        self.n_keys_frm.place(relx = 0.06,rely=0.15,relwidth=0.88,relheight=0.83)
 #       self.lbl = Label(self.n_keys_frm, image=self.background)
 #       self.lbl.place(relx = 0, rely = 0,relwidth = 1, relheight = 1)

        self.n_one = Button(self.n_keys_frm,text = "1",command= lambda : num(self,"1"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_one.place(relx=0,rely=0.7,relwidth=0.25,relheight=0.1)

        self.n_two = Button(self.n_keys_frm, text="2", command=lambda: num(self,"2"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_two.place(relx=0.25, rely=0.7, relwidth=0.25,relheight=0.1)

        self.n_three = Button(self.n_keys_frm, text="3", command=lambda: num(self,"3"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_three.place(relx=0.5, rely=0.7, relwidth=0.25,relheight=0.1)

        self.n_four = Button(self.n_keys_frm, text="4", command=lambda: num(self,"4"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_four.place(relx=0, rely=0.6, relwidth=0.25,relheight=0.1)

        self.n_five = Button(self.n_keys_frm, text="5", command=lambda: num(self,"5"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_five.place(relx=0.25, rely=0.6, relwidth=0.25,relheight=0.1)

        self.n_six = Button(self.n_keys_frm, text="6", command=lambda: num(self,"6"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_six.place(relx=0.5, rely=0.6, relwidth=0.25,relheight=0.1)

        self.n_seven = Button(self.n_keys_frm, text="7", command=lambda: num(self,"7"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_seven.place(relx=0, rely=0.5, relwidth=0.25,relheight=0.1)

        self.n_eight = Button(self.n_keys_frm, text="8", command=lambda: num(self,"8"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_eight.place(relx=0.25, rely=0.5, relwidth=0.25,relheight=0.1)

        self.n_nine = Button(self.n_keys_frm, text="9", command=lambda: num(self,"9"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_nine.place(relx=0.5, rely=0.5, relwidth=0.25,relheight=0.1)

        self.n_zero = Button(self.n_keys_frm, text="0", command=lambda: num(self,"0"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.n_zero.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.1)

        self.k_multi = Button(self.n_keys_frm, text = "*",command=lambda :handler(self,"mult"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_multi.place(relx= 0.75,rely=0.5,relwidth=0.25,relheight=0.1)

        self.k_div = Button(self.n_keys_frm, text="/", command=lambda: handler(self,"div"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_div.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.1)

        self.k_sum = Button(self.n_keys_frm, text="+", command=lambda: handler(self,"sum"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_sum.place(relx=0.75, rely=0.7, relwidth=0.25, relheight=0.1)

        self.k_minus= Button(self.n_keys_frm, text="-", command=lambda: handler(self,"diff"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_minus.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.1)

        self.k_minus = Button(self.n_keys_frm, text="π", command=lambda: num(self, "π"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_minus.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.1)

        self.k_sin = Button(self.n_keys_frm,text = "sin",command = lambda : handler(self,"sin"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_sin.place(relx=0, rely=0.1, relwidth=0.25,relheight=0.1)
        self.k_cos = Button(self.n_keys_frm, text="cos", command=lambda: handler(self,"cos"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_cos.place(relx=0.25, rely=0.1, relwidth=0.25, relheight=0.1)
        self.k_tan = Button(self.n_keys_frm, text="tan", command=lambda: handler(self,"tan"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_tan.place(relx=0.5, rely=0.1, relwidth=0.25, relheight=0.1)

        self.k_sqrt = Button(self.n_keys_frm, text="√", command=lambda: handler(self,"sqrt"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_sqrt.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.1)
        self.k_power = Button(self.n_keys_frm, text="X^y", command=lambda: handler(self,"^"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_power.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.1)
        self.k_log = Button(self.n_keys_frm, text="log10", command=lambda: handler(self,"log10"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_log.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.1)

        self.k_equal = Button(self.n_keys_frm,text="=",command = lambda : handler(self,"equal"),relief=RAISED,bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_equal.place(relx=0.5,rely=0.8,relheight=0.1,relwidth=0.25)

        self.k_clear = Button(self.n_keys_frm, text="clr", command=lambda: clear(self), relief=RAISED, bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_clear.place(relx=0.5, rely=0.4, relheight=0.1, relwidth=0.25)

        self.k_back = Button(self.n_keys_frm, text="⇐", command=lambda: back(self), relief=RAISED, bd=5,bg = "#e0ffff",activebackground="#f0e68c")
        self.k_back.place(relx=0.75, rely=0.4, relheight=0.1, relwidth=0.25)


        self.bind("<Return>",handler(self,"="))

if __name__=="__main__":
    calc = Calc()
    calc.mainloop()
