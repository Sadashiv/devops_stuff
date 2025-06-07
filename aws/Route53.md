Route53

- ELBs do not have pre-defined IPv4 addresses; you resolve to them using a DNS name.
- Understand the differeance between an alias record and CNAME
- Given the choice, Always choose an alias over a CNAME

CNAMES  can't be used for naked domain like starts with domain name
A records are address

Comman DNS Types
- SOA Records
- NS Records
- A Records
- CNAMES
- MX Records
- PTR Records


Register domain ssiindia.net
then create hostedzone

create different servers in different zone

then create record set for domain ssgindia.net

user -> Route 53 diffrenet time will redirect less time request serving webserver

Routing policy
- Simple routing policy
- Latency Routing policy
- Failover Routing policy
- Geolocation Routing policy

