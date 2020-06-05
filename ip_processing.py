from iptools import *

ip_range = '169.255.24.192 - 169.255.24.255'

def processor(ip_range):
    if '-' in ip_range:
        ip_range.split(' - ')
        

print len(IpRangeList(ip_range))

for ip in IpRangeList(ip_range):
    print ip