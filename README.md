# Data Processing for [Big Tech Detective](https://bigtechdetective.net)

[Autonomous System Numbers](https://www.arin.net/resources/guide/asn/) for each tech giant are collected by hand by watching [BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) peering using [BGPview](https://bgpview.io/). ASNs are converted to CIDR blocks via `asn_to_cidr_blocks` a simple bash script that takes a CSV of Company,ASNs pairs and converts it into a csv of Company,CIDR pairs.

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

The outputted csv contains about 60,000 CIDR blocks, which corresponds to trillions of IPv4 and IPv6 addresses. It is then added to a table on a remote Postgres database, which is queryable via the [Big Tech Detective API](https://gitlab.com/big-tech-detective/Blocker-API).