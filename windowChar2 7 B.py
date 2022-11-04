#Q7B)Window character
# Time domain and frequency domain characteristics of different window function
# import pakages
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal 

# Define window length
N=51
M=N-1
#Time range
n=np.arange(N)
# Define rectangular window
w1=np.ones(N)
plt.figure(1)
plt.subplot(1,2,1)
plt.stem(n,w1,use_line_collection=True)
plt.title('Rectangular window')
plt.xlabel('Time index n--->')

# To plot magnitude response of rectangular window
a=1    # denominator
w,H=signal.freqz(w1,a)
Hm=np.abs(H)   #magnitude omly
Hdb=20*np.log10(Hm)   # log magnitude
plt.subplot(1,2,2)
plt.plot(w/max(w),Hdb,color='red')
plt.title('magnitude response')
plt.xlabel('normalized freq w--->')
plt.ylabel('dB magnitude')
plt.grid()

# To plot magn response of hanning window
a=1
M=N-1
w2=0.5-0.5*np.cos(2*np.pi*n/M)    # denominator
plt.figure(2)
plt.subplot(1,2,1)
plt.stem(n,w2,use_line_collection=True)
plt.title('Hanning window')
plt.xlabel('Time index n--->')
w,H=signal.freqz(w2,a)
Hm=np.abs(H)   #magnitude omly
Hdb=20*np.log10(Hm)   # log magnitude
plt.subplot(1,2,2)
plt.plot(w/max(w),Hdb,color='red')
plt.title('magnitude response')
plt.xlabel('normalized freq w--->')
plt.ylabel('dB magnitude')
plt.grid()

# To plot magn response of hanning window
a=1
M=N-1
w3=0.54-0.46*np.cos(2*np.pi*n/M)    # denominator
plt.figure(3)
plt.subplot(1,2,1)
plt.stem(n,w3,use_line_collection=True)
plt.title('Hamming window')
plt.xlabel('Time index n--->')
w,H=signal.freqz(w3,a)
Hm=np.abs(H)   #magnitude omly
Hdb=20*np.log10(Hm)   # log magnitude
plt.subplot(1,2,2)
plt.plot(w/max(w),Hdb,color='red')
plt.title('magnitude response')
plt.xlabel('normalized freq w--->')
plt.ylabel('dB magnitude')
plt.grid()

# To plot magn response of hanning window
a=1
M=N-1
w4=0.42-0.5*np.cos(2*np.pi*n/M)+0.08*np.cos(4*np.pi*n/M)    # denominator
plt.figure(4)
plt.subplot(1,2,1)
plt.stem(n,w4,use_line_collection=True)
plt.title('Blackman window')
plt.xlabel('Time index n--->')
w,H=signal.freqz(w4,a)
Hm=np.abs(H)   #magnitude omly
Hdb=20*np.log10(Hm)   # log magnitude
plt.subplot(1,2,2)
plt.plot(w/max(w),Hdb,color='red')
plt.title('magnitude response')
plt.xlabel('normalized freq w--->')
plt.ylabel('dB magnitude')
plt.grid()

# To plot magn response of hanning window

n1=np.arange(0,M/2)
n2=np.arange(M/2,N)
w5=2*n1/M    # denominator
w6=2-2*n2/M
wb=np.concatenate([w5,w6])
plt.figure(5)
plt.subplot(1,2,1)
plt.stem(n,wb,use_line_collection=True)
plt.title('Bartlett window')
plt.xlabel('Time index n--->')
(w,H)=signal.freqz(wb,a)
Hm=np.abs(H)   #magnitude omly
Hdb=20*np.log10(Hm)   # log magnitude
plt.subplot(1,2,2)
plt.plot(w/max(w),Hdb,color='red')
plt.title('magnitude response')
plt.xlabel('normalized freq w--->')
plt.ylabel('dB magnitude')
plt.grid()