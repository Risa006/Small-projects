# -*- coding: UTF-8 -*-
# Program:		Space-Invaders.py
# Zadání:		
# URL zadání:		
# Datum:		2024-06-07
# Verze:		1.3
# Autor:		Richard Rutterle
import turtle

okno = turtle.Screen()                              #Vytvoří OKNO
okno.tracer(0) 
okno.setup(0.5, 0.75)                               #Určí velikost okna ---> float: procento screenu, int: skutečná velikost
okno.bgcolor(0.2, 0.2, 0.2)                         #Nastavení barvy pozadí v RGB ---> pouze float: [0, 1](min, max)
okno.title("Space Invaders"+" " u"\U0001F60A")      #Nastavení titulku okna i s UTF-8

#VARIABLES
LEFT = okno.window_width()/2
RIGHT = -okno.window_width()/2
TOP = okno.window_height()/2
BOTTOM = -okno.window_height()/2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * okno.window_width()

kanon = turtle.Turtle()                             #Vetvoření objektu pro vykreslení
kanon.penup()                                       #Přerušení vekreslování
kanon.color(1, 1, 1)                                #Nastavení barvy objektu
kanon.shape("square")                               #Nastavení tvaru podle pojemnovaného tvaru
kanon.setposition(0, FLOOR_LEVEL)                   #nastavení pozice objektu
kanon.turtlesize(1, 4)
kanon.stamp()
kanon.sety(FLOOR_LEVEL + 10)
kanon.turtlesize(1, 1.5)
kanon.stamp()
kanon.sety(FLOOR_LEVEL + 20)
kanon.turtlesize(0.8, 0.3)
kanon.stamp()
kanon.sety(FLOOR_LEVEL)

KROK = 10

def draw():
    kanon.clear()
    kanon.turtlesize(1, 4)
    kanon.stamp()
    kanon.sety(FLOOR_LEVEL + 10)
    kanon.turtlesize(1, 1.5)
    kanon.stamp()
    kanon.sety(FLOOR_LEVEL + 20)
    kanon.turtlesize(0.8, 0.3)
    kanon.stamp()
    kanon.sety(FLOOR_LEVEL)
    okno.update()

def move_left():
    x = kanon.xcor() - KROK
    if x >= LEFT + GUTTER:
        kanon.setx(x = x)
        draw()

def move_right():
    x = kanon.xcor() + KROK
    if x <= RIGHT + GUTTER:
        kanon.setx(x = x)
        draw()


okno.onkeypress(move_left, "Left")
okno.onkeypress(move_right, "Right")
okno.onkeypress(turtle.bye, "q")
okno.listen()

draw()

turtle.done()                   #Poslední ---> Stratuje aplikaci a nechává zapnutý okno
