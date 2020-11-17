
import yfinance as yf
import datetime
import pandas


# Gets last friday or current date if date is friday
# then it gets 210 days before last friday
# purpose is to frame the date range and calculate EMA
ct = datetime.datetime.today()
for x in range (0,7):
	d = ct - datetime.timedelta(days=x)
	if d.weekday() == 4:
		tgif=d
		stgif=d-datetime.timedelta(days=210)
lfriday=tgif.strftime("%Y-%m-%d")
sfriday=stgif.strftime("%Y-%m-%d")
ctstr=ct.strftime("%Y-%m-%d-%H-%M-%S")

#This file takes the tickers from
tickerdata = pandas.read_csv("TSX-Tickers.csv")
tickerlist=tickerdata["Symbol"].astype(str).values.tolist()
tickerstring=""
for ticker in tickerlist:
	tickerstring+=ticker+".TO"+" "

# Use yfinance to download stock data based on tickerstring and date range calculated above
# Print date range boudaries and save to csv with file name 
data = yf.download(tickers= "CNQ.TO BCE.TO", start=sfriday, end=lfriday,interval="1d")
print(sfriday)
print(lfriday)

data.to_csv(ctstr+".csv")


