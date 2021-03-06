#!/bin/python
#Program written by Giovanni Alzetta for the P1.9 Course, first assignment
#We are asked to build a simple python script: the aim is to use git

#Used libraries
##Graphical libraries
import matplotlib.pyplot as plt
##Numerical libraries
import numpy as np

#Python 2 and 3 compatibility
try:
   input = raw_input
except NameError:
   pass

#First: handle user input
print("This is assignment P1.9")
choice = input("Please, to choose the function, insert an integer: ")

while(len(choice)==0):
    print("Usage: this is a list of integer and the corresponding functions:")
    print("1	f(x)=x")
    print("2	f(x)=x**2")
    print("3	f(x)=x**3")
    print("4	f(x)=sin(x)")
    print("5	f(x)=cos(x)")
    print("6	f(x)=tan(x)")
    print("7	f(x)=exp(x)")
    print("8	f(x)=sqrt(|x|)")
    choice = input("Insert choosen function: ")
try:
    choice = int(choice)
except ValueError:
    print("You must insert an integer; default value 1 will be used")
    choice = int(1)
#Second: filling in the lists

def multif(x,my_type):
    if(my_type==1):
        return x
    elif(my_type==4):
        return np.sin(x)
    elif(my_type==5):
        return np.cos(x)
    elif(my_type==6):
        return np.tan(x)
    elif(my_type==2):
        return x*x
    elif(my_type==3):
        return x*x*x
    elif(my_type==7):
        return np.exp(x)
    elif(my_type==8):
        return np.sqrt(np.abs(x))
    #Added an else, in case something goes wrong!
    else:
        print("Something is wrong! Using 0 function!")
        return 0

f = lambda x: multif(x,choice)

xval = np.arange(-3.0,3.1,0.1)
yval = [f(x) for x in xval]
#Third: plotting the values

plt.plot(xval,yval,'blue')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
