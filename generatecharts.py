from linefunction import line_func
import numpy as np 
import matplotlib.pyplot as plt 

#generate array with stock data
datatext=np.genfromtxt('2020-12-21-13-24-10.csv',delimiter=',',dtype=None,encoding=None)
data=np.genfromtxt('2020-12-21-13-24-10.csv',delimiter=',')

n=len(data[:,3])
i=len(data[:,3])-120
e=len(data[:,3])-5

#generate resistanc line for the past 3 months
prices=data[(n-120):,3]
resist_list=data[i:e,3]
print(resist_list)
resist=line_func(resist_list.tolist())
#print(resist)

#plot chart
# plotting the line 1 points 
plt.plot(range(len(prices)), prices, label = "Price")

# plotting the line 2 points 
plt.plot(range(len(resist)), resist, label = "Resistance line")
plt.show()











		



