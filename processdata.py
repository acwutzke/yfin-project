import datetime
import pandas

data = pandas.read_csv("2020-11-13-15-36-03.csv")


col=data.columns.tolist()

emadict={}
lsfloat=[]

i=0
for c in col:
	if c[:9]=="Adj Close":
		ls=data[c].values.tolist()
		for item in ls[2::5]:
			lsfloat.append(float(item))
		ema=[sum(lsfloat)/len(lsfloat)]
		emadict[ls[0]]=ema

print(emadict)
		






		



