import yfinance as yf
from datetime import datetime
from datetime import timedelta
import time, sys, os
def p(msg):
    for i in msg:
        sys.stdout.flush()
        sys.stdout.write(i)
        time.sleep(0.0005)
    print()

def stock(stockName):
    try:
        ticker = yf.Ticker(stockName).info
    except:
        p('unknown stock ticker name')
        return None
    try:
        p(ticker['symbol'] + ".currentPrice: " + str(ticker['currentPrice']))
        p(ticker['symbol'] + ".open: " + str(ticker['open']))
        p(ticker['symbol'] + ".dayLow: " + str(ticker['dayLow']))
        p(ticker['symbol'] + ".dayHigh: " + str(ticker['dayHigh']))
        p(ticker['symbol'] + ".regularMarketPreviousClose: " + str(ticker['regularMarketPreviousClose']))
        p(ticker['symbol'] + ".regularMarketOpen: " + str(ticker['regularMarketOpen']))
        p(ticker['symbol'] + ".regularMarketDayLow: " + str(ticker['regularMarketDayLow']))
        p(ticker['symbol'] + ".regularMarketDayHigh: " + str(ticker['regularMarketDayHigh']))
        p(ticker['symbol'] + ".targetHighPrice: " + str(ticker['targetHighPrice']))
        p(ticker['symbol'] + ".targetLowPrice: " + str(ticker['targetLowPrice']))
        p(ticker['symbol'] + ".targetMeanPrice: " + str(ticker['targetMeanPrice']))
        p(ticker['symbol'] + ".targetMedianPrice: " + str(ticker['targetMedianPrice']))
        p(ticker['symbol'] + ".fiftyTwoWeekLow: " + str(ticker['fiftyTwoWeekLow']))
        p(ticker['symbol'] + ".fiftyTwoWeekHigh: " + str(ticker['fiftyTwoWeekHigh']))
        p(ticker['symbol'] + ".fiftyDayAverage: " + str(ticker['fiftyDayAverage']))
        p(ticker['symbol'] + ".twoHundredDayAverage: " + str(ticker['twoHundredDayAverage']))
        p(ticker['symbol'] + ".marketCap: " + str(ticker['marketCap']))
    except:
        p("Could not get all information for stock " + stockName)

def previousWeek(stockName):
    try:
        ticker = yf.Ticker(stockName)
    except:
        p('unknown stock ticker name')
        return None
    b = ticker.history(period="7d")
    p(str(b))

def previousMonth(stockName):
    try:
        ticker = yf.Ticker(stockName)
    except:
        p('unknown stock ticker name')
        return None
    b = ticker.history(period="1mo")
    p(str(b))

def previousDay(stockName):
    try:
        ticker = yf.Ticker(stockName)
    except:
        p('unknown stock ticker name')
        return None
    b = ticker.history(period="1day")
    p(str(b))

def getAbbv():
    p('GOOGL - google')
    p('MSFT - microsoft')
    p('INTC - intel')
    p('TSLA - tesla')
    p('AAPL - apple')
    p('AMZN - amazon')
    p('META - meta')
    p('V - visa')
    p('JPM - JP Morgan')
    p('NVDA - NVDIA')
    p('COST - costco')
    p('DIS - Disney')
    
while True: #loop
    cmd = input('> ').lower()
    cmdsplit = cmd.split(" ")
    if cmdsplit[0] == "stock" or cmdsplit[0] == "get" or cmdsplit[0] == "stockinfo":
        try:
            a = cmdsplit[1]
            try:
                a = cmdsplit[2]
                if cmdsplit[2] == "--getweek" or cmdsplit[2] == "--previousweek" or cmdsplit[2] == "--week" or cmdsplit[2] == "--lastweek":
                    previousWeek(cmdsplit[1])
                elif cmdsplit[2] == "--getmonth" or cmdsplit[2] == "--previousmonth" or cmdsplit[2] == "--month" or cmdsplit[2] == "--lastmonth":
                    previousMonth(cmdsplit[1])
                elif cmdsplit[2] == "--getday" or cmdsplit[2] == "--previousday" or cmdsplit[2] == "--day" or cmdsplit[2] == "--lastday":
                    previousDay(cmdsplit[1])
                else:
                    p('Unknown command: ' + str(cmd[2]))
            except IndexError:
                stock(cmdsplit[1])
        except IndexError:
            p('Please enter a stockname; type "stocks" to get a list of popular stock names')
    elif cmdsplit[0] == "names" or cmdsplit[0] == "stocks" or cmdsplit[0] == "abbr":
        getAbbv()
    elif cmdsplit[0] == "exit":
        sys.exit(1)
    elif cmdsplit[0] == "cls" or cmdsplit == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmdsplit[0] == "help":
        p('stock|get|stockinfo <stockname> [getpreviousinfo:week|month|day]         get stock info about a specific stock      stockname is required, getprevious info is optional')
        p('names|stocks|abbr                                                    shows list of popular stocks')
        p('cls|clear                                                            clear terminal')
        p('exit                                                                 exits')
    else:
        p('not a command (use "help" to list commands)')