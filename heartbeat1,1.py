#!/usr/bin/env python3

import psutil
import math
import os
import turtle
import time
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkdial import Dial

pattern=[0,0,0,40,-80,120,-40,0,0,0]
x = -300
def loop():
    global x
    CPU = psutil.cpu_percent()
    RAM = 100 - psutil.virtual_memory().percent
    for y in pattern:
        t.goto(x,y)
        t.pendown()
        x += Constant - (CPU / 2)
        if x > 300:
            t.clear()
            t.penup()
            x = -300
    CPUTEXT = tk.Label(root, text=f"{CPU:.1f}", fg="green", bg="black", font=("Arial", 25, "bold"))
    CPUTEXT.place(x=715, y=30)
    RAMTEXT = tk.Label(root, text=f"{RAM:.1f}", fg="blue2", bg="black", font=("Arial", 25, "bold"))
    RAMTEXT.place(x=715, y=75)
    root.after(40, loop)


root = tk.Tk()
root.geometry("800x400")
root.title("Heartbeat 1.1.0")
root.configure(bg="grey10")
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack(pady=10)

screen = turtle.TurtleScreen(canvas)

screen.bgcolor("darkgreen")
Constant = 51
t = turtle.RawTurtle(screen)
t.color("green")
t.width(3)
t.speed(0)
t.penup()
t.goto(0, 125)
t.hideturtle()
loop()


root.mainloop()