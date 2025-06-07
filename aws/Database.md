Relational database(RDS) OLTP(Online Tranaction processing)
 SQL
 MYSQL
 PostgresSQL
 Oracle
 Aurora
 MariaDB

Dynamodb(No SQL)
Red shift(OLAP)

Elastic  cache
 Memcached
 Redis

RDS Runs on virtual machine
You can't login to RDS operating systems however
Patching of RDS operating system and DB is amazon responsibility
RDS is not serverless

There are two different type of backups for RDS
- Automated backups
- Database snapshots

Basics of DynamoDB
- Stored SSD storage
- Spread across 3 geographically dicstnct data centres
- Eventual consistenet reads(Default)
- Strong consistent reads(less than a second)


Redshift
- Redshift is used for business intelligence
- Available in only 1 AZ
- Enabled by default with a 1 day retention period
- Maximum retention period is 35 days
- Redshift always attempts to maintain at least three copies of your data(the original and replica on compute nodes and backup in Amazon S3)
- Redshift can also asynchronously replicate your snapshots to S3 in another region for disaster recovery

Aurora Exam tips
- 2 copies of your data are contained in each availiblity zone, with minimum of 3 availiblity zones, 6 copies for your data
- You can share Aurora snapshots with other AWS accounts
- 3 types of replica availibe Aurora Replicas,MySQL replicas and PostgresSQL replicas automated failover is only available with Aurora replcas
- Aurora has automated backups turned on by defualt, You can also take snapshots with Aurora, You can share these snapshots with other
  AWS accounts
- Use Aurora serverless if you want a simple, cost-effective option for frequently, intermittent,unpredicatable workloads

Elastic cache
- Use Elasticcache to increase database and webapplication performance 
- Redis is multi AZ
- You can do backups and restore redis



