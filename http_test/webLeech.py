#!/usr/bin/env python
import urllib2
import sys

import httplib

https://amers1.mobile13.cp.reutest.com/msf1.0/data/MarketData?$filter=Request/Tickers+eq+%27EUR=%27

thisurl = sys.argv[1]

conn = httplib.HTTPConnection(thisurl)
conn.request("GET", "/index.html")
# for MFS
# url_query =urllib2.quote(filter=Request/Filter"TRI.TO")
# conn.request("GET", "/?"+ url_query )
r1 = conn.getresponse()
print r1.status, r1.reason


if r1.status==200:
   print "Yay, this worked....check temp.html!"
   print "and reads as follows:"
   print r1.read()



response = urllib2.urlopen('http://'+thisurl)
html=response.read()

outfile = open('temp.html', 'w')
outfile.write(html)
outfile.close()
#print html
