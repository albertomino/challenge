#!/usr/bin/python

import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

def traffic_by_protocol(file):
    allowed_protocols = {'80' : 0, '443': 0, '123' : 0, '53' : 0}
    for i in range(len(data)):
        if data[i]['Destination_port'] in allowed_protocols.keys():
            allowed_protocols[data[i]['Destination_port']] += int(data[i]['Packet_length'])
        else:
            pass
    return allowed_protocols


def port_to_name(allowed_protocols):
    known_protocols = {'80' : 'HTTP', '443' : 'HTTPS', '123' : 'NTP', '53' : 'DNS'}
    converted_dict = {}
    for i in allowed_protocols.keys():
        if i in known_protocols.keys():
            converted_dict[known_protocols[i]] = allowed_protocols[i]
        else:
            pass
    print converted_dict
    new_json_file = open('traffic_by_protocol.json', 'w')
    new_json_file.write(json.dumps(converted_dict))
    new_json_file.close()



port_to_name(traffic_by_protocol(data))
