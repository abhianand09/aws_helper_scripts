#!/usr/bin/env python
import boto3
import click
import datetime



rds = boto3.client('rds')


@click.group()
def cli():
    pass

@cli.command('list-rds-instances')
def list_rds():
 try:
    rds_list = rds.describe_db_instances()
    for rds_name in rds_list['DBInstances']: 
      print (rds_name['Endpoint']['Address'])  
 except Exception as error:
    print error



@cli.command('delete-db-instance')
@click.argument('rds_instance_name')
def del_rds(rds_instance_name):
 try:
    response = rds.delete_db_instance(
        DBInstanceIdentifier=rds_instance_name,
        SkipFinalSnapshot=True)
    print response
 except Exception as error:
    print error



@cli.command('create-db-snapshot')
@click.argument('rds_instance_name')
def create_rds_snapshot(rds_instance_name):
 try:
    now = datetime.datetime.now()
    response = rds.create_db_snapshot(
    DBSnapshotIdentifier=rds_instance_name+"-"+str(now)[:10],
    DBInstanceIdentifier=rds_instance_name,
    )
    print response
 except Exception as error:
    print error



@cli.command('copy-db-snapshot')
@click.argument('rds_snapshot_identifier')
@click.argument('rds_snapshot_identifier_arn')
@click.argument('source_region')
@click.argument('destination_region')
def copy_rds_snapshot(rds_snapshot_identifier,rds_snapshot_identifier_arn,source_region,destination_region):
 try:
    now = datetime.datetime.now()
    rds1 = boto3.client('rds', region_name=destination_region)
    response = rds1.copy_db_snapshot(
    SourceDBSnapshotIdentifier=rds_snapshot_identifier_arn,
    TargetDBSnapshotIdentifier=rds_snapshot_identifier,
    CopyTags=True,
    SourceRegion=source_region
)
    print response
 except Exception as error:
    print error    


@cli.command('create-event-subscription')
@click.argument('rds_instance_name')
@click.argument('subscription_name')
@click.argument('sns_topic_arn')
def create_rds_event_subscr(rds_instance_name,subscription_name,sns_topic_arn):
 try:
    response = rds.create_event_subscription(
    SubscriptionName=subscription_name,
    SnsTopicArn=sns_topic_arn,
    SourceType="db-instance",
    SourceIds=[
        rds_instance_name,
    ],
    Enabled=True,
    )
    print response
 except Exception as error:
    print error



if __name__ == '__main__':
    cli()    