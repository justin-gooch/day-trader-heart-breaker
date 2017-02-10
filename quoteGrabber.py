#create this as a function that will be used several times

#first thing you will need is a way to download files
# import urllib2
# response = urllib2.urlopen('http://www.example.com/')
# html = response.read()

#then you will need an api to grab it from
# http://wern-ancheta.com/blog/2015/04/05/getting-started-with-the-yahoo-finance-api/
# #essentially the api will look like 
# #http://finance.yahoo.com/d/quotes.csv?s=GOOG%f=abo
# keep in mind that the s = symbol (a.e. google) and that f = requested 
#data with a being ask, b being bid and o being open price
# they will come as "csv" data or comma separated values. 

#with the values we will need to store them somewhere for future use with a timestamp... luckily we have sqlite readily 
#available and can switch to mysql later on with ease

# https://docs.python.org/2/library/sqlite3.html will tell you all you need to know about the database
# my suggestion is to make the table with an id (for referencing elsewhere that auto increments), stock symbol name,
# stock current price and unix timestamp

import urllib2
import sqlite3
import datetime, time

symbol='ATVI'
info='abo'

today = datetime.date.today()

for i in symbol
	link=('http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s,symbol(i),info(i)')
	now = datetime.datetime.now()
	data(i) = 'today, now, urllib2.urlopen(link)'

conn = sqlite3.connect('Stocks.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, time text, symbol text, ask real, bid real, open real)''')

# Insert the data
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', data)

# Save (commit) the changes
conn.commit()
conn.close()