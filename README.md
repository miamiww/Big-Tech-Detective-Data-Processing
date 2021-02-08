# Data Processing for Big Tech Detective

asn_to_cidr_blocks is a simple bash script that takes a CSV of Company,ASNs pairs and converts it into a csv of Company,CIDR pairs.
So for example, `Amazon,AS1650` is expanded into:

```csv
Amazon,54.230.212.0/23
Amazon,54.230.214.0/23
Amazon,54.192.0.0/17
Amazon,54.192.0.0/18
Amazon,54.192.0.0/19
Amazon,54.192.0.0/20
Amazon,54.192.0.0/21
Amazon,54.192.0.0/23
Amazon,54.192.2.0/23
Amazon,54.192.4.0/23
... and so on
```

The outputted csv is then added to a table on the remote postgress server, accessible via the following api:
[https://bigtechdetective.club/ips](https://bigtechdetective.club/ips)
