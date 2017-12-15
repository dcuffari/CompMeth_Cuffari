#!/usr/bin/python3


import numpy as np
import random as rand
from matplotlib import pyplot as plt

"""This code was written using the following source as a guide.
   https://www.acsu.buffalo.edu/~phygons/cp2/topic5/topic5.pdf
   Last accessed on Dec. 11th 2017.
"""


class Atom(object):
    """The Atom class is used to define the trial wavefunction of
       two electrons interacting with (a) proton(s).

    """
    def __init__(self,re1,re2,R1,R2,alpha):
        self.alpha = alpha
        self.updatepos(re1,re2,R1,R2)


    def updatepos(self,re1,re2,R1,R2):
        """sets the positions of the electrons and calculates the
           magnitude of their displacements from the origin.
       
        """
        self.r1  = np.sqrt(sum(i*i for i in re1))
        self.r2  = np.sqrt(sum(i*i for i in re2))
        self.r12 = np.sqrt(sum((i-j)*(i-j) for i,j in zip(re1,re2)))
        self.re1 = re1
        self.re2 = re2
        self.R1  = R1
        self.R2  = R2


    def psiE(self):
        """calculates the trial wavefunction based on the positions of
           the electrons and the Jastrow variational parameter alpha.
        """
        return np.exp(-2*self.r1-2*self.r2+self.r12/(2*(1+self.alpha*self.r12)))


    def localE(self):
        """Calculates the local energy of the atomic configuration.
        """
        dotProd = 0
        dotProd = sum(((i-j)/self.r12)*((i/self.r1)-(j/self.r2)) for i,j in zip(self.re1,self.re2))
        denom = 1/(1+self.alpha*self.r12)
        return -4+self.alpha*(denom+denom**2+denom**3)-0.25*(denom**4)+dotProd*(denom**2)


def psiT(re1,re2,alpha):
    """Calculates the local energy of the atomic configuration.
    """
    r1  = np.sqrt(sum(i*i for i in re1))
    r2  = np.sqrt(sum(i*i for i in re2))
    r12 = np.sqrt(sum((i-j)*(i-j) for i,j in zip(re1,re2)))
    return np.exp(-2*r1-2*r2+r12/(2*(1+alpha*r12)))


def iniwalkers(N,ne,ndim):
    """initializes the random walkers used in the VMC.
    """
    return [[[rand.random()-0.5 for x in range(ndim)] for y in range(ne) ] for z in range(N) ]


def metroStep(He,walker,r,alpha,delta,nAccept,esum,eSqdSum,collectwaves,collectposit):
    """compares trial wavefunctions defined by the random set of walkers
       to trial wavefunctions that are randomly incramented/decramented,
       then returns the total energy and acceptance count.
    """
    #updates the positions of the electrons with the first walker
    He.updatepos((r[walker][0][0],r[walker][0][1],r[walker][0][2]),(r[walker][1][0],r[walker][1][1],r[walker][1][2]),(0,0,0),(1,0,0))
    #generates trial position advancements to electron 1 and 2
    rtrial1 = [ i + delta*(2*rand.random()-1) for i in He.re1 ]
    rtrial2 = [ i + delta*(2*rand.random()-1) for i in He.re2 ]
    #calculates the ratio of the trial wavefunction to current wavefunction
    w = psiT(rtrial1,rtrial2,alpha)/(He.psiE())
    #checking if trial wavefunction can be accepted
    if rand.random() < w*w:
        r[walker][0][:] = He.re1 = rtrial1
        r[walker][1][:] = He.re2 = rtrial2
        nAccept+=1
    #add local energy of accepted wavefunction to the total
    esum += He.localE()
    eSqdSum += He.localE()*He.localE()
    #used to collect additional information about system
    collectwaves[walker] = He.psiE()
    collectposit[walker][0][:] = He.r1,He.r2,He.r12
    return esum, eSqdSum, nAccept, collectwaves, collectposit


def oneMonteCarloStep(N,He,r,alpha,delta,nAccept,esum,eSqdSum):
    """Performs a Monte Carlo step for all walkers.
    """
    #defines arrays for collection additional information about system
    collectwaves = np.zeros(N)
    collectposit = [[[0.0 for x in range(3)] for y in range(2) ] for z in range(N) ]
    #performs one Monte Carlo step for all walkers by calling metroStep
    for i in range(N):
        esum, eSqdSum, nAccept, collectwaves, collectposit = metroStep(He,i,r,alpha,delta,nAccept,esum,eSqdSum,collectwaves,collectposit)
    return esum, eSqdSum, nAccept, collectwaves, collectposit


def run(alpha):
    """Driver function for simulation as a function of alpha
    """
    ndim=3
    ne=2
    esum = 0
    eSqdSum = 0

    N=1000
    delta = 1
    r = iniwalkers(N,ne,ndim)
    He = Atom(r[0][0][:],r[9][0][:],(0,0,0),(1,0,0),alpha)
    cp = [[[0.0 for x in range(3)] for y in range(ne) ] for z in range(N) ]
    cw = np.zeros(N)

    MCSteps = 1000
    thermSteps = int(0.2*MCSteps)
    adjustInterval = int(0.1*thermSteps)+1
    nAccept = 0

    print("Performing ", thermSteps, " thermalization steps ...")
    for i in range(thermSteps):
        esum, eSqdSum, nAccept, cw, cp = oneMonteCarloStep(N,He,r,alpha,delta,nAccept,esum,eSqdSum)
        if (i+1)%adjustInterval == 0:
            delta *= nAccept/(0.5*N*adjustInterval)
            nAccept = 0
    print("Adjusted step size delta = ",delta)

    esum = eSqdSum = 0
    nAccept = 0

    print("Performing", MCSteps, " production steps ...")
    for i in range(MCSteps):
        esum, eSqdSum, nAccept, cw, cp = oneMonteCarloStep(N,He,r,alpha,delta,nAccept,esum,eSqdSum)

    eAve = esum / N / MCSteps
    eVar = eSqdSum / N / MCSteps - eAve*eAve
    error = np.sqrt(eVar) / np.sqrt(N*MCSteps)
    print("\n <Energy> = ",eAve," +/- ", error)
    print("\n Variance = ",eVar)

    print("vmc complete plotting ...")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [ cp[i][0][0] for i in range(N) ]
    y = [ cp[i][0][1] for i in range(N) ]
    z=cw
    ax.scatter(x,y,z, c='r', marker='o')
    
    plt.show()

    plt.scatter(x,z)
    plt.show()

#call driver and loop alpha
for i in range(10):
    run(i*0.1)
