from math import sqrt
import scipy.stats

def main():
  filename = "experiment(4.28).txt"
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

    utilization2g = (float(dataset[i+1].split(' ')[2]) - float(dataset[i].split(' ')[2]))/(time*10)

    external2g = ((float(dataset[i+1].split(' ')[2]) + float(dataset[i+1].split(' ')[6]) + float(dataset[i+1].split(' ')[8])) - (float(dataset[i].split(' ')[2]) + float(dataset[i].split(' ')[6]) + float(dataset[i].split(' ')[8])))/(time*10)

    retry2g = (float(dataset[i+1].split(' ')[10]) - float(dataset[i].split(' ')[10]))/time

    singal2g = float(dataset[i+1].split(' ')[11])


    thoughout1list_trans.append(thoughout1_trans)

    otherlist2g.append(external2g)

    retrylist2g.append(retry2g)

    singallist2g.append(singal2g)

    utilizationlist2g.append(utilization2g)


  print scipy.stats.pearsonr(thoughout1list_trans, utilizationlist2g)
  #print pearson(thoughout2list_trans, busytimelist_2g)
  print scipy.stats.pearsonr(thoughout1list_trans, singallist2g)
  #print pearson(thoughout2list_trans, signal_2g)
  print scipy.stats.pearsonr(thoughout1list_trans, retrylist2g)

  print scipy.stats.pearsonr(thoughout1list_trans, otherlist2g)

if __name__ == "__main__":
  main()