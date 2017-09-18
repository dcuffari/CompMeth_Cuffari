#!/usr/bin/python
import sys,os
import platform as pform
import numpy as np


rows, col = os.popen('stty size', 'r').read().split()
rows = int(rows)/2
col = int(col)/2


def clearscreen():
    if pform.system() == 'Linux':
        os.system("clear")
    if pform.system() == 'Darwin':
        os.system("clear")
    if pform.system() == 'Windows':
        os.system("cls")


def homework1_1():
    test = float(input('Please enter a tower height: '))
    print("It will take {first:2.2f} seconds for the ball to hit the ground from a height of {second:2.2f} meter(s).\n".format( first=(np.sqrt(2*test/(9.8))),second=(test) ) )


def homework1_2():

    def T(test):
        if test == -1:
            test = float(input('Please enter an orbital period in seconds: '))
        G = 6.67e-11 #Newton's Gravitational Constant in m**3 kg**-1 s**-2
        M = 5.97e24  #Mass of earth in kg
        R = 6371000  #Earths radius in m
        return ( (G*M*test*test)/(4*(np.pi)**2) )**(0.33333333333333)


    def choose():
        while True:
            try:
                choice = input('Would you like to try again? (1 for yes or 2 for no): ')
                if choice == 1 or choice == 2:
                    return choice
                else:
                    print("\nPlease enter 1 or 2\n")
                    continue
            except(TypeError,NameError,SyntaxError):
                print("\nPlease enter 1 or 2\n")
            


    def factoid():
        print("Before you leave, did you know the altitude for a 90 minute orbit is {first:2.2f} meters \nand {second:2.2f} meters for a 45 minute orbit.\n".format( first=(T(90*60)),second=(T(45*60)) ))
        print("Also, the altitude for a geosynchronous (23.93 hours) satellite is {first:2.2f} meters,\nwhile a 24 hour satellite is {second:2.2f} meters.".format( first=(T(23.93*60*60)),second=(T(24*60*60)) ))
        print("That's a difference of {0:2.2f} meters.\n".format( T(24*60*60)-T(23.93*60*60) ) )


    while True:
        try:
            Tp = T(-1)
            if Tp < 2000000:
                os.system("echo -e '\007'")
                print("Your orbital period will result in an unstable orbit and crash into earth.\n")
                choice = choose()
                if choice == 1:
                    continue
                elif choice == 2:
                    factoid()
                    break
                else:
                    continue
            elif Tp > 36000000:
                os.system("echo -e '\007'")
                print("Your orbital period will result in an unstable orbit and escape earths gravity.\n")
                choice = choose()
                if choice == 1:
                    continue
                elif choice == 2:
                    factoid()
                    break
                else:
                    continue
            else:
                print("\nYour satellite will have an altitude of {first:2.2f} meter(s).\n".format( first=(Tp) ) )
                factoid()
                break
        except(TypeError, NameError, SyntaxError):
            print("You did not enter a valid option, try again.\n")


def homework2_1():
    
    print("hw 2.1 Not completed yet\n")


def homework3_1():
    print("hw 3.1 Not completed yet\n")


while True:  # While loop structure used for error handling.
    try:
        hwnum = 0
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
#            clearscreen()
            print("Please choose a value from the list\n")
        else:
#            clearscreen()
            print("Please choose a value from the list\n")
    except NameError:
#        clearscreen()
        print("Please choose a value from the list\n")
    except(TypeError, NameError, SyntaxError):
#        clearscreen()
        print("Please choose a value from the list\n")
