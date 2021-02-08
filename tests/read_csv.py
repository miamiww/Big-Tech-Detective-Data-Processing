import csv

with open('/home/blocker/Blocker_DB_Update/ip_ranges.csv') as csvfile:
    ip_ranges = csv.reader(csvfile)
    for ip in ip_ranges:
        print ip[0]
        print ip[1]