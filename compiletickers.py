import pandas

#This file takes the tickers from
tickerdata = pandas.read_csv("TSX-Tickers.csv")
tickerlist=tickerdata["Symbol"].astype(str).values.tolist()
tickerstring=""
for ticker in tickerlist:
	tickerstring+=ticker+" "

