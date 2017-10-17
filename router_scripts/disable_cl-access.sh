#!/bin/sh

echo 0 > /proc/sys/net/ipv4/ip_forward
sed -i s/net.ipv4.ip_forward=1/#net.ipv4.ip_forward=1/g /etc/sysctl.conf

iptables -F
iptables -t nat -F
#iptables -X
