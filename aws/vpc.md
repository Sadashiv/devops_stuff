Virtual private cloud(VPC)

- When you create a VPC a default Route table, Network Access Control List(NACL) and default secuirty group
- It wont create any subnets, nor will it create a default internet gateway
- US-East-1A in your aws account can be completeley different availiblity zone to US-East-1A in another AWS account.
  The AZ's are randomized
- Amazon always reserve 5 IP addresses within your subnets
- You can only have 1 Internet gateway per VPC
- Secuirty groups can't span VPC's

NAT Instances and NAT Gateways(Network address translation)
- When creating a NAT instance, disable Source/Destination check on the instance
- NAT instance must be public subnet
- There must be route out of the private subnet to the NAT instance in oreder for this work
- The amount of traffic that NAT instance can support depends on the instane size. If you are bottlenecking, increase the instance size
- You can create high availiblity using autoscaling groups, multiple subnets in different AZ's and script to automatic failover.
- Behind security group
- Redundant inside the availabilty Zone
- Not associated with security groups
- No need to patch
- Not associated with security groups
- Remember to update your route tables
- No need to disable Source/Destination checks


VPC Private link
- If you see a question asking about peering VPC's to tens, or thousands of customers VPC's Think of AWS private link
- Doesn't require VPC peering; no route table, NAT, IGWs etc
- Requires a network load balancer on the service VPC and an ENI on the customer VPC

Transit Gateway - Combining gateway for all vpn connection, amazon vpc etc
