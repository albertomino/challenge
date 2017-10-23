#!/bin/sh

echo 1 > /proc/sys/net/ipv4/ip_forward
sed -i s/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g /etc/sysctl.conf

iptables -F
iptables -t nat -F
iptables -X


iptables -t nat -A PREROUTING -p tcp --dport 2220 -j DNAT --to-destination 192.168.1.140:22
iptables -t nat -A PREROUTING -p tcp --dport 2240 -j DNAT --to-destination 192.168.1.150:22
iptables -t nat -A POSTROUTING -p tcp -d 192.168.1.140 --dport 22 -j SNAT --to-source 192.168.1.10
iptables -t nat -A POSTROUTING -p tcp -d 192.168.1.150 --dport 22 -j SNAT --to-source 192.168.1.10

