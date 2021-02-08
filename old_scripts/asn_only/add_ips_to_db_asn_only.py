import csv
from iptools import *
from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('ipdatabase')
        
def adder(company,ip_range):
    cql_string = "insert into ipdatabase.ipblocks(id,Company,CIDR) VALUES(uuid(),'%s','%s')" % (company,ip_range)
    print cql_string
    result = session.execute(cql_string)
    print result



with open('asn_only_ip_ranges.csv') as csvfile:
    ip_ranges = csv.reader(csvfile)
    for ip in ip_ranges:
        adder(ip[0],ip[1])
        



