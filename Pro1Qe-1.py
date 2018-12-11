#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 01:26:33 2017

@author: Xianan
"""

from numpy import arange,sqrt,exp,absolute,pi,tan,sin,cos,meshgrid,empty,log,real,imag
from pylab import contour, xlabel, title,show,legend,ylabel,contourf,colorbar
from gaussxw import gaussxwab
#Here let a = 1
a = 1
A = 1
wavelength = a/5.
def f(x,xp,y,yp,D):
    #re = empty([length,length])
    #p = 0
    #q = 0    
    re1 = real(D/sqrt((x-xp)**2+(y-yp)**2+D**2)*(1+D/sqrt((x-xp)**2+(y-yp)**2+D**2))*exp(1j*2*pi/wavelength*sqrt((x-xp)**2+(y-yp)**2+D**2)))
    re2 = imag(D/sqrt((x-xp)**2+(y-yp)**2+D**2)*(1+D/sqrt((x-xp)**2+(y-yp)**2+D**2))*exp(1j*2*pi/wavelength*sqrt((x-xp)**2+(y-yp)**2+D**2)))
    return re1,re2

N = 20
point,w = gaussxwab(N,-a/2.,a/2.)

s = 0+0j


D = 0.5*a
x = 0
y = 0
length = len(arange(-1*a,1*a,0.02))
result = empty([length,length],complex)
for p in arange(-1*a,1*a,0.02):
    for q in arange(-1*a,1*a,0.02):
        for m in range(N):
            for n in range(N):
                re1,re2 = f(p,point[m],q,point[n],D)
                s += w[m]*w[n]*(re1+1j*re2)
        result[x,y] = s
        y += 1
        s = 0+0j
    x += 1
    y = 0
x = arange(-1*a,1*a,0.02)
y = arange(-1*a,1*a,0.02)
X,Y = meshgrid(x,y)
#print(result)
#plot(s)
amp = absolute(result)
contourf(X,Y,log(amp**2*(2*pi/wavelength)**2*A**2/16/a**2/pi/pi/D/D))
colorbar()


#legend()
title('D = 0.5a')
xlabel('x (unit in a)')
ylabel('y (unit in a)')
