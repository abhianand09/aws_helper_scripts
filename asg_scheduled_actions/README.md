# AWS handy script for Autoscaling Scheduled Actions for Non-Prod envs


Prerequisites:

```
1.Before running the scripts make sure you have aws cli configured properly as this script will require your access key ID and secret accesskey.

```


```
2.You have list of all the ASG names in a file on which you want to have scheduled actions implemented
```

Usage:

```
./ASG_scheduled_actions.sh filename
```


filename will look like this:


```
auto_scaling_group_1
auto_scaling_group_2
autoscaling_group_3
autoscaling_group_4
```



Description:

This script will take each input line(ASG name) from the filename and run scale up and scale down scheduled actions for the ASG

For Scale down operation 
```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name ScaleDown --auto-scaling-group-name $line --start-time "2018-06-29T14:30:00Z" --recurrence "30 14 * * MON-FRI" --desired-capacity 0 --min-size 0 --max-size 0
```



For Scale Up operation 
```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name ScaleUp --auto-scaling-group-name $line  --start-time "2018-06-29T22:30:00Z" --recurrence "30 22 * * MON-FRI" --desired-capacity 2 --min-size 2 --max-size 10
```

This script will ensure that all the ASG who has scheduled actions set by this script will shut down all ASG servers at 14:30 UTC and turn on the ASG servers at 22:30 UTC from MON-FRI.
The servers will be down in weekends.


You can change the timings as per your requirement
