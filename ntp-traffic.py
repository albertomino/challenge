#!/usr/bin/python


import ntplib
import itertools
import sys
from time import ctime

ntplist = ['0.us.pool.ntp.org', '1.us.pool.ntp.org', '2.us.pool.ntp.org', '3.us.pool.ntp.org']

c = ntplib.NTPClient()

n = int(sys.argv[1])

for ntpserver in itertools.cycle(ntplist):
    try:
        response = c.request(ntpserver)
        print(ctime(response.tx_time))
    except Exception as e:
        pass
    n -= 1
    if n == 0:
        break
print 'Done!'
