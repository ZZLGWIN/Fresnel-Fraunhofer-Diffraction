# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:24:44 2017

@author: Xianan
"""
from numpy import arange,sqrt,exp,absolute,pi,tan,sin,cos,real,imag
from pylab import plot, xlabel, title,show,legend,ylabel
from gaussxw import gaussxwab
#Here all spatial variables are in unit of b.
def I_Frau(D):
    theta = arange(0,pi/2,0.01)
    beta = 1/2*2*pi/(1/5)*sin(theta)
    return cos(theta)**2*cos(theta/2)**4*(sin(beta)/beta)**2
def f(xp,D):
    theta = arange(0,pi/2,0.01)
    x = D*tan(theta)
    re1 = real(sqrt((x-xp)**2/D**2+1)+1)/((x-xp)**2/D**2+1)*exp(1j*sqrt((x-xp)**2+D**2))
    re2 = imag(sqrt((x-xp)**2/D**2+1)+1)/((x-xp)**2/D**2+1)*exp(1j*sqrt((x-xp)**2+D**2))
    return re1,re2

s = 0
N = 100
x,w = gaussxwab(N,-0.5,0.5)



D = 1
for k in range(N):
    re1,re2 = f(x[k],D)
    s += w[k]*(re1+1j*re2)

plot(arange(0,pi/2,0.01),absolute(s)**2/4,'k--',label = 'D = b, Fresnel')
plot(arange(0,pi/2,0.01),I_Frau(D),'r--',label = 'D = b, Fraunhofer')

x,w = gaussxwab(N,-0.5,0.5)
s = 0
D = 5
for k in range(N):
    re1,re2 = f(x[k],D)
    s += w[k]*(re1+1j*re2)

plot(arange(0,pi/2,0.01),absolute(s)**2/4,'k:', label = 'D = 5b, Fresnel')
plot(arange(0,pi/2,0.01),I_Frau(D),'r:',label = 'D = 5b, Fraunhofer')

x,w = gaussxwab(N,-0.5,0.5)
D = 10
s = 0
for k in range(N):
    re1,re2 = f(x[k],D)
    s += w[k]*(re1+1j*re2)

plot(arange(0,pi/2,0.01),absolute(s)**2/4,'k', label = 'D = 10b, Fresnel')
plot(arange(0,pi/2,0.01),I_Frau(D),'r',label = 'D = 10b, Fraunhofer')

x,w = gaussxwab(N,-0.5,0.5)
D = 50
s = 0
for k in range(N):
    re1,re2 = f(x[k],D)
    s += w[k]*(re1+1j*re2)

plot(arange(0,pi/2,0.01),absolute(s)**2/4,'kx',label = 'D = 50b, Fresnel')
plot(arange(0,pi/2,0.01),I_Frau(D),'rx',label = 'D = 50b, Fraunhofer')



legend()
xlabel('Theta')
ylabel('Normalized Intensity')
