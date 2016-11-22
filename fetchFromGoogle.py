# Hacking Google Finance in Real-Time for Algorithmic Traders
#
# (c) 2014 QuantAtRisk.com, by Pawel Lachowicz
# http://www.quantatrisk.com/2014/01/14/hacking-google-finance-in-real-time-for-algorithmic-traders/

import urllib, time, os, re, csv

def fetchGF(googleticker):
    url="http://www.google.com/finance?&q="
    txt=urllib.urlopen(url+googleticker).read()
    k=re.search('id="ref_(.*?)">(.*?)<',txt)
    if k:
        tmp=k.group(2)
        q=tmp.replace(',','')
    else:
        q="Nothing found for: "+googleticker
    return q

# display time corresponding to your location
print(time.ctime())
print

# Set local time zone to NYC
os.environ['TZ']='America/New_York'
time.tzset()
t=time.localtime() # string
print(time.ctime())
print

def combine(ticker):
    quote=fetchGF(ticker) # use the core-engine function
    t=time.localtime()    # grasp the moment of time
    output=[t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,  # build a list
            t.tm_min,t.tm_sec,ticker,quote]
    return output

tickers=["NASDAQ:AAPL","NASDAQ:GOOG","NASDAQ:BIDU","NYSE:IBM", \
         "NASDAQ:INTC","NASDAQ:MSFT","NYSEARCA:SPY"]

# define the name of an output file
fname="portfolio.dat"
# remove a file, if exist
os.path.exists(fname) and os.remove(fname)

freq=600 # fetch data every 600 sec (10 min)

with open(fname,'a') as f:
    writer=csv.writer(f,dialect="excel") #,delimiter=" ")
    while(t.tm_hour<=16):
        if(t.tm_hour==16):
            while(t.tm_min<01):
                #for ticker in tickers:
                data=combine(ticker)
                print(data)
                writer.writerow(data)
                time.sleep(freq)
            else:
                break
        else:
            for ticker in tickers:
                data=combine(ticker)
                print(data)
                writer.writerow(data)
            time.sleep(freq)

f.close()
