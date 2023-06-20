J='clear'
I='cls'
H=IndexError
F='unknown stock ticker name'
C=str
import yfinance as E
from datetime import datetime,timedelta
import time,sys as D,os
def A(msg):
	for A in msg:
		D.stdout.flush();D.stdout.write(A)
		if A==' ':continue
		else:time.sleep(1e-12)
	print()
def K(stockName):
	G=stockName;D='symbol'
	try:B=E.Ticker(G).info
	except:A(F);return
	try:A(B[D]+'.currentPrice: '+C(B['currentPrice']));A(B[D]+'.open: '+C(B['open']));A(B[D]+'.dayLow: '+C(B['dayLow']));A(B[D]+'.dayHigh: '+C(B['dayHigh']));A(B[D]+'.regularMarketPreviousClose: '+C(B['regularMarketPreviousClose']));A(B[D]+'.regularMarketOpen: '+C(B['regularMarketOpen']));A(B[D]+'.regularMarketDayLow: '+C(B['regularMarketDayLow']));A(B[D]+'.regularMarketDayHigh: '+C(B['regularMarketDayHigh']));A(B[D]+'.targetHighPrice: '+C(B['targetHighPrice']));A(B[D]+'.targetLowPrice: '+C(B['targetLowPrice']));A(B[D]+'.targetMeanPrice: '+C(B['targetMeanPrice']));A(B[D]+'.targetMedianPrice: '+C(B['targetMedianPrice']));A(B[D]+'.fiftyTwoWeekLow: '+C(B['fiftyTwoWeekLow']));A(B[D]+'.fiftyTwoWeekHigh: '+C(B['fiftyTwoWeekHigh']));A(B[D]+'.fiftyDayAverage: '+C(B['fiftyDayAverage']));A(B[D]+'.twoHundredDayAverage: '+C(B['twoHundredDayAverage']));A(B[D]+'.marketCap: '+C(B['marketCap']))
	except:A('Could not get all information for stock '+G)
def L(stockName):
	try:B=E.Ticker(stockName)
	except:A(F);return
	D=B.history(period='7d');A(C(D))
def M(stockName):
	try:B=E.Ticker(stockName)
	except:A(F);return
	D=B.history(period='1mo');A(C(D))
def N(stockName):
	try:B=E.Ticker(stockName)
	except:A(F);return
	D=B.history(period='1day');A(C(D))
def O(stockName):
	try:B=E.Ticker(stockName)
	except:A(F);return
	D=B.history(period='1y');A(C(D))
def P():A('Examples: ');A('GOOGL - google');A('MSFT - microsoft');A('INTC - intel');A('TSLA - tesla');A('AAPL - apple');A('AMZN - amazon');A('META - meta');A('V - visa');A('JPM - JP Morgan');A('NVDA - NVDIA');A('COST - costco');A('DIS - Disney')
def help():A('stock|get|stockinfo <stockname> [getpreviousinfo:week|month|day]     get stock info about a specific stock');A('stockname is required, getprevious info is optional');A('names|stocks|abbr                                                    shows list of popular stocks');A('cls|clear                                                            clear terminal');A('exit                                                                 exits')
help()
while True:
	G=input('> ').lower();B=G.split(' ')
	if B[0]=='stock'or B[0]=='get'or B[0]=='stockinfo':
		try:
			Q=B[1]
			try:
				Q=B[2]
				if B[2]=='--getweek'or B[2]=='--previousweek'or B[2]=='--week'or B[2]=='--lastweek':L(B[1])
				elif B[2]=='--getmonth'or B[2]=='--previousmonth'or B[2]=='--month'or B[2]=='--lastmonth':M(B[1])
				elif B[2]=='--getday'or B[2]=='--previousday'or B[2]=='--day'or B[2]=='--lastday':N(B[1])
				elif B[2]=='--getyear'or B[2]=='--previousyear'or B[2]=='--year'or B[2]=='--lastyear':O(B[1])
				else:A('Unknown command: '+C(G[2]))
			except H:K(B[1])
		except H:A('Please enter a stockname; type "stocks" to get a list of popular stock names')
	elif B[0]=='names'or B[0]=='stocks'or B[0]=='abbr':P()
	elif B[0]=='exit':D.exit(1)
	elif B[0]==I or B==J:os.system(I if os.name=='nt'else J)
	elif B[0]=='help':help()
	else:A('not a command (use "help" to list commands)')