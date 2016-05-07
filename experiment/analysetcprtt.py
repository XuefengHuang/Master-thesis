import numpy as np

import matplotlib.pyplot as plt

data_2g = np.loadtxt('experiment(3.3)_rtt2g.txt')

sorted_data_2g = np.sort(data_2g)

yvals_2g=np.arange(len(sorted_data_2g))/float(len(sorted_data_2g))

plt.plot(sorted_data_2g,yvals_2g,color='red',label = '2.4 GHz')

data_5g = np.loadtxt('experiment(3.3)_rtt5g.txt')

sorted_data_5g = np.sort(data_5g)

yvals_5g=np.arange(len(sorted_data_5g))/float(len(sorted_data_5g))

plt.plot(sorted_data_5g,yvals_5g,color='blue',label = '5 GHz',lw=3)

plt.ylabel('Cumulative fraction of flows')
plt.xlabel('LAN TCP RTT (s)')

plt.legend()
plt.show()