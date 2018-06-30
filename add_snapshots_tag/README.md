# AWS handy script for adding tags to snapshots based on AMI tag key

Prerequisites:

```
1.Before running the scripts make sure you have aws cli configured properly as this script will require your access key ID and secret accesskey.

```


```
2.You have list of all the snapshots ids in a file on which you want to add tags
```

Usage:

```
./snap_tag.py filename
```


filename will look like this:


```
snapshot_ID_1
snapshot_ID_2
snapshot_ID_3
snapshot_ID_4
```



Description:

This script will take each input line(snapshot_id) from the filename and add tag to it based on the AMI tag value for tag key(In this case `Entity`)

For example:
```
Based on the snapshotID Description value first the AMI ID is retrieved and then its value of tag (In this case `Entity`). The tag key `Entity` and its value are then added to its snapshotID
```



You can change the tag key as per your requirement
