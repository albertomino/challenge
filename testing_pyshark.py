#!/usr/bin/python
## Captura utilizando pyshark
import pyshark


def capture():

 capture_file = open('/scripts/captura.pcap', 'w')

 capture = pyshark.LiveCapture(interface='eth1')

 for packet in capture.sniff_continuously(packet_count=500):
  capture_file.write(str(packet))

 capture_file.close()
 return  "Se capturaron 500 paquetes!"


def capture_http_filter():

    capture_file = open('/scripts/captura_http.pcap', 'w')

    capture = pyshark.LiveCapture(interface='eth1', display_filter='http')

    for packet in capture.sniff_continuously(packet_count=500):
        capture_file.write(str(packet))

    capture_file.close()
    return "Se capturaron 500 paquetes!"


def capture_ssl_filter():

    capture_file = open('/scripts/captura_ssl.pcap', 'w')

    capture = pyshark.LiveCapture(interface='eth1', display_filter='ssl')

    for packet in capture.sniff_continuously(packet_count=500):
        capture_file.write(str(packet))

    capture_file.close()
    return "Se capturaron 500 paquetes!"

print capture_http_filter()
