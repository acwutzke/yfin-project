import pandas

# This script compiles the

x ="Open"

data = pandas.read_csv("data5.csv")

ls=data[x].values.tolist()

plot1=[]

for r in range(30):
	plot1.append(sum(ls[r:(r+30)])/30)









		
