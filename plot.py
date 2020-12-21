import yfinance as yf
import datetime
import pandas
import matplotlib.pyplot as plt 

fl = input("Name of csv file: ")

data = pandas.read_csv(fl + ".csv")

col=data.columns.tolist()

emadict={}
emals=[]
lsfloat=[]
lsdata=[]


for c in col:
	if c[:9]=="Adj Close":
		ls=data[c].values.tolist()
		for item in ls[2::5]:
			lsfloat.append(float(item))
		emadict[ls[0]]=[]
		emadict[ls[0]].append(lsfloat)
		lsfloat=[]
		lsdata=[]

for c in col:
	if c[:6]=="Volume":
		ls=data[c].values.tolist()
		for item in ls[2::5]:
			lsfloat.append(float(item))
		emadict[ls[0]].append(lsfloat)
		lsfloat=[]
		lsdata=[]

datels = data['Unnamed: 0'].values.tolist()
emadict['Date']=datels[2::5]

plt.plot(emadict['BCE.TO'][0])
plt.show()

# print(emadict)
# print(emadict)