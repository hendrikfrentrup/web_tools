textarea="00:21:1             124             8.0 \n\
00:40:6             130             8.0 \n\
00:59:0             132             8.0 \n\
01:26:1             132             8.5 \n\
01:34:9             136             8.5 \n\
01:43:6             138             8.5 \n\
02:24:7             140             9 \n\
02:32:7             143             9 \n\
02:46:5             146             9 \n\
02:55:5             143             9 \n\
03:00:6             144             9.5 \n\
03:03:6             141             9.5 \n\
03:07:3             146             9.5 \n\
03:27:7             146             9.5 \n\
03:40:5             152             10 \n\
03:46:6             150             10 \n\
03:58:1             149             10.5 \n\
04:12:5             153             10.5 \n\
04:21:2             157             10.5 \n\
04:32:8             156             11 \n\
04:41:3             160             11 \n\
04:46:1             159             11 \n\
04:50:2             163             11 \n\
05:09:5             166             11 \n\
05:20:5             168             11.5 \n\
05:26:6             165             11.5 \n\
05:32:4             171             11.5 \n\
05:45:0             170             11.5 \n\
06:04:3             173             11.5 \n\
06:15:0             172             12 \n\
06:37:4             176             12 \n\
06:47:9             178             12"

import pdb

import matplotlib    
import matplotlib.pyplot as pl
import matplotlib.dates as md
import numpy as np

import coconiTest as ct

sampleTest = ct.coconiTest()
sampleTest.setHTMLstring(textarea)
sampleTest.parseSelf()

#time, bpm, speed = coconiTest.parseExtString(textarea)

secs=[]
for t in sampleTest.time:
    secs.append(t.tm_min*60+t.tm_sec)

#times = matplotlib.dates.date2num(time)
#pl.plot_date(secs, bpm)

#start=0.0
#for i,s in enumerate(secs[0:10]):      
#    pl.bar(start,speed[i],s)
#    start=secs[i-1]

fig=pl.figure('bpm')
pl.subplot(211)
pl.plot(secs,sampleTest.bpm,'bo-')
pl.subplot(212)
pl.plot(secs,sampleTest.speed,'ro')
pl.show()

#ax=fig.gca()
#xfmt = md.DateFormatter('%M:%S')
#ax.xaxis.set_major_formatter(xfmt)
#pl.plot(time,bpm, "o-")
#pl.show()


