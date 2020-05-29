from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('ipdatabase')

company_names = ["Amazon","Google","Microsoft","Facebook","Apple"]

company_name = company_names[0]
ip_address = "99.84.115.72"

# to put data in the database
result = session.execute("insert into ipdatabase.ips(id,company,ipv4) VALUES(uuid(),{},{})".format(company_name,ip_address))
print result
