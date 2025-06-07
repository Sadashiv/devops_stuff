https://978578900743.signin.aws.amazon.com/console
https://signin.aws.amazon.com/switchrole?roleName=S3_cross_account_access
374260077541
IAM(Identify Access Management)
You can create
- users
- groups
- roles

creates new url for user
Each 12digitid or domain name is unique

Management and Goverance create cloud watch setting up an billing alaram

S3(Simple storage service)

- S3 is object based Think of objects just as files
- It gurantees upload of data 0 to 5TB of data.
- Files are stored in simple buckets

Objects consist of the fallowing

- Key(The simple name of object)
- Value(This is simply the data and is made up of sequence of bytes)
- Version ID(Important for versioning)
- Metadata(Data about data you are storing)
- Resources
    Access control Lists
    Torrent

* S3 has the fallowing features:
- Tiered storage availble
- Lifecycle management
- Versioning
- Encryption
- MFA Delete
- Secure your data using Access control Lists and Bucket policies

* S3 Storage classes

- S3 standarad 
- S3 IA(Infrequently accessed) May be monthly once
- S3 One Zone IA
- S3 Intelligent Tiering
- S3 Glacier(Low-cost storage class data archiving for years) 
- S3 Glacier Deep Archive

S3 charged for fallowing ways
- Storage
- Requests
- Storage management pricing
- Data transfer pricing
- Transfer Acceleration
- Cross Region Replication pricing

Successful uploads will generate a HTTP 200 status code

- Read after Write consistency for PUTS of new objects
- Eventually consistency for overwrite PUTS and DELETES(Can take some time to propagate)

Creating the S3 bucket name should be unique

S3 FAQ before taking exam
All users will upload the files to edge location, edge location uses the amazon backbone network to speed up

Restricting the Bucket Access
- Bucket policies - Applied accross the whole bucket
- Object policies - Applied to individual files
- IAM Policies to Users and Groups - Applies to Users and Groups

s3 basics
 Encryption in Transit is achieved by SSL/TLS
 Encryption At Rest(Server Side) is schieved by
    - s3 managed keys-SSE(Server side Encryption)-S3
    - AWS key management service managed keys-SSE-KMS
    - Server side Encryption with customer provided keys-SSE-C

Client side Encryption

Encrypt at bucket level, Individual object level,
Each version to be made public in S3 bucket to access by default it will be private
Once versioning enabled it can't be Disabled, but it can be suspended

Life cycle in bucket management
Lifecyle allows you to automate moving storage different tiers

S3 lock
 Write once and read many(WORM)
 Goverance mode - User can't overwrite or delete delete an object version or alter it's lock
 settings unless they have special permissions with Goveranance mode.
 In the Governance mode particular user to alter or retention settings or delete the objects if necessary.

 Compliance mode - including root user in aws account can't be overwritten or deleted by user.

Glacier vault lock
- Object locks can be individual object or or applied across the bucket.
- Object mode comes in two modes Governance mode and Compliance mode

S3 Performance
- what is prefix
  mybucketname/folder1/subfolder1/myfile.jpg > /folder1/subfolder1
  mybucketname/folder1/myfile.jpg > /folder1

  Highr number of 3500 PUT/COPY/POST/DELETE 
  5500 GET/HEAD requests per second per prefix
  2 prefixes 11,000 per second

S3 before uses more time time download cvs/zip file and load data
S3 select after write simple SQl query(get subset of data) to increase performance up to 400% and 80% cheaper

3 different ways to share S3 bucket across accounts
- Using Bucket policies and IAM(Applies across the entire bucket) programatic access only
- Using bucket ACLs and IAM(Individual objects) Programtic access only
- Corss account IAM roles, Programatic and Console access

Corss Region Replication
- Vesioning must be enabled on both source and destination buckets
- Files in existing buckets are not repicated automatically
- All subsequent updated files will be replicated automatically
- Delete markers are not replicated
- Deleting individual versions or delete markers will not be replciated

Transfer Accelartion
https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html

Data sync
own cloud to aws

Cloud front is CDN
- CloudFront Distributions
- Web and RTMP(user for media streamin)

Edge location - This is location where content will be cached. this is seperate to an AWS Region/AZ
Origin - This is the origin of all the files that CDN will distribute. This can be either an S3 bucket, an EC2 instance,
         an Elastic Load Balancer or Route53
Distribution - This is the name given to the CDN which consists of collection of Edge locations
Web Distribution - Typically used for websites
RTMP - used for media streaming
objects are cached for the life of the TTL(Time To Live)

Cloud Front Signed URL's and Cookies

- Use signed URLs/Cookies when you want to secure content so that only the people you authorize are able to access it.
- Signed URL is for individual files 1 file = 1 URL
- Signed cookie is for multiple files 1 cookie = multiple files
- If your origin is EC2, then use CloudFront
You can invalidate and this will go away from edge location

Note: Snowball topic is optional for AWS Exam
Snowball is transfering the very high data to AWS

Three different types of storage
- File gateway(NFS & SMB)
- Volume Gateway(iSCSI)
    Stored Volumes - Entire dataset is stored on site and is asynchronusly backed up to S3
    Cached Volumes - Entire dataset is stored on S3 and the most frequently accessed data is cached on site
- Tape gateway(VTL) 
Datasync
One premisis store data and push to s3


Athena Vs Macie
Athena(for sql query S3)
- Athena is an interactive query service
- It allows you to query data located in S3 using standarad SQL
- Serverless
- Commonly used to analyse data stored in S3

Macie(Secuirty service looks for PII)
- Macie uses AI to analyse data in S2 and helps identify PII
- Can also be used to analyse cloudtrail logs for suspicious API activity
- Includes dashboards, Reports and Altering
- Great for PCI-DSS compliance and preventing ID theft
