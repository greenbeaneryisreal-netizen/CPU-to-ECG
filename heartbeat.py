#!/usr/bin/env python3

import psutil
import math
import os
import turtle
import time
import threading

#Sreen

screen = turtle.Screen()
screen.bgcolor("darkgreen")
screen.setup(width = 700, height=300)

#Turtle
Constant = 51
t = turtle.Turtle()
t.hideturtle()
t.color("green")
t.width(3)
t.speed(0)
t.penup()
t2 = turtle.Turtle()
t2.hideturtle()
t2.color("green")
t2.penup()
t2.goto(0, 125)

#Ecg Pattern Y values
pattern=[0,0,0,40,-80,120,-40,0,0,0]
x = -350
while True:
     CPU = psutil.cpu_percent()
     for y in pattern:
        t.goto(x,y)
        t.pendown()
        x += Constant - CPU / 2
        time.sleep(0.03)
        
        # Reset for continous loop
        if x > 350:
            t.clear()
            t.penup()
            x = -350
            t2.clear()
            t2.pendown()
            t2.write(f"{CPU}%", move=False, font=("arial", 12, "normal"))
            t2.penup()