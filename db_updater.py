from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('ipdatabase')

company_names = ['Amazon','Google','Microsoft','Facebook','Apple']

company_name = 'Amazon'
# print company_name
ip_address = '13.226.27.72'

# to put data in the database
# result = session.execute("insert into ipdatabase.ips(id,company,ipv4) VALUES(uuid(),{},{})".format(company_name,ip_address))
# cql_string = "insert into ipdatabase.ips(id,company,ipv4) VALUES(uuid(),%s,%s)" % (company_name,ip_address)
cql_string = "insert into ipdatabase.ips(id,company,ipv4) VALUES(uuid(),"+str(company_name)+","+str(ip_address)+")"
print cql_string
result = session.execute(cql_string)
# result = session.execute("insert into ipdatabase.ips(id,company,ipv4) VALUES(uuid(),'Amazon','13.226.27.72')")

print result
