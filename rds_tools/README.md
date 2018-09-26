# AWS rds handy tools for list,delete,create snapshot,copy snapshot & create event subscription

Prerequisites:

```
1.Before running the scripts make sure you have aws cli configured properly as this script will require your access key ID and secret accesskey.

```


```
```

Usage:

```
./rds_script.py --help
Usage: rds_script.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  copy-db-snapshot
  create-db-snapshot
  create-event-subscription
  delete-db-instance
  list-rds-instances


To check what parameter does any of the above Commands takes use like:

./rds_script.py copy-db-snapshot --help

This will output the usage of the command


Usage: rds_script.py copy-db-snapshot [OPTIONS] RDS_SNAPSHOT_IDENTIFIER
                                      RDS_SNAPSHOT_IDENTIFIER_ARN
                                      SOURCE_REGION DESTINATION_REGION


```


Note for copy-db-snapshot it is valid only for MySQL RDS ,Maria DB and Postgres DB




Description:

This script will take one command from below list at a time and does the needful:

Commands:
  copy-db-snapshot
  create-db-snapshot
  create-event-subscription
  delete-db-instance
  list-rds-instances

 




