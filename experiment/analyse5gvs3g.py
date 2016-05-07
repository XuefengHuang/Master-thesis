import numpy as np
import matplotlib.pyplot as plt

filename = "experiment(4.19).txt"
data = open(filename, 'r')
dataset = data.readlines()
length = len(dataset)
thoughout1list_trans = list()
thoughout2list_trans = list()
retrylist2g = list()
retrylist5g= list()
otherlist2g = list()
otherlist5g = list()
singallist2g = list()
singallist5g = list()
utilizationlist2g = list()
utilizationlist5g = list()

for i in range(0,length-1):
  time = float(dataset[i+1].split(' ')[0]) - float(dataset[i].split(' ')[0])
  #time = float(dataset[i+1].split(' ')[0])
  thoughout1_trans = (float(dataset[i+1].split(' ')[1]) - float(dataset[i].split(' ')[1]))/time
  thoughout2_trans = (float(dataset[i+1].split(' ')[13]) - float(dataset[i].split(' ')[13]))/time
  utilization2g = (float(dataset[i+1].split(' ')[2]) - float(dataset[i].split(' ')[2]))/(time*10)
  utilization5g = (float(dataset[i+1].split(' ')[14]) - float(dataset[i].split(' ')[14]))/(time*10)
  external2g = ((float(dataset[i+1].split(' ')[2]) + float(dataset[i+1].split(' ')[4]) + float(dataset[i+1].split(' ')[6])) - (float(dataset[i].split(' ')[2]) + float(dataset[i].split(' ')[4]) + float(dataset[i].split(' ')[6])))/(time*10)
  external5g = ((float(dataset[i+1].split(' ')[14]) + float(dataset[i+1].split(' ')[16]) + float(dataset[i+1].split(' ')[18])) - (float(dataset[i].split(' ')[14]) + float(dataset[i].split(' ')[16]) + float(dataset[i].split(' ')[18])))/(time*10)
  retry2g = (float(dataset[i+1].split(' ')[8]) - float(dataset[i].split(' ')[8]))/time
  retry5g = (float(dataset[i+1].split(' ')[20]) - float(dataset[i].split(' ')[20]))/time
  singal2g = float(dataset[i+1].split(' ')[9])
  singal5g = float(dataset[i+1].split(' ')[21])

  thoughout1list_trans.append(thoughout1_trans)
  thoughout2list_trans.append(thoughout2_trans)
  otherlist2g.append(external2g)
  otherlist5g.append(external5g)
  retrylist2g.append(retry2g)
  retrylist5g.append(retry5g)
  singallist2g.append(singal2g)
  singallist5g.append(singal5g)
  utilizationlist2g.append(utilization2g)
  utilizationlist5g.append(utilization5g)


sorted_data_2g = np.sort(thoughout1list_trans)

yvals_2g = np.arange(len(sorted_data_2g))/float(len(sorted_data_2g))

plt.plot(sorted_data_2g, yvals_2g, label = '2.4 GHz')


sorted_data_5g = np.sort(thoughout2list_trans)

yvals_5g=np.arange(len(sorted_data_5g))/float(len(sorted_data_5g))

plt.plot(sorted_data_5g,yvals_5g, label = '5 GHz', lw=3)


plt.ylabel('Cumulative fraction of flows',fontsize=16)
plt.xlabel('Thoughout (bps)',fontsize=16)
plt.legend()
plt.show()