#!/usr/bin/env python

import botocore
import boto3
import os
import re
import sys



client = boto3.client('ec2')
inFile = sys.argv[1]

def retrieve_entity_tag_name(amiid):
 try:
  response = client.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [
                amiid,
            ],
        },
         {
            'Name': 'tag-key',
            'Values': [
                'Entity',
            ],
        },
    ],
   )
  if not response['Tags']:
    return None

  for d in response['Tags']:
    return d['Value']

 except botocore.exceptions.ClientError:
   print "AMI id not found"


def get_ami_id_tag_by_snapshot_id(snapshot_id):
 response = client.describe_snapshots(
         SnapshotIds=[
            snapshot_id,
         ],
         )

 for d in response["Snapshots"]:
           a=d["Description"]
           x=re.search('for\s(ami-\w+\S)',a)
           if x:
            #print x.group(1)
            tag=retrieve_entity_tag_name(x.group(1))
	    if tag:
               #print "tag found"
               add_tag_to_snapshot(snapshot_id,tag)
            else:
               print "null value of tag"
           else:
    	     print "ami Desc Not found"


def add_tag_to_snapshot(snapshotid,tag_value):

 try:
  response = client.create_tags(
    Resources=[
        snapshotid,
    ],
    Tags=[
        {
            'Key': 'Entity',
            'Value': tag_value,
        },
    ],
  )

  print(response)

 except botocore.exceptions.ClientError:
  print "not found"


with open(inFile) as f:
    lines = f.readlines()
    
for k in lines:
  j=k.split('\n')
  get_ami_id_tag_by_snapshot_id(j[0])
