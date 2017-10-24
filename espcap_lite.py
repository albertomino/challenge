#!/usr/bin/env python

import sys
import click
import pyshark
import json
import time

def list_interfaces():
    proc = os.popen("tshark -D")  # Note tshark must be in $PATH
    tshark_out = proc.read()
    interfaces = tshark_out.splitlines()
    for i in range(len(interfaces)):
        interface = interfaces[i].strip(str(i+1)+".")
        print interface

def get_ip_version(packet):
    for layer in packet.layers:
        if layer._layer_name == 'ip':
            return 4
        elif layer._layer_name == 'ipv6':
            return 6


def dump_packets(capture):
    i = 1
    for packet in capture:
        if packet.transport_layer == 'UDP':
            ip = None
            ip_version = get_ip_version(packet)
            if ip_version == 4:
                ip = packet.ip
            elif ip_version == 6:
                ip = packet.ipv6
            print 'Packet %d' % i
            print 'Packet length    -', packet.length
            print 'sniff_time       -', packet.sniff_time
            print 'sniff_timestamp  -', packet.sniff_timestamp
            print 'Source IP        -', ip.src
            print 'Source port      -', packet.udp.srcport
            print 'Destination IP   -', ip.dst
            print 'Destination port -', packet.udp.dstport
            print '\n'
        if packet.transport_layer == 'TCP':
            ip = None
            ip_version = get_ip_version(packet)
            if ip_version == 4:
                ip = packet.ip
            elif ip_version == 6:
                ip = packet.ipv6
            try:
                print 'Packet %d' % i
                print 'Packet length    -', packet.length
                print 'sniff_time       -', packet.sniff_time
                print 'sniff_timestamp  -', packet.sniff_timestamp
                print 'Source IP        -', ip.src
                print 'Source port      -', packet.tcp.srcport
                print 'Destination IP   -', ip.dst
                print 'Destination port -', packet.tcp.dstport
                print 'http host        -', packet.http.host
                print '\n'
            except Exception as e:
                print e
                pass
        i += 1

def dump_packets_to_dict(capture):
    counter = 0
    timestr = time.strftime("%H%M%S-%d%m%Y")
    capture_file = open(timestr, 'w')
    packets_list = []
    i = 1
    for packet in capture.sniff_continuously(packet_count=2500):
        if packet.transport_layer == 'UDP':
            ip = None
            ip_version = get_ip_version(packet)
            if ip_version == 4:
                ip = packet.ip
            elif ip_version == 6:
                ip = packet.ipv6
            packets_list.append({'Packet' : i, 'Packet_length' : packet.length, 'sniff_time' : str(packet.sniff_time), 'sniff_timestamp' : packet.sniff_timestamp, 'Source_IP' : ip.src, 'Source_Port' : packet.udp.srcport, 'Destination_IP' : ip.dst, 'Destination_port' : packet.udp.dstport})
        if packet.transport_layer == 'TCP':
            ip = None
            ip_version = get_ip_version(packet)
            if ip_version == 4:
                ip = packet.ip
            elif ip_version == 6:
                ip = packet.ipv6
            try:
                packets_list.append({'Packet' : i, 'Packet_length' : packet.length, 'sniff_time' : str(packet.sniff_time), 'sniff_timestamp' : packet.sniff_timestamp, 'Source_IP' : ip.src, 'Source_Port' : packet.tcp.srcport, 'Destination_IP' : ip.dst, 'Destination_port' : packet.tcp.dstport, 'HTTP_Host' : packet.http.host})
            except Exception as e:
                packets_list.append({'Packet' : i, 'Packet_length' : packet.length, 'sniff_time' : str(packet.sniff_time), 'sniff_timestamp' : packet.sniff_timestamp, 'Source_IP' : ip.src, 'Source_Port' : packet.tcp.srcport, 'Destination_IP' : ip.dst, 'Destination_port' : packet.tcp.dstport})
        i += 1
        counter += 1
    packets_list = json.dumps(packets_list, indent=4, sort_keys=True)
    capture_file.write(packets_list)
    capture_file.close()
    print '%s were captured!' % counter


@click.command()
@click.option('--dump', is_flag=False, help='Network interface for live capture using json output to a file (default=False)')
@click.option('--nic', default=None, help='Network interface for live capture (default=None, if file specified)')
@click.option('--file', default=None, help='PCAP file for file capture (default=None, if nic specified)')
@click.option('--list', is_flag=True, help='List the network interfaces')
def main(nic, file, list, dump):
    if list:
        list_interfaces()
        sys.exit(0)
    elif nic == None and file == None:
        print 'You must specify either a network interface or packet capture file'
        sys.exit(1)

    capture = None
    if nic == None:
        capture = pyshark.FileCapture(file)
    elif dump == 'True':
        capture = pyshark.LiveCapture(nic, bpf_filter='not tcp port 22 and not tcp port 2220 and not tcp port 2240 and not host 192.168.1.10')
        dump_packets_to_dict(capture)
    elif file == None:
        capture = pyshark.LiveCapture(nic, output_file='captura.pcap', bpf_filter='not tcp port 22 and not tcp port 2220 and not tcp port 2240')
        dump_packets(capture)



if __name__ == '__main__':
    main()
