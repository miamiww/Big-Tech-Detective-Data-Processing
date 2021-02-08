import csv
from iptools import *
from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('ipdatabase')


def processor(ip_range):
    if '-' in ip_range:
        range = ip_range.split('-')
        b = range[0]
        t = range[1]
        return IpRange(b,t)
    else:
        return IpRange(ip_range)
        
def adder(company,ip_range):
    clean_range = processor(ip_range)
    print clean_range
    for ip in clean_range:
        cql_string = "insert into ipdatabase.ips(id,company,ipv4) VALUES(uuid(),'%s','%s')" % (company,ip)
        print cql_string
        result = session.execute(cql_string)
        print result



with open('ip_ranges.csv') as csvfile:
    ip_ranges = csv.reader(csvfile)
    for ip in ip_ranges:
        adder(ip[0],ip[1])
        