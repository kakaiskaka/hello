#Q6B) FIR filter 
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
    plt.xlabel('Re')
    plt.ylabel('Imag')
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.grid()
    return(zeros,poles,gain)
#IIR-BPF
num1=[1,0,0]
den1=[1,0,0.49]
plt.figure(1)
plt.subplot(1,2,1)
zplane(num1,den1)
# plot pole zero diagram and mag response
plt.title('IIR-BPF')
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num1,den1)
Hm=np.abs(H)
# magnitude response
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.xlabel('w---->')
plt.ylabel('mag response')
plt.grid()
# NOTCH FILTER
num1=[1,0,1]
den1=[1,0,0.49]
plt.figure(2)
plt.subplot(1,2,1)
zplane(num1,den1)
# plot pole zero diagram and mag response
plt.title('Notch filter')
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num1,den1)
Hm=np.abs(H)
# magnitude response
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.xlabel('w---->')
plt.ylabel('mag response')
plt.grid()
# COMB FILTER
num1=[1,0,0,0,-1]
den1=[1,0,0,0,0]
plt.figure(3)
plt.subplot(1,2,1)
zplane(num1,den1)
# plot pole zero diagram and mag response
plt.title('COMB filter')
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num1,den1)
Hm=np.abs(H)
# magnitude response
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.xlabel('w---->')
plt.ylabel('mag response')
plt.grid()
#comb filter
num1=[1,0,0,0,1]
den1=[1,0,0,0,0]
plt.figure(4)
plt.subplot(1,2,1)
zplane(num1,den1)
# plot pole zero diagram and mag response
plt.title('COMB filter')
w=np.linspace(0,np.pi,100)
(w,H)=signal.freqz(num1,den1)
Hm=np.abs(H)
# magnitude response
plt.subplot(1,2,2)
plt.plot(w,Hm)
plt.xlabel('w---->')
plt.ylabel('mag response')
plt.grid()


