# NAME = C.DILAKSHI KAUMADI ABEYSINGHE
# AR   = 96301
# AF   = 18 / 14335
# First Year First Semester Project


import tkinter as tk

import SystemDB as backEnd

from tkinter import *

import tkinter.messagebox as MessageBox

import mysql.connector as mysql
import self as self

from PIL import ImageTk, Image

# create instance

from tkinter.ttk import Button

# import action as action


my_Window = Tk()

# self.geometry('500x500')


# Window 1
from PIL import ImageTk, Image


class FirstPage(tk.Frame):
    # global a_label, my_image, my_button
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)


        # Add a title
        # self.title("System GUI")

        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Algerian 30 bold")

        # self.a_label = tk.Label(self, text="EXAM RESULT SYSTEM", font=("Arial", 30))
        self.a_label.place(x=250, y=150)

        # Add image

        # self.my_img = tk.PhotoImage(Image.open("pic.png"))
        # self.Label=(tk.my_window, Image = my_img).grid(row = 4, column = 5)
        #
        my_image = ImageTk.PhotoImage(Image.open("pic.png"))
        my_label = tk.Label(image=my_image)
        my_label.place(x=350, y=600)

        # Add Button
        self.my_button = tk.Button(self, text="Lets Go..!", background="brown", command=lambda: controller.show_frame(SecondPage))
        self.my_button.place(x=400, y=500)

        # Start GUI
        # self.mainloop()


# Window 2

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="WELCOME TO THE ERS..!", fg="maroon", font="Arial 16 bold")
        self.a_label2.place(x=329, y=200)

        self.a_label3 = tk.Label(self, background="white", text="EMAIL ADDRESS", fg="black", font="Arial 12 bold")
        self.a_label3.place(x=300, y=350)

        self.a_label4 = tk.Label(self, background="white", text="PASSWORD", fg="black", font="Arial 12 bold")
        self.a_label4.place(x=300, y=450)

        # Add Text Box
        self.e = tk.Entry(self, width=20)
        self.e.place(x=500, y=350)
        # e.insert(0, "Enter Your Email")

        # Add Entry Box
        self.e = tk.Entry(self, width=20)
        self.e.place(x=500, y=450)
        # self.e.insert(0, "Enter Your Password")

        # Add Button
        self.my_button = tk.Button(self, text="Log In", background="brown", command=lambda: controller.show_frame(ForthPage))
        self.my_button.place(x=400, y=550)

        self.my_button = tk.Button(self, text="Sign Up", background="brown", command=lambda: controller.show_frame(ThirdPage))
        self.my_button.place(x=395, y=600)

        # # Start GUI
        # self.mainloop()


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 =  tk.Label(self, background="white", text="Sign Up For Your Account", fg="maroon", font="Arial 16 bold")
        self.a_label2.place(x=329, y=200)

        self.a_label3 = tk.Label(self, background="yellow", text="EMAIL ADDRESS", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=300, y=300)

        self.a_label4 = tk.Label(self, background="yellow", text="USER NAME", fg="black", font="Arial 10 bold")
        self.a_label4.place(x=300, y=400)

        self.a_label3 = tk.Label(self, background="yellow", text="PASSWORD", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=300, y=500)

        self.a_label4 = tk.Label(self, background="yellow", text="CONFIRM PASSWORD", fg="black", font="Arial 10 bold")
        self.a_label4.place(x=300, y=600)

        # Add Entry Box
        self.e = tk.Entry(self, width=20)
        self.e.place(x=500, y=300)
        self.e.insert(0, "Enter Your Email")

        self.e = tk.Entry(self, width=20)
        self.e.place(x=500, y=400)
        self.e.insert(0, "Enter Your Password")

        self.e = tk.Entry(self, width=20)
        self.e.place(x=500, y=500)
        self.e.insert(0, "Enter Your Password")

        self.e = tk.Entry(self, width=20)
        self.e.place(x=500, y=600)
        self.e.insert(0, "Enter Your Password")

        self.my_button = tk.Button(self, text="Sign Up", background="brown", command=lambda: controller.show_frame(ForthPage))
        self.my_button.place(x=700, y=625)

        # Start GUI
        # self.mainloop()


# Window 4

class ForthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label1 = tk.Label(self, background="yellow", text="RESULT", fg="black", font="Arial 10 bold")
        self.a_label1.place(x=300, y=400)

        option = [
            "Student Individual Result",
            "Overall Result"
        ]

        self.clicked = tk.StringVar()
        self.clicked.set(option[0])

        self.drop = tk.OptionMenu(self, self.clicked, *option, )
        self.drop.place(x=400, y=400)

        # selectedpage = FifthPage

        def selectPage(val):

            if (val == "Student Individual Result"):
                selectedpage = FifthPage
            else:
                selectedpage = TwelvethPage

            return selectedpage

        page =self.clicked.get()

        z = selectPage(page)

        self.my_button = Button(self, text="View", command=lambda:  controller.show_frame(selectPage(self.clicked.get())))
        self.my_button.place(x=600, y=400)

        self.my_button = Button(self, text="Log Out",  command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # # Start GUI

        # self.mainloop()


# Window 5
# var = 0
# get_ar = 0
get_ar = tk.IntVar(value=0.0)

class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # global get_ar
        # global var

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="STUDENT INDIVIDUAL RESULT", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.a_label3 = tk.Label(self, background="yellow", text="STUDENT AR NUMBER", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=300, y=400)

        # global get_ar
        # get_ar = tk.IntVar()

        self.e = tk.Entry(self, width=20, textvariable=parent.get_ar.get())
        self.e.place(x=500, y=400)
        # # e.insert(0, "")


        self.my_button = tk.Button(self, text="View", command=lambda: passValue(get_ar.get(),SixthPage))
        self.my_button.place(x=450, y=500)

        self.my_button = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        def passValue(val,page):
            parent.get_ar.set(val)
            controller.show_frame(page)

        # Start GUI
        # self.mainloop()


# Window 6

class SixthPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="STUDENT INDIVIDUAL RESULT", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=335, y=200)

        # system should out the student AR number and student email address
        # my sql code

        self.a_label1 = tk.Label(self, background="white", text="SEMESTER RESULT", fg="black", font="Arial 10 bold")
        self.a_label1.place(x=290, y=300)

        option = [
            "1ST YEAR 1ST SEMESTER",
            "1ST YEAR 2ND SEMESTER",
            "2ND YEAR 1ST SEMESTER",
            "2ND YEAR 2ND SEMESTER",
        ]

        clicked = tk.StringVar()
        clicked.set(option[0])

        self.drop = tk.OptionMenu(self, clicked, *option)
        self.drop.place(x=450, y=300)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(SeventhPage))
        self.my_button.place(x=650, y=300)

        self.a_label2 = tk.Label(self, background="white", text="FINAL RESULT", fg="black", font="Arial 10 bold")
        self.a_label2.place(x=290, y=450)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(EleventhPage))
        self.my_button.place(x=650, y=450)

        self.my_button = tk.Button(self, text="CLOSE", command=lambda: controller.show_frame(SixthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 7

class SeventhPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="1ST YEAR 1ST SEMESTER", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.a_lbl1 = tk.Label(self, background="white", text="Sub 1 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl1.place(x=350, y=300)

        self.a_lbl2 = tk.Label(self, background="white", text="Sub 2 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl2.place(x=350, y=350)

        self.a_lbl3 = tk.Label(self, background="white", text="Sub 3 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl3.place(x=350, y=400)

        a_lbl4 = tk.Label(self, background="white", text="Sub 4 Grade", fg="black", font="Arial 8 bold")
        a_lbl4.place(x=350, y=450)

        a_lab1 = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 10 bold")
        a_lab1.place(x=250, y=550)

        a_lab1a = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 10 bold")
        a_lab1a.place(x=250, y=550)

        a_lab2 = tk.Label(self, background="white", text="Credits", fg="black", font="Arial 10 bold")
        a_lab2.place(x=450, y=550)

        a_lab3 = tk.Label(self, background="white", text="Class", fg="black", font="Arial 10 bold")
        a_lab3.place(x=650, y=550)

        self.my_button = tk.Button(self, text="CLOSE", command=lambda: controller.show_frame(SixthPage))
        self.my_button.place(x=750, y=600)

        self.my_button = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # System should output the Grade and etc.
        # mysql code

        # Start GUI

        # self.mainloop()


# Window 8

class EightPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="1ST YEAR 2ND SEMESTER", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.a_lbl1 = tk.Label(self, background="white", text="Sub 1 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl1.place(x=350, y=300)

        self.a_lbl2 = tk.Label(self, background="white", text="Sub 2 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl2.place(x=350, y=350)

        self.a_lbl3 = tk.Label(self, background="white", text="Sub 3 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl3.place(x=350, y=400)

        a_lbl4 = tk.Label(self, background="white", text="Sub 4 Grade", fg="black", font="Arial 8 bold")
        a_lbl4.place(x=350, y=450)

        a_lab1 = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 10 bold")
        a_lab1.place(x=250, y=550)

        a_lab2 = tk.Label(self, background="white", text="Credits", fg="black", font="Arial 10 bold")
        a_lab2.place(x=450, y=550)

        a_lab3 = tk.Label(self, background="white", text="Class", fg="black", font="Arial 10 bold")
        a_lab3.place(x=650, y=550)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(SixthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # System should output the Grade and etc.
        # mysql code

        # Start GUI

        # self.mainloop()


# Window 9

class NinePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="2ND YEAR 1ST SEMESTER", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.a_lbl1 = tk.Label(self, background="white", text="Sub 1 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl1.place(x=350, y=300)

        self.a_lbl2 = tk.Label(self, background="white", text="Sub 2 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl2.place(x=350, y=350)

        self.a_lbl3 = tk.Label(self, background="white", text="Sub 3 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl3.place(x=350, y=400)

        a_lbl4 = tk.Label(self, background="white", text="Sub 4 Grade", fg="black", font="Arial 8 bold")
        a_lbl4.place(x=350, y=450)

        a_lab1 = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 10 bold")
        a_lab1.place(x=250, y=550)

        a_lab2 = tk.Label(self, background="white", text="Credits", fg="black", font="Arial 10 bold")
        a_lab2.place(x=450, y=550)

        a_lab3 = tk.Label(self, background="white", text="Class", fg="black", font="Arial 10 bold")
        a_lab3.place(x=650, y=550)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(SixthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # System should output the Grade and etc.
        # mysql code

        # Start GUI

        # self.mainloop()


# Window 10

class TenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="2ND YEAR 2ND SEMESTER", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.a_lbl1 = tk.Label(self, background="white", text="Sub 1 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl1.place(x=350, y=300)

        self.a_lbl2 = tk.Label(self, background="white", text="Sub 2 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl2.place(x=350, y=350)

        self.a_lbl3 = tk.Label(self, background="white", text="Sub 3 Grade", fg="black", font="Arial 8 bold")
        self.a_lbl3.place(x=350, y=400)

        a_lbl4 = tk.Label(self, background="white", text="Sub 4 Grade", fg="black", font="Arial 8 bold")
        a_lbl4.place(x=350, y=450)

        a_lab1 = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 10 bold")
        a_lab1.place(x=250, y=550)

        a_lab2 = tk.Label(self, background="white", text="Credits", fg="black", font="Arial 10 bold")
        a_lab2.place(x=450, y=550)

        a_lab3 = tk.Label(self, background="white", text="Class", fg="black", font="Arial 10 bold")
        a_lab3.place(x=650, y=550)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(SixthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # System should output the Grade and etc.
        # mysql code

        # Start GUI

        # self.mainloop()


# Window 11

class EleventhPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="FINAL RESULT", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        self.a_lbl1 = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 12 bold")
        self.a_lbl1.place(x=200, y=400)

        self.ar_var = tk.IntVar(value=0.0)
        self.ar_var.set(lambda :parent.get_ar.get())

        self.a_lbl = tk.Label(self, textvariable=self.ar_var)
        self.a_lbl.place(x=200, y=500)
        print("VAR ",lambda :parent.get_ar.get())
        # val = backEnd.calcFinalgpa()
        # print("VAL ",val)


        # self.update()

        self.a_lbl2 = tk.Label(self, background="white", text="TOTAL CREDITS", fg="black", font="Arial 12 bold")
        self.a_lbl2.place(x=400, y=400)

        self.a_lbl3 = tk.Label(self, background="white", text="CLASS", fg="black", font="Arial 12 bold")
        self.a_lbl3.place(x=600, y=400)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(SixthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


        # self.mainloop()


# Window 12

class TwelvethPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="OVERALL RESULT", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        self.a_label1 = tk.Label(self, background="white", text="GPA DISTRIBUTION", fg="black", font="Arial 10 bold")
        self.a_label1.place(x=290, y=400)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=600, y=400)

        self.a_label2 = tk.Label(self, background="white", text="CLASS DISTRIBUTION", fg="black", font="Arial 10 bold")
        self.a_label2.place(x=290, y=500)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(FourteenthPage))
        self.my_button.place(x=600, y=500)

        self.a_label3 = tk.Label(self, background="white", text="SUBJECT ANALYSIS", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=290, y=600)

        option = [
            "1001",
            "1002",
            "1003",
            "1004",
        ]

        clicked = tk.StringVar()
        clicked.set(option[0])

        self.drop = tk.OptionMenu(self, clicked, *option)
        self.drop.place(x=500, y=600)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(FifteenthPage))
        self.my_button.place(x=600, y=600)

        self.a_label4 = tk.Label(self, background="white", text="OVERALL RANKING SUMMARY", fg="black", font="Arial 10 bold")
        self.a_label4.place(x=290, y=700)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(FifteenthPage))
        self.my_button.place(x=600, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 13

class ThirteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="GPA DISTRIBUTION", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        # Add GPA Distribution in line chart

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 14

class FourteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="CLASS DISTRIBUTION", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        # Add Class Distribution in bar chart

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 15

class FifteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 1", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        # Add Subject Analysis in pie chart

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(SixteenthPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 16

class SixteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #
        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 2", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        # Add Class Distribution in pie chart

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 17

class SeventeenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 3", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        # Add Class Distribution pie chart

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 18

class EighteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 4", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        # Add Class Distribution pie chart

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()


# Window 19

class NineteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # # Add a title
        # self.title("System GUI")
        #
        # self.configure(background="white")
        # self.minsize(width=300, height=300)
        # self.maxsize(width=900, height=900)

        # Add Label
        self.a_label1 = tk.Label(self, background="white", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="OVERALL RANKING SUMMARY", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=335, y=200)

        # Add Table to display overall ranking summary

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        # Start GUI

        # self.mainloop()



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        # self.get_ar = tk.IntVar(tk.Tk())
        tk.Tk.__init__(self, *args, **kwargs)
        # self.get_ar = tk.IntVar()
        # creating a window
        # my_window = tk.Tk()
        my_window = tk.Frame(self)
        my_window.pack()
        # get_ar = tk.IntVar(tk.Tk())
        my_window.grid_rowconfigure(0, minsize=700)
        my_window.grid_columnconfigure(0, minsize=900)
        my_window.configure(background="white")
        # my_window.minsize(width=300, height=300)
        # my_window.maxsize(width=900, height=900)

        self.frames = {}
        # for F in (FirstPage, SecondPage):
        for F in (FirstPage, SecondPage, ThirdPage, ForthPage, FifthPage, SixthPage, SeventhPage, EightPage, NinePage,TenthPage, EleventhPage, TwelvethPage, ThirteenthPage, FourteenthPage, FifteenthPage, SixteenthPage, SeventeenthPage, EighteenthPage, NineteenthPage):
            frame = F(my_window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()

