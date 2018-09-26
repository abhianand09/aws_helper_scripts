# AWS handy script for create AMI from an instance-id and copy it to another region

Prerequisites:

```
1.Before running the scripts make sure you have aws cli configured properly as this script will require your access key ID and secret accesskey.

```


```
```

Usage:

```
./create_and_copy.sh instance-id source-region destination-region
```




Description:

This script will first take the AMI of the instance-id provided by user and copy it to the region where user wants it

For example:
```
./create_and_copy.sh i-00563f37eb9b204c0 ap-southeast-1 ap-south-1
will copy new AMI of this instance from ap-southeast-1 region to ap-south-1 region
```



