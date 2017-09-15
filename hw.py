#!/usr/bin/python
import sys,os
import platform as pform
import numpy as np

def clearscreen():
    if pform.system() == 'Linux':
        os.system("clear")
    if pform.system() == 'Darwin':
        os.system("clear")
    if pform.system() == 'Windows':
        os.system("cls")

def homework1_1():
    test = float(input('Please enter a tower height: '))
    print("It will take {0:2.2f} seconds for the ball to hit the ground.\n".format( np.sqrt(2*test/(9.8)) ))


def homework1_2():
    print("hw 1.2 Not completed yet\n")


def homework2_1():
    print("hw 2.1 Not completed yet\n")


def homework3_1():
    print("hw 3.1 Not completed yet\n")


while True:  # While loop structure used for error handling.
    try:
        print("\n    1)  HW 1 problem 1"
              "\n    2)  HW 1 problem 2"
              "\n    3)  HW 2 problem 1"
              "\n    4)  HW 3 problem 1"
              "\n    5)  Exit\n")
        hwnum = input("Please choose which HW assignment: ")
        if hwnum == 1:
            clearscreen()
            homework1_1()
        if hwnum == 2:
            clearscreen()
            homework1_2()
        if hwnum == 3:
            clearscreen()
            homework2_1()
        if hwnum == 4:
            clearscreen()
            homework3_1()
        if hwnum == 5:
            clearscreen()
            break
        if not isinstance(hwnum,int):
            clearscreen()
            print("Please choose a value from the list\n")
        else:
            clearscreen()
            print("Please choose a value from the list\n")
    except NameError:
        clearscreen()
        print("Please choose a value from the list\n")
    except(TypeError, NameError, SyntaxError):
        clearscreen()
        print("Please choose a value from the list\n")

