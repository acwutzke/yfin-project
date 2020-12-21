import datetime
import pandas

fl = input("Name of csv file:")

data = pandas.read_csv(fl + ".csv")


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
		






		



