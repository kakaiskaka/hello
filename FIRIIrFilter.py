#Q6A) Desigin simple FIR Filter  

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
# user defined function for pole zero plot
def zplane (num,den):
# convert transfer function H(Z) to poles and zeros
(zeros,poles,gain)=signal.tf2zpk(num,den)
angle=np.linspace(0,2*np.pi,100)
cirx=np.sin(angle)
ciry=np.cos(angle)
plt.plot(poles.real,poles.imag,'bX',zeros.real,zeros.imag,'ro',cirx,ciry,'k-')
plt.xlabel('Red')
plt.ylabel('Imag')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.grid()
return(zeros,poles,gain)
# LPF-IIR
num=[1,0]
den=[1,-0.9]
plt.figure(1)
plt.subplot(1,2,1)
zplane(num,den)
plt.title("LPF-IIR")
# magnitude response
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num,den)
Hm=np.abs(H)
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.title("LPF-IIR MAGNITUDE RESPONSE")
# HPF-IIR
num=[1,0]
den=[1,0.9]
plt.figure(2)
plt.subplot(1,2,1)
zplane(num,den)
plt.title("HPF-IIR")
# magnitude response
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num,den)
Hm=np.abs(H)
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.title("HPF-IIR MAGNITUDE RESPONSE")
# HPF-FIR
num=[1,-0.9]
den=[1,0]
plt.figure(3)
plt.subplot(1,2,1)
zplane(num,den)
plt.title("HPF-FIR")
# magnitude response
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num,den)
Hm=np.abs(H)
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.title("HPF-FIR MAGNITUDE RESPONSE")
# LPF-FIR
num=[1,0.9]
den=[1,0]
plt.figure(4)
plt.subplot(1,2,1)
zplane(num,den)
plt.title("LPF-FIR")
# magnitude response
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num,den)
Hm=np.abs(H)
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.title("LPF-FIR MAGNITUDE RESPONSE")
# ALL PASS FILTER
num=[1,-2]
den=[1,-0.5]
plt.figure(5)
plt.subplot(1,2,1)
zplane(num,den)
plt.title("ALL PASS FILTER")
# magnitude response
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num,den)
Hm=np.abs(H)
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.title("ALL PASS FILTER MAGNITUDE RESPONSE")