from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('ipdatabase')

# to test just print the database
result = session.execute("select * from ipdatabase.ipblocks")[0]
print result
