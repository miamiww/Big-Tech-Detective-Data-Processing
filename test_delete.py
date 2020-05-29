from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('ipdatabase')

# input for a uuid
id_value = input("Type UUID of record you wish to delete: ")
# deletes the value 
result = session.execute("DELETE FROM ipdatabase.ips WHERE id=%s" % (id_value))
print result
