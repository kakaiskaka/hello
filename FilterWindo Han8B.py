#Q8) FIR window Problem hanning And reactangle
# Import packages and modules
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
N=11
# Use inbuilt function for FIR filter
b1=signal.firwin(N,cutoff=[0.25,0.75],window='rectangular',pass_zero=False)
a1=1   # Denominator of H(Z)
# To plot magnitude response
plt.figure(1)
w,H=signal.freqz(b1,a1)
Hm=np.abs(H)   #magnitude omly
Hdb=20*np.log10(Hm)   # log magnitude
plt.plot(w/max(w),Hdb,color='red')
plt.title('FIR BPF having cutoff freq pi/4 to 3pi/4')
plt.xlabel('normalized freq w--->')
plt.ylabel('dB magnitude')
plt.grid()
print(np.float16(b1))

b2=signal.firwin(N,cutoff=[0.25,0.75],window='hamming',pass_zero=False)
a2=1   # Denominator of H(Z)
# To plot magnitude response
plt.figure(1)
w,H=signal.freqz(b2,a2)
Hm=np.abs(H)   #magnitude omly
Hdb=20*np.log10(Hm)   # log magnitude
plt.plot(w/max(w),Hdb,color='green')
plt.title('FIR BPF having cutoff freq pi/4 to 3pi/4')
plt.xlabel('normalized freq w--->')
plt.ylabel('dB magnitude')
plt.grid()
print('coefficient of FIR BPF using Hamming',np.float16(b2))
plt.legend(['rectangular','hamming'])

