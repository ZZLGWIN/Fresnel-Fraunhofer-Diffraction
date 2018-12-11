# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import pi
from pylab import plot, xlabel, title,legend
from numpy import arange,sin,cos

#Here all spatial variables are in unit of b.
def I_Frau(D):
    theta = arange(0,pi/2,0.01)
    beta = 1/2*2*pi/(1/5)*sin(theta)
    return cos(theta)**2*cos(theta/2)**4*(sin(beta)/beta)**2

D = 1
plot(arange(0,pi/2,0.01),I_Frau(D),'k--',label = 'D = b')

D = 5
plot(arange(0,pi/2,0.01),I_Frau(D),'k:',label = 'D = 5b')

D = 10
plot(arange(0,pi/2,0.01),I_Frau(D),'k',label = 'D = 10b')

D = 50
plot(arange(0,pi/2,0.01),I_Frau(D),'r',label = 'D = 50b')
legend()
title('Fraunhofer diffraction')
xlabel('Theta')
ylabel('IFres(theta)/Ifrau(0)')