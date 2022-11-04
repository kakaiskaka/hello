#Q7 Window chartersists

#To study characteristics of window function in time and frequency domain
# Import packages and modules
import numpy as np
from matplotlib import pyplot as plt

  # Define window parameters
N=51   #length of window function
n=np.arange(N)   # n---->0 to N-1
M=N-1
# Define rectangular window and plot
w1=np.ones(N) 
print("\n coefficient of rectangular window:" , w1 )
plt.figure(1)
plt.stem(n,w1,use_line_collection=True,linefmt='red')
plt.title("rectangular window")
plt.xlabel("time index n--->")
plt.ylabel("amplitude")
plt.show()

#Define Hanning window and plot
w2=0.5-0.5*np.cos(2*np.pi*n/M)
print("\n coefficient of hanning window:" , w2)
plt.figure(2)
plt.stem(n,w2,use_line_collection=True,linefmt='red')
plt.title("Hanning window")
plt.xlabel("time index n--->")
plt.ylabel("amplitude")
plt.show()

# Define Hammimg window and plot
w3=0.54-0.46*np.cos(2*np.pi*n/M)
print("\n coefficient of Hammimg window" , w3)
plt.figure(3)
plt.stem(n,w3,use_line_collection=True,linefmt='red')
plt.title("Hammimg window")
plt.xlabel("time index n--->")
plt.ylabel("amplitude")
plt.show()

#Define Blackman window and plot
w4=0.42-0.5*np.cos(2*np.pi*n/M)+0.08*np.cos(4*np.pi*n/M)
print("\n coefficient of Blackman window" , w4)
plt.figure(4)
plt.stem(n,w4,use_line_collection=True,linefmt='red')
plt.title("Blackman window")
plt.xlabel("time index n--->")
plt.ylabel("amplitude")
plt.show()

#Define Bartlett window and plot
n1=np.arange(0,M/2)
n2=np.arange(M/2,N)
wb1=2*n1/M
wb2=2-2*n2/M
wb=np.concatenate([wb1,wb2])
print("\n coefficient of Bartlett window" , wb)
plt.figure(5)
plt.stem(n,wb,use_line_collection=True,linefmt='red')
plt.title("Bartlett window")
plt.xlabel("time index n--->")
plt.ylabel("amplitude")
plt.show()