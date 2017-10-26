#!/usr/bin/python

import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

def clients_vs_sites(file):
    links = []
    for i in range(len(data)):
        if 'HTTP_Host' in data[i]:
            pprint('adding to links %s' % data[i]['HTTP_Host'])
            links.append({'source': "%s" % data[i]['Source_IP'], 'target': "%s" % data[i]['HTTP_Host'], 'type': "licensing"})
        else:
            pass
    new_json_file = open('clients_vs_sites.json', 'w')
    new_json_file.write(json.dumps(links))
    new_json_file.close()


clients_vs_sites(data)
