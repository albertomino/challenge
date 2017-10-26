#!/usr/bin/python

import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

def top_sites(file):
    sites = {}
    for i in range(len(data)):
        try:
            if data[i]['HTTP_Host'] not in sites.keys():
                sites[data[i]['HTTP_Host']] = 1
            else:
                sites[data[i]['HTTP_Host']] += 1
        except Exception as e:
            pass
    new_json_file = open('top_sites.json', 'w')
    new_json_file.write(json.dumps(sites))
    new_json_file.close()


top_sites(data)
