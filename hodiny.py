# -*- coding: UTF-8 -*-
# Program:		hodiny.py
# Zadání:		
# URL zadání:		
# Datum:		2024-04-11
# Verze:		1.0
# Autor:		Richard Rutterle
# Třída:		3.PT

from tkinter import Tk, Canvas
from datetime import datetime
import math


class Hodiny:
    def __init__(self, width = 700, height = 700):
        self.h = iter(['12','1','2','3','4','5','6','7','8','9','10','11'])
        self.analog = 0
        
        radius  = 250
        root = Tk()
        root.resizable(False,False)
        
        self.width, self.height = width, height
        
        self.x1, self.y1 = self.width // 4, self.height // 4
        self.x2, self.y2 = self.width // 3, self.height // 3
        self.x3, self.y3 = self.width // 2, self.height // 2
        self.x4, self.y4 = self.width, self.height
        
        self.seconds = radius - 20
        self.minutes = self.seconds - 60
        self.hours = self.minutes - 60
        
        self.seconds_needles = radius - 110
        self.minutes_needles = self.seconds_needles
        self.hours_needles = self.minutes_needles

        

        self.canvas = Canvas(root, width = self.width, height = self.height)
        self.canvas.pack()
        
        self.canvas.create_text(self.x3,50, text = "hodiny", font = "Consolas 20")
        self.date = self.canvas.create_text(self.x3, self.height-50, text = "Datum: ", font = "Consolas 20")

        self.canvas.create_oval(self.x3 - radius, self.y3 - radius, self.x3 + radius, self.y3 + radius, width=2)
        self.canvas.create_oval(self.x3-5, self.y3-5, self.x3+5, self.y3+5, fill="#000000")
        
        if self.analog:
            self.add_numbers(radius_cisla = radius-20, pause = 1000)
            
            self.s_needle = self.canvas.create_text(self.x3 + self.seconds - 30 * math.sin(0), self.x3 - self.seconds - 30 * math.cos(0), text = "\n|"*6, angle = math.radians(self.seconds), font = "Consolas 20", fill = "red", anchor="center")
            self.m_needle = self.canvas.create_text(self.x3 + self.minutes - 30 * math.sin(0), self.x3 - self.minutes - 30 * math.cos(0), text = "\n"*2 + "\n|"*4, angle = math.radians(self.minutes), font = "Consolas 20", fill = "green", anchor="center")
            self.h_needle = self.canvas.create_text(self.x3 + self.hours - 30 * math.sin(0), self.x3 - self.hours - 30 * math.cos(0), text = "\n"*4 + "\n|"*2, angle = math.radians(self.hours), font = "Consolas 20", fill = "blue", anchor="center")
            

        else:
            self.second = self.canvas.create_text(self.x3 + self.seconds * math.sin(0), self.x3 - self.seconds * math.cos(0), text = "Now:", angle = math.radians(self.seconds), font = "Consolas 20", fill = "red", anchor="center")
            self.minute = self.canvas.create_text(self.x3 + self.minutes * math.sin(0), self.x3 - self.minutes * math.cos(0), text = "Now:", angle = math.radians(self.minutes), font = "Consolas 20", fill = "green", anchor="center")
            self.hour = self.canvas.create_text(self.x3 + self.hours * math.sin(0), self.x3 - self.hours * math.cos(0), text = "Now:", angle = math.radians(self.hours), font = "Consolas 20", fill = "blue", anchor="center")   

            self.s_needle = self.canvas.create_text(self.x3 + self.seconds - 30 * math.sin(0), self.x3 - self.seconds - 30 * math.cos(0), text = "\n|"*6, angle = math.radians(self.seconds), font = "Consolas 20", fill = "red", anchor="center")
            self.m_needle = self.canvas.create_text(self.x3 + self.minutes - 30 * math.sin(0), self.x3 - self.minutes - 30 * math.cos(0), text = "\n"*2 + "\n|"*4, angle = math.radians(self.minutes), font = "Consolas 20", fill = "green", anchor="center")
            self.h_needle = self.canvas.create_text(self.x3 + self.hours - 30 * math.sin(0), self.x3 - self.hours - 30 * math.cos(0), text = "\n"*4 + "\n|"*2, angle = math.radians(self.hours), font = "Consolas 20 bold", fill = "blue", anchor="center")
            

        self.reload_canvas()
        root.mainloop()
        
    def reload_canvas(self):
        date_time = datetime.now()
        self.canvas.itemconfigure(self.date, text = f"Datum: {date_time.day}.{date_time.month}.{date_time.year}")
        self.canvas.after(1, self.reload_canvas)
        
        rad_sec = math.radians(date_time.second)*6
        rad_min = math.radians(date_time.minute)*6
        rad_hour = math.radians(date_time.hour)*30

        
        if self.analog:
            self.canvas.itemconfigure(self.s_needle, angle = -math.degrees(rad_sec))

            self.canvas.coords(self.s_needle,  (self.x3 + self.seconds_needles * math.sin(rad_sec), self.x3 - self.seconds_needles * math.cos(rad_sec)))

            self.canvas.itemconfigure(self.m_needle,  angle = -math.degrees(rad_min))

            self.canvas.coords(self.m_needle, (self.x3 + self.minutes_needles * math.sin(rad_min), self.x3 - self.minutes_needles * math.cos(rad_min)))

            self.canvas.itemconfigure(self.h_needle, angle = -math.degrees(rad_hour))

            self.canvas.coords(self.h_needle,  (self.x3 + self.hours_needles * math.sin(rad_hour), self.x3 - self.hours_needles * math.cos(rad_hour)))

        
        else:
            
            self.canvas.itemconfigure(self.second, text = f"{date_time.second}", angle = -math.degrees(rad_sec))
            self.canvas.coords(self.second,  (self.x3 + self.seconds * math.sin(rad_sec), self.x3 - self.seconds * math.cos(rad_sec)))
            
            self.canvas.itemconfigure(self.s_needle, angle = -math.degrees(rad_sec))
            self.canvas.coords(self.s_needle,  (self.x3 + self.seconds_needles * math.sin(rad_sec), self.x3 - self.seconds_needles * math.cos(rad_sec)))

            self.canvas.itemconfigure(self.minute, text = f"{date_time.minute}", angle = -math.degrees(rad_min))
            self.canvas.coords(self.minute,  (self.x3 + self.minutes * math.sin(rad_min), self.x3 - self.minutes * math.cos(rad_min)))

            self.canvas.itemconfigure(self.m_needle,  angle = -math.degrees(rad_min))
            self.canvas.coords(self.m_needle, (self.x3 + self.minutes_needles * math.sin(rad_min), self.x3 - self.minutes_needles * math.cos(rad_min)))

            self.canvas.itemconfigure(self.hour, text = f"{date_time.hour}", angle = -math.degrees(rad_hour))
            self.canvas.coords(self.hour,  (self.x3 + self.hours * math.sin(rad_hour), self.x3 - self.hours * math.cos(rad_hour)))

            self.canvas.itemconfigure(self.h_needle, angle = -math.degrees(rad_hour))
            self.canvas.coords(self.h_needle,  (self.x3 + self.hours_needles * math.sin(rad_hour), self.x3 - self.hours_needles * math.cos(rad_hour)))



    def add_numbers(self, pause = 10, degree=0, radius_cisla = 180, loop=0, end = 60):
            in_radian = math.radians(degree) # converting to radian
            # print(loop)
            if loop % 5 == 0:
                t1 = self.x3 + radius_cisla * math.sin(in_radian) # coordinate to add text ( hour numbers )
                t2 = self.x3 - radius_cisla * math.cos(in_radian) # coordinate to add text ( hour numbers )
                self.canvas.create_text(t1, t2, text = next(self.h), font="Consolas 20") # number added
            
            if loop < end-1:    
                self.canvas.after(pause // 2, lambda a = None: self.add_numbers(degree = degree + 6,loop =  loop + 1, radius_cisla = radius_cisla))
            
            else: return
        
        
        
if __name__ == "__main__":
    d = Hodiny()
