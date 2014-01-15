import math
import matplotlib.pyplot as plt
import numpy as np

class Number(object):
    def __init__(self):
        print("New calculation")

    def truedip(self,num1,num2):
        # a = apparent bed thickness or structure contour value
        # b = horizontal distance
        a = math.radians(num1)
        b = math.radians(num2)
        x = a/b
        #print(x)
        y = math.atan(x)
        print ("True dip is", math.degrees(y), "degrees.")
        return math.degrees(y)

    def appdip(self,num1,num2):
        # a = true dip
        # b = angle of horizontal deviation from true dip direction
        # tan appdip = tan true * sin b
        a = math.radians(num1)
        b = math.radians(num2)
        x = math.tan(a) * math.sin(b)
        #print(x)
        # x = tan(apparent dip)
        y = math.atan(x)
        # y = apparent dip
        print(math.degrees(y))
        return math.degrees(y)

    def hydcon(self, num1, num2, num3, num4):
#Q, A, dh, dl
        Q = num1
        A = num2
        dh = num3
        dl = num4
        K = -Q/(A * (dh/dl))
        print("K =", K, "m/s")
        return K

#def perm
#k = K/(pg/mu)
#falling head perm
#constant head perm
#def plate bearing calculation

#def plate bearing calculation
#def darcy

#main

print("What calculation do you want to do?\n Press 1 for true dip calculator\n"
      " Press 2 for apparent dip\n Press 3 for hydraulic conductivity\n Or press any other key to exit")
menuchoice = input()
    
while menuchoice == "1" or "2" or "3":
    
    if menuchoice == "1":
        i = float(input("Input apparent bed thickness.\n"))
        j = float(input("Input horizontal distance.\n"))
        calc = Number()
        calc.truedip(i,j)
        

    elif menuchoice == "2":
        i = float(input("Input true dip in degrees\n"))
        j = float(input("Input angle of horizontal deviance from true dip direction.\n"))
        calc = Number()
        calc.appdip(i,j)
       
    elif menuchoice == "3":
        i = float(input("Input discharge in cumecs (Q)\n"))
        j = float(input("Input Area (A) in metres squared\n"))
        k = float(input("Input change in height (dh) in metres\n"))
        l = float(input("Input change in length (dl) in metres\n"))
        calc = Number()
        calc.hydcon(i,j,k,l)
    
    else:
        exit



