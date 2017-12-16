#!/usr/bin/python3

import sys,os
import platform as pform
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from gaussxw import *
import time
import banded
from math import sin,pi
from numpy import empty,array,arange
from pylab import plot,show
import pylab

#Some testing, please ignore

#rows, col = os.popen('stty size', 'r').read().split()
#rows = int(rows)/2
#col = int(col)/2

#os.system("resize -s 'rows col'")

#End testing.

def clearscreen():
    """
    """
    if pform.system() == 'Linux':
        os.system("clear")
    if pform.system() == 'Darwin':
        os.system("clear")
    if pform.system() == 'Windows':
        os.system("cls")


def homework1_1():
    """
    """
    while True:
        try:
            print("I will calculate the time it takes a ball to drop from a tower.\n")
            test = float(input('Please enter a tower height: '))
            if test > 0:
                print("It will take {first:2.2f} second(s) for the ball to hit the ground from a height of {second:2.2f} meter(s).\n".format( first=(np.sqrt(2*test/(9.8))),second=(test) ) )
                break
            else:
                print("That is not a valid height")
        except(TypeError, NameError, SyntaxError):
            print("That is not a valid height")


def homework1_2():
    """
    """
    def T(test):
        """
        """
        if test == -1:
            test = float(input('\nPlease enter an orbital period in seconds: '))
        G = 6.67e-11 #Newton's Gravitational Constant in m**3 kg**-1 s**-2
        M = 5.97e24  #Mass of earth in kg
        R = 6371000  #Earths radius in m
        return ( (G*M*test*test)/(4*(np.pi)**2) )**(0.33333333333333)


    def choose():
        """
        """
        while True:
            try:
                choice = int(input('Would you like to try again? (1 for yes or 2 for no): '))
                if choice == 1 or choice == 2:
                    return choice
                else:
                    print("\nPlease enter 1 or 2\n")
                    continue
            except(TypeError,NameError,SyntaxError):
                print("\nPlease enter 1 or 2\n")


    def factoid():
        """
        """
        print("\nBefore you leave, did you know the altitude for a 90 minute orbit is {first:2.2f} meters \nand {second:2.2f} meters for a 45 minute orbit.\n".format( first=(T(90*60)),second=(T(45*60)) ))
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
    """
    """
    while True:
        try:
            print("\n1) Deltoid Curve "
                  "\n2) Galilean Spiral"
                  "\n3) Fey's Function"
                  "\n4) Exit\n")
            test = int(input("Please choose a plot: "))
            if test == 1:
                x = np.linspace(0, 2*np.pi, 100)
                plt.plot(2*np.cos(x) + np.cos(2*x), 2*np.sin(x) - np.sin(2*x),color='black')
                plt.xlabel("x = 2cos(theta) + cos(2theta)")
                plt.ylabel("y = 2sin(theta) - sin(2theta)")
                plt.title("Deltoid Curve")
                plt.show()
            elif test == 2:
                y = np.linspace(0, 10, 1000)
                plt.plot( (y**2)*np.cos(y), (y**2)*np.sin(y),color='red')
                plt.xlabel("theta**2")
                plt.ylabel("r")
                plt.title("Galilean Spiral")
                plt.show()
            elif test == 3:
                y = np.linspace(0,24,1000)
                plt.plot( (np.exp(np.cos(y)) - 2*np.cos(4*y) + (np.sin(y/12))**5)*np.cos(y), (np.exp(np.cos(y)) - 2*np.cos(4*y) + (np.sin(y/12))**5)*np.sin(y) ,color='blue')
                plt.xlabel("exp(cos(theta)) - 2cos(4theta) + (sin(theta/12))^5")
                plt.ylabel("r")
                plt.title("Fey's Function")
                plt.show()
            elif test == 4:
                break
            else:
                print("\nThat is not a valid option\n")
        except(TypeError, NameError, SyntaxError):
            print("\nThat is not a valid option\n")


def homework2_2():
    """
    """
    def feig(r,x):
        """
        """
        return r*x*(1-x)


    def feigrun(r,n,x):
        """
        """
        temp = 0
        for i in range(n):
            temp = feig(r,x)
            x = temp
        return temp


    def feigtree(r,ni,nj,x):
        """
        """
        for i in range(ni):
            x2[i] = feigrun( (i*r)/ni, nj,x)
            x = np.random.rand()
        return x2

    #Defining initial conditions.    
    x = 0.5
    ni = 5000
    nj = 1000
    r = 4.0
    x2 = np.zeros(ni)

    clearscreen()

    print("Plotting Feigenbaum Plot")
    #call and plot feigtree
    plt.plot(np.linspace(0.0,r,ni),feigtree(r,ni,nj,x),'k*',ms=1)
    plt.title("Feigenbaum Plot")
    plt.xlabel("r")
    plt.ylabel("x")
    plt.axis([1,4,0,1])
    plt.show()


def homework3_1():
    """
    """
    def factorial(n):
        """
        """
        if n < 1:
            return 1
        elif n > 996:
            print("I can't calculate that")
            return ""
        else:
            return n*factorial(n-1)


    def f(n,z):
        """
        """
        return (1/((z-1)**2))*np.exp(-z/(1-z))*(z/(1-z))**(n-1)


    def gamma(n):
        """
        """
        quad = 1000
        x,w = gaussxwab(quad,0.0,1.0)
        total = 0
        for i in range(quad):
            total += w[i]*f(n,x[i])
        return total


    def getinput(n):
        """
        """
        if n == -1:
            return int(input("Please enter a value to calculate the factorial: "))
        if n == -2:
            return float(input("You have unlocked the gamma function! Please enter a floating point value: "))

    #User menu wrapped in a while loop and a try/except for error control.
    while True:
        try:
            n = getinput(-1)
            print("factorial of an integer variable gives: \n")
            print(factorial(int(n)))
            print("")
            print("factorial of a float variable gives: \n")
            print("{0:2.1f}".format( factorial(float(n))))
            print("\nThat's a difference of,\n")
            print
            print("{0:2.1f}\n".format( np.abs(factorial(float(n))-factorial(int(n)) ) ))
            
            choice = int(input("More? (1 = yes, 2 = no): "))
            if choice == 1:
                continue
            if choice == 2:
                break
            if choice == 3:
                n = getinput(-2)
                print(factorial(n))
            if choice == 4:
                n = getinput(-2)
                print(gamma(n))
        except(TypeError, NameError, SyntaxError):
            clearscreen()
            print("Please choose a value from the list\n")
        except(ValueError):
            clearscreen()
            print("Please enter integer values only")


def homework3_2():
    """
    """
    print("hw 3.2 Not completed yet\n")


def homework4_1():
    """
    """
    def f(x):
        if hasattr(x,"__len__") and (not isinstance(x,str)) == True:
            return [np.exp(-x[i]*x[i]) for i in range(len(x))]
        else:
            return np.exp(-x**2)


    def E(x1):
        """
        """
        quad = 100
        x,w = gaussxwab(quad,0,x1)
        tot = 0
        for i in range(quad):
            tot += w[i]*f(x[i])
        return tot

    print("\n   The integral: ∫exp(-t^2)dt  has no analytic solution. The integral can be\n"
          "   evaluated numerically for different bounds, 0 to x. The following plot evaluates\n"
          "   x from negative pi to pi.")

    y = np.zeros(199,dtype=float)
    x = np.zeros(199,dtype=float)

    for i in range(199):
        x[i] = -np.pi+i*0.01*np.pi
        y[i] = E(-np.pi+i*0.01*np.pi)

    plt.title("Plot of E(x) = ∫exp(-t^2)dt")
    plt.xlabel("x")
    plt.ylabel("E(x)")
    plt.plot(x,y)
    plt.show()
    print("\n   As can be seen from the plot, the integral grows asymptotically toward\n"
          "   a value of ±√π/2\n")
    while True:
        try:
            a=float(input("   Try for yourself. Please enter a value of x : "))
            x=E(a)
            print("   That gives ",x)
            b=int(input("   Would you like to try another value of x? (yes = 1, no = 2): "))
            if b == 1:
                continue
            elif b == 2:
                print("\nGoodbye.\n")
                break
        except(TypeError, NameError, SyntaxError,ValueError):
            clearscreen()
            print("Please choose a value from the list\n")
        except(KeyboardInterrupt):
            clearscreen()
            print("\nCan't use the values in the list? Ok goodbye!\n")
            break


def homework4_2():
    """
    """
    def f(x):
        return (x**4)/((np.exp(x)-1)**2)


    def Cv(T):
        """
        """
        quad = 50
        x,w = gaussxwab(quad,0,T)
        tot = 0
        for i in range(quad):
            tot += w[i]*f(x[i])
        return tot


    print("Would you like to see a plot of the Debye Temperature of Aluminum? ...\n\n")
    time.sleep(2)
    print("... Too late you are seeing it anyway.")
    y = np.zeros(495,dtype=float)
    x = np.zeros(495,dtype=float)
    cof = 9*0.001*6.022*(10**28)*1.38064852*(10**-23)*(428**-3)*np.exp(4) #V = 0.001 cubic meters 
    for T in range(5,500):
        x[T-5] = T
        y[T-5] = (T**3)*cof*Cv(428*(T**-1))

    plt.title("Plot of The Debye Temperature of Aluminum")
    plt.xlabel("T")
    plt.ylabel("Cv(T) = 9Vρk(T/Θ)^3∫exp(-t^2)dt")
    plt.plot(x,y)
    plt.show()


def homework5_1():
    N = int(input("Solving A Chain of Resistors. Please enter the number of unkown junction voltages.\n\n \tN = "))
    A = np.zeros((N,N))
    V = 5  #voltage of upper rail
    u = 2  #number of non-zero values above diagonal of matrix A
    d = u  #number of non-zero values below diagonal of matrix A
    # populate A in a very ugly way!
    for i in range(2,N-2):
        A[i,(i-2)] = -1
        A[i,(i-1)] = -1
        A[i,(i)] =  4
        A[i,(i+1)] = -1
        A[i,(i+2)] = -1
    A[0,0] = 3
    A[0,1] = -1
    A[0,2] = -1
    A[1,0] = -1
    A[1,1] = 4
    A[1,2] = -1
    A[1,3] = -1
    A[N-1,N-1] = 3
    A[N-1,N-2] = -1
    A[N-1,N-3] = -1
    A[N-2,N-1] = -1
    A[N-2,N-2] = 4
    A[N-2,N-3] = -1
    A[N-2,N-4] = -1
    print(A)
    w = np.zeros(N)
    w[0] = V
    w[1] = V
    if ( N <= 20 ):
        #solve Av=w
        v = np.linalg.solve(A,w)
        print(v)

    if ( N > 20 ):
        #reorder matrix A into matrix diagonal ordered form
        Anew = np.zeros((1+u+d,N))
        k=0
        for i in range(N):
            for j in range(u+1):
                Anew[(u + i - k-j),k] = A[i,k-j]
            for l in range(1,d+1):
                if ( i < N-l ):
                    Anew[(u + i - k+l),k] = A[i+l,k]
            k+=1
        print(Anew)
        # solve Av=w
        v = banded.banded(Anew,w,u,d)
        print(v)
        #sanity check of all values being less than 5
        for i in range(N):
            if ( v[i] > 5 ):
                print("greater than 5!!!!!")
                check = 1
            else:
                check = 0
        if ( check == 0 ):
            print("All less than 5!!!!")
        for i in range(N):
            if ( v[i] < 0 ):
                print("less than 0!!!!!")
                check = 1
            else:
                check = 0
        if ( check == 0 ):
            print("All greater than 0!!!!")


def homework6_1():
    A = 1
    B = 3
    
    a = 0.0
    b = 20.0
    N = 100          # Number of "big steps"
    H = (b-a)/N      # Size of "big steps"
    delta = 1e-10     # Required position accuracy per unit time
    
    def f(r):
        x = r[0]
        y = r[1]
        fx = 1 - (B + 1)*x + A*x*x*y
        fy = B*x - A*x*x*y
        return array([fx,fy],float)
    
    tpoints = arange(a,b,H)
    xpoints = []
    ypoints = []
    r = array([0.0,0.0],float)
    
    # Do the "big steps" of size H
    for t in tpoints:
    
        xpoints.append(r[0])
        ypoints.append(r[1])
    
        # Do one modified midpoint step to get things started
        n = 1
        r1 = r + 0.5*H*f(r)
        r2 = r + H*f(r1)
    
        # The array R1 stores the first row of the
        # extrapolation table, which contains only the single
        # modified midpoint estimate of the solution at the
        # end of the interval
        R1 = empty([1,2],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))
    
        # Now increase n until the required accuracy is reached
        error = 2*H*delta
        while error>H*delta:
    
            n += 1
            h = H/n
    
            # Modified midpoint method
            r1 = r + 0.5*h*f(r)
            r2 = r + h*f(r1)
            for i in range(n-1):
                r1 += h*f(r2)
                r2 += h*f(r1)
    
            # Calculate extrapolation estimates.  Arrays R1 and R2
            # hold the two most recent lines of the table
            R2 = R1
            R1 = empty([n,2],float)
            R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
            for m in range(1,n):
                epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
                R1[m] = R1[m-1] + epsilon
            error = abs(epsilon[0])
    
        # Set r equal to the most accurate estimate we have,
        # before moving on to the next big step
        r = R1[n-1]
    
    # Plot the results
    pylab.title("Belousov-Zhabotinsky Reaction")
    pylab.ylabel("Concentration, a.u.")
    pylab.xlabel("time, t")
    plot(tpoints,xpoints)
    plot(tpoints,xpoints,"b.",label='concentration x')
    plot(tpoints,ypoints)
    plot(tpoints,ypoints,"r.",label='concentration y')
    pylab.annotate('Rapid change\nin concentration',xy=(8.8,2.6),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.05))
    pylab.legend()
    show()


def homework8_1():


    def f(x):
        return x**(-1/2)*(np.exp(x)+1)**-1


    def p(x):
        return 1/(2*x**(-1/2))

    def mc():
        print("\n   The integral: ∫x^(-1/2)/(exp(x)+1)dx will be calculated using a \n"
              "                 Monte Carlo with a importance sampling, w(x) = x^(-1/2)\n")
        N = 1000000
        count = 0
        x = []
        for i in range(N):
            x[i] = 2*np.random.rand()
            y = np.random.rand()
            if y < f(x):
                count +=1
        I = 2*count/N
        print("The result is ... ",I)
        trash = input("One second...")


    mc()


reset = True
while reset:  # While loop structure used for error handling.
    try:
        hwnum = 0
        print("\n    1)  Introduction to Python 1.1"
              "\n    2)  Introduction to Python 1.2\n"
              "\n    3)  Plotting in Python 2.1"
              "\n    4)  Plotting in Python 2.2\n"
              "\n    5)  Accuracy and Speed 3.1"
              "\n    6)  Accuracy and Speed 3.2\n"
              "\n    7)  Integration 4.1"
              "\n    8)  Integration 4.2\n"
              "\n    9)  Solving Equations 5.1\n"
              "\n   10)  ODE's 6.1\n"
              "\n   11)  Monte Carlo 8.1"
              "\n\n   12)  Exit\n")
        hwnum = int(input("Please choose which HW assignment: "))
        if hwnum == 1:
            clearscreen()
            homework1_1()
        elif hwnum == 2:
            clearscreen()
            homework1_2()
        elif hwnum == 3:
            clearscreen()
            homework2_1()
        elif hwnum == 4:
            clearscreen()
            homework2_2()
        elif hwnum == 5:
            clearscreen()
            homework3_1()
        elif hwnum == 6:
            clearscreen()
            homework3_2()
        elif hwnum == 7:
            clearscreen()
            homework4_1()
        elif hwnum == 8:
            clearscreen()
            homework4_2()
        elif hwnum == 9:
            clearscreen()
            homework5_1()
        elif hwnum == 10:
            clearscreen()
            homework6_1()
        elif hwnum == 11:
            clearscreen()
            homework8_1()
        elif hwnum == 12:
            clearscreen()
            reset = False
            break
        elif not isinstance(hwnum,int):
            clearscreen()
            print("Please choose a value from the list\n")
        else:
            clearscreen()
            print("Please choose a value from the list\n")
#    except(TypeError, NameError, SyntaxError,ValueError):
#        clearscreen()
#        print("Please choose a value from the list\n")
    except(KeyboardInterrupt):
        clearscreen()
        print("\nCan't use the values in the list? Ok goodbye!\n")
        break
