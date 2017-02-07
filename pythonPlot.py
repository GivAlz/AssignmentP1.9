#!/bin/python
#Program written by Giovanni Alzetta for the P1.9 Course, first assignment
#We are asked to build a simple python script: the aim is to use git

#Used libraries
##Graphical libraries
import matplotlib.pyplot as plt
##Numerical libraries
import numpy as np

#First: handle user input
print("This is assignment P1.9")
choice = input("Please, to choose the function, insert an integer: ")

try:
    choice = int(choice)
except ValueError:
    print("You must insert an integer; default value 1 will be used")
    choice = int(1)
