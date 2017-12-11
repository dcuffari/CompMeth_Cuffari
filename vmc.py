#!/usr/bin/python
import numpy as np
import random as rand

class Atom(object):


    def __init__(self,re1,re2,alpha):
        self.alpha = alpha
        self.updatepos(re1,re2)


    def updatepos(self,re1,re2):
        self.r1  = np.sqrt(sum(i*i for i in re1))
        self.r2  = np.sqrt(sum(i*i for i in re2))
        self.r12 = np.sqrt(sum((i-j)*(i-j) for i,j in zip(re1,re2)))
        self.re1 = re1
        self.re2 = re2


    def psiE(self):
        return np.exp(-2*self.r1-2*self.r2+self.r12/(2*(1+self.alpha*self.r12)))


    def localE(self):
        dotProd = 0
        dotProd = sum(((i-j)/self.r12)*((i/self.r1)-(j/self.r2)) for i,j in zip(self.re1,self.re2))
        denom = 1/(1+self.alpha*self.r12)
        return -4+self.alpha*(denom+denom**2+denom**3)-0.25*(denom**4)+dotProd*(denom**2)


def psiT(re1,re2,alpha):
    r1  = np.sqrt(sum(i*i for i in re1))
    r2  = np.sqrt(sum(i*i for i in re2))
    r12 = np.sqrt(sum((i-j)*(i-j) for i,j in zip(re1,re2)))
    return np.exp(-2*r1-2*r2+r12/(2*(1+alpha*r12)))


def iniwalkers(N,ne,ndim):
    return [[[rand.random()-0.5 for x in range(ndim)] for y in range(ne) ] for z in range(N) ]


def metroStep(He,walker,r,alpha,delta,nAccept,esum,eSqdSum):
    He.updatepos((r[walker][0][0],r[walker][0][1],r[walker][0][2]),(r[walker][1][0],r[walker][1][1],r[walker][1][2]))
    rtrial1 = [ i + delta*(2*rand.random()-1) for i in He.re1 ]
    rtrial2 = [ i + delta*(2*rand.random()-1) for i in He.re2 ]
    w = psiT(rtrial1,rtrial2,alpha)/He.psiE()
    if rand.random() < w*w:
        r[walker][0][:] = He.re1 = rtrial1
        r[walker][1][:] = He.re2 = rtrial2
        nAccept+=1
    esum += He.localE()
    eSqdSum += He.localE()*He.localE()
    return esum, eSqdSum, nAccept


def oneMonteCarloStep(N,He,r,alpha,delta,nAccept,esum,eSqdSum):
    for i in range(N):
        esum, eSqdSum, nAccept = metroStep(He,i,r,alpha,delta,nAccept,esum,eSqdSum)
    return esum, eSqdSum,nAccept


#Start main
ndim=3
ne=2
esum = 0
eSqdSum = 0


N=1000
alpha = 0.5
delta = 1
r = iniwalkers(N,ne,ndim)
He = Atom(r[0][0][:],r[9][0][:],alpha)

MCSteps = 1000
thermSteps = int(0.2*MCSteps)
adjustInterval = int(0.1*thermSteps)+1
nAccept = 0

for i in range(thermSteps):
    esum, eSqdSum, nAccept = oneMonteCarloStep(N,He,r,alpha,delta,nAccept,esum,eSqdSum)
    if (i+1)%adjustInterval == 0:
        delta *= nAccept/(0.5*N*adjustInterval)
        nAccept = 0
print "Adjusted step size delta = ",delta

esum = eSqdSum = 0
nAccept = 0

print "Performing", MCSteps, " production steps ..."
for i in range(MCSteps):
    esum, eSqdSum, nAccept = oneMonteCarloStep(N,He,r,alpha,delta,nAccept,esum,eSqdSum)

eAve = esum / N / MCSteps
eVar = eSqdSum / N / MCSteps - eAve*eAve
error = np.sqrt(eVar) / np.sqrt(N*MCSteps)
print "\n <Energy> = ",eAve," +/- ", error
print "\n Variance = ",eVar
