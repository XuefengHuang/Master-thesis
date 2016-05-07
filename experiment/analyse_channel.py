import numpy as np
import matplotlib.pyplot as plt
import datetime

filename = "experiment2.29.txt"
data = open(filename, 'r')
dataset = data.readlines()
length = len(dataset)
thoughoutlist = list()
utilizationlist = list()
timelist = list()
transmit_timelist = list()
reveive_timelist = list()
thoughoutlist1 = list()

for i in range(0,length-1):
  time = float(dataset[i+1].split(' ')[0]) - float(dataset[i].split(' ')[0])
  thoughout = (float(dataset[i+1].split(' ')[1]) - float(dataset[i].split(' ')[1]))/time
  thoughout1 = (float(dataset[i+1].split(' ')[7]) - float(dataset[i].split(' ')[7]))/time
  busytime = (float(dataset[i+1].split(' ')[19]) - float(dataset[i].split(' ')[19]))/(time*10)
  activetime = (float(dataset[i+1].split(' ')[21]) - float(dataset[i].split(' ')[21]))/(time*10)
  transmit_time = (float(dataset[i+1].split(' ')[23]) - float(dataset[i].split(' ')[23]))/(time*10)
  reveive_time = (float(dataset[i+1].split(' ')[25]) - float(dataset[i].split(' ')[25]))/(time*10)
  utilization = busytime
  thoughoutlist.append(activetime)
  #thoughoutlist1.append(thoughout1)
  utilizationlist.append(utilization)
  transmit_timelist.append(transmit_time)
  reveive_timelist.append(reveive_time)
  #plt.ylabel('%')
  #plt.xlabel('busy time/total time')
#plt.title("Channel survey")
# sorted_data_2g = np.sort(thoughoutlist1)

# yvals_2g = np.arange(len(sorted_data_2g))/float(len(sorted_data_2g))

# plt.plot(sorted_data_2g, yvals_2g, label = '2.4 GHz')


# sorted_data_5g = np.sort(thoughoutlist)

# yvals_5g=np.arange(len(sorted_data_5g))/float(len(sorted_data_5g))

# plt.plot(sorted_data_5g,yvals_5g, label = '5 GHz')
#norm1 = [float(i)/sum(thoughoutlist) for i in thoughoutlist]
#norm2 = [float(i)/sum(thoughoutlist1) for i in thoughoutlist1]
#plt.plot(norm1, label = '5 GHz')
#plt.plot(norm2, label = '2.4 GHz')
plt.plot(thoughoutlist,color='blue',label = 'active time', linestyle = 'solid')
plt.plot(utilizationlist,color='green',label = 'busy time', linestyle = 'dashed')
plt.plot(reveive_timelist,color='purple',label = 'receive time', linestyle = 'dashdot')
plt.plot(transmit_timelist,color='yellow',label = 'transmit time', linestyle = 'dotted')
#plt.plot(utilizationlist)
plt.ylim(0,100)
plt.ylabel('%')
plt.xlabel('Times')
plt.legend()
plt.show()

