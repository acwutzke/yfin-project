import datetime

ct = datetime.datetime.today()

for x in range (0,7):
	d = ct - datetime.timedelta(days=x)
	if d.weekday() == 4:
		tgif=d

lfriday=tgif.strftime("%Y-%m-%d")

		
print(lfriday)