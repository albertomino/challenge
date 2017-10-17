#!/bin/sh

echo 0 > /proc/sys/net/ipv4/ip_forward
sed -i s/net.ipv4.ip_forward=1/#net.ipv4.ip_forward=1/g /etc/sysctl.conf

iptables -F
iptables -t nat -F
#iptables -X
root@router:/scripts# cat disable_internet-access.sh
#!/bin/sh

iptables -t nat -D POSTROUTING -j MASQUERADE
root@router:/scripts# cat enable_internet-access.sh
#!/bin/sh

echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -t nat -A POSTROUTING -j MASQUERADE
