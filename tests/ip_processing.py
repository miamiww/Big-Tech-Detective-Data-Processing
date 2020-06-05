from iptools import *

in_range = '169.255.24.192-169.255.24.255'
# in_range = '192.168.0.0/24'   

def processor(ip_range):
    if '-' in ip_range:
        range = ip_range.split('-')
        b = range[0]
        t = range[1]
        return IpRange(b,t)
    else:
        return IpRange(ip_range)
        
def expander(ip_range):
    clean_range = processor(ip_range)
    print clean_range
    for ip in clean_range:
        print ip     


expander(in_range)