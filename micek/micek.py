# -*- coding: UTF-8 -*-
# Program:		micek.py
# Zadání:		
# URL zadání:	
# Datum:		2024-04-25
# Verze:		1.1
# Autor:		Richard Rutterle
# Třída:		3.PT

import asyncio
from tkinter import Tk, Canvas
from random import randint

class Micek:
    pocet = 0
    def __init__(self, x, y, d, pr:float = 1, dx = 5):
        self.x, self.y, self.d, self.pr, self.dx, self.dy = x, y, d, pr, dx, 0
        self.mic = pl.create_oval(x, y, x+d ,y+d, fill = self.barva())
        self.pohyb()
    
    def remove(self):
        if Micek.pocet > 1:
            pl.delete(self.mic)
            Micek.pocet -= 1

    async def spawn(self):
        asyncio.sleep(1)
        Micek(randint(10,500), randint(10,100), randint(10, 15),pr = randint(2,10)/10, dx = randint(-15, 15)/10)
        Micek.pocet += 1
        print(Micek.pocet)
    
    def pohyb(self):
        self.x += self.dx
        o.after(1000*10, self.remove)
        
        if self.x <= 0 or (self.x + self.d) >= 600:
            self.dx *= -self.pr
            self.remove()
            return
            
        self.dy += 1
        self.y += self.dy

        if self.y + self.d >= 600:
            self.y = 600 - self.d
            self.dy *= -self.pr
            pl.itemconfig(self.mic)
            
            if Micek.pocet < 100: 
                asyncio.run(self.spawn())
                
        pl.coords(self.mic, self.x, self.y, self.x + self.d,  self.y + self.d)
        o.after(50, self.pohyb)
        
    def barva(self):
        HEX = "0123456789ABCDEF"
        
        barva = f"#{HEX[randint(0,15)]}{HEX[randint(0,15)]}{HEX[randint(0,15)]}"
        return barva
    
o = Tk()
pl = Canvas(o, width = 600, height = 600)
pl.pack()
asyncio.run(Micek.spawn("m1"))
o.mainloop()
