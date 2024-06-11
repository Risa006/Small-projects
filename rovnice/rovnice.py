# -*- coding: UTF-8 -*-
# Program:		rovnice.py
# Zadání:		
# URL zadání:		
# Datum:		2024-06-06
# Verze:		1.6
# Autor:		Richard Rutterle
class Rovnice:
    def __init__(self, **kwargs:dict[str,int|float]) -> None:
        try:
            self.a = kwargs["a"]
        except(KeyError):
            self.a = 0
        try:
            self.b = kwargs["b"]
        except(KeyError):
            self.b = 0
        try:
            self.c = kwargs["c"]
        except(KeyError):
            self.c = 0
        if self.a == 0 and self.b == 0 and self.a == 0:
            print("Zadej hodnoty \"a\", \"b\", \"c\"")
            return None
            
        elif self.a == 0:
            self.__linearni()
        else:
            if self.b != 0 and self.c != 0:
                self.__kvadraticka()
            else:
                print("Zadej hodnoty \"b\", \"c\"")
  
    def __kvadraticka(self):
        d = self.b ** 2 - 4 * self.a * self.c
        x1 = ((-self.b) + (self.odmocnina(d, 2)))/(2 * self.a)
        x2 = ((-self.b) - (self.odmocnina(d, 2)))/(2 * self.a)
        print(f"Kvadratická funkce s kořeny {x1 = } a {x2 = }")
        
    def __linearni(self):
        x = (-self.c)/self.b
        print(f"Funkce je lineární s kořenem {x = }")

    def mocnina(self, koren:int|float, exponent:int) -> int|float|complex:
        return koren**int(exponent)

    def odmocnina(self, koren:int|float, exponent:int) -> int|float|complex:
        return koren**(1/int(exponent))
r = Rovnice(
    a=1,
    b=5,
    c=11
)
