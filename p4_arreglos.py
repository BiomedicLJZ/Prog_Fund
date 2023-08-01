import numpy as np
import matplotlib.pyplot as plt
import math as m

T=1
fs=1000
F=15
t=np.linspace(0,T,fs)
s=np.sin(2*np.pi*F*t)

plt.plot(t,s)