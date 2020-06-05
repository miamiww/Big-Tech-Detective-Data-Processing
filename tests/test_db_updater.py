from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('ipdatabase')

company_names = ['Amazon','Google','Microsoft','Facebook','Apple']

company_name = 'Amazon'
# print company_name
ip_address = '13.226.27.72'

# to put data in the database
cql_string = "insert into ipdatabase.ips(id,company,ipv4) VALUES(uuid(),'%s','%s')" % (company_name,ip_address)
result = session.execute(cql_string)

print result
