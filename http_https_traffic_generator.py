import urllib2
import sys
import time

n = sys.argv[1]

## The urls used below depends on a dns or some "name to ip" solution like edit /etc/hosts file on linux.

urls=['https://www.google.com', 'http://www.mercadolibre.com.ar', 'http://www.santanderrio.com', 'http://www.debian.org']

# create the request object using funtions to determine how many packets or curls are desired using:
# req = urllib2.Request(url)

def pcurl(n, urls):
 if n == 'i':
  while True:
   for url in urls:
    res = urllib2.urlopen(url)
    print res.read()
    time.sleep(0.1)
 else:
  while n > 0:
   for url in urls:
    res = urllib2.urlopen(url)
    print res.read()
    n = int(n)-1

# make the request and print the results

print  pcurl(n, urls)
