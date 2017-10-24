import urllib2
import sys
import time
import itertools

n = int(sys.argv[1])

## The urls used below depends on a dns or some "name to ip" solution like edit /etc/hosts file on linux.

urls=['https://www.google.com', 'http://www.mercadolibre.com.ar', 'http://www.santanderrio.com', 'http://www.debian.org', 'http://fernswa.myspecies.info', 'http://pngbirds.myspecies.info', 'http://nolinoideae.e-monocot.org', 'http://thymus.myspecies.info', 'http://chondrichthyes.myspecies.info', 'http://bormene.myspecies.info', 'http://pleistocenekokemushi.myspecies.in', 'http://dombeya.myspecies.info', 'http://aponogetonaceae.e-monocot.org', 'http://data.neomaps.org', 'http://aframomum.myspecies.info', 'http://itaxa.myspecies.info', 'http://crinoids.myspecies.info']


# create the request object using funtions to determine how many packets or curls are desired using:
# req = urllib2.Request(url)

def pcurl(n, urls):
 if n == 'i':
  while True:
   for url in urls:
    res = urllib2.urlopen(url)
    print res.read()
    time.sleep(0.5)
 else:
   for url in itertools.cycle(urls):
    try:
     res = urllib2.urlopen(url)
     print 'curling %s' % url
     print res.read()
     time.sleep(0.5)
     n = int(n)-1
     if n == 0:
      break
    except Exception as e:
        pass
   print 'Done!'



# make the request and print the results

print  pcurl(n, urls)
