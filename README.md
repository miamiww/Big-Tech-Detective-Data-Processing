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

The outputted csv is then added to a table on a remote postgress server.

## API
The data are accessible via the following api:

### [https://bigtechdetective.club/](https://bigtechdetective.club/) returns a heartbeat

### [/ips](https://bigtechdetective.club/ips) returns the whole dataset in json

```json
{
    "ips":
        [
            {"CIDR":"54.230.212.0/23", "company":"Amazon"},
            {"CIDR":"54.230.214.0/23", "company":"Amazon"},
            // 'etc'
            {"CIDR":"2620:112:3000::/44", "company":"Microsoft"}

        ]
}
```

### [https://bigtechdetective.club/ips/{ip_address}](https://bigtechdetective.club/ips/{ip_address}) gives returns a response indicating whether or not ip_address is in the dataset

for example, [/ips/54.192.0.0](https://bigtechdetective.club/ips/54.192.0.0) returns

```json
{
    "ip":
        {
            "ipaddress":"54.192.0.0",
            "company":"Amazon"    
        }
}
```

an address that isn't in the database, such as `/ips/192.168.0.1`, returns

```json
{
    "errors": [
        "IP not found"
    ]
}
```

and a request that isn't recognized as an ip address returns, such as `/ips/ipaddress`

```json
{
    "errors": [
        "not a valid IP address",
        "IP not found"
    ]
}

```
