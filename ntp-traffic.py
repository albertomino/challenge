#!/usr/bin/python


import ntplib
from time import ctime

ntplist = ['0.us.pool.ntp.org', '1.us.pool.ntp.org', '2.us.pool.ntp.org', '3.us.pool.ntp.org']

c = ntplib.NTPClient()

for ntpserver in ntplist:
    try:
        response = c.request(ntpserver)
        print(ctime(response.tx_time))
    except Exception as e:
        pass
print 'Done!'
