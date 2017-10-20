#!/usr/bin/python

import requests
import sys

n = sys.argv[1]

urls=['http://www.google.com', 'http://www.mercadolibre.com.ar', 'http://www.santanderrio.com', 'http://www.debian.org', 'http://fernswa.myspecies.info', 'http://pngbirds.myspecies.info', 'http://nolinoideae.e-monocot.org', 'http://thymus.myspecies.info', 'http://chondrichthyes.myspecies.info', 'http://bormene.myspecies.info', 'http://dombeya.myspecies.info', 'http://aponogetonaceae.e-monocot.org', 'http://data.neomaps.org', 'http://aframomum.myspecies.info', 'http://itaxa.myspecies.info', 'http://crinoids.myspecies.info']


headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

for url in urls:
 r = requests.post(url, headers=headers)
 print r
