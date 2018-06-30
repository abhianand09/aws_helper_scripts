#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do

aws  autoscaling put-scheduled-update-group-action --scheduled-action-name ScaleUp --auto-scaling-group-name $line  --start-time "2018-07-01T22:30:00Z" --recurrence "30 22 * * MON-FRI" --desired-capacity 2 --min-size 2 --max-size 10

aws autoscaling put-scheduled-update-group-action --scheduled-action-name ScaleDown --auto-scaling-group-name $line --start-time "2018-06-30T14:30:00Z" --recurrence "30 14 * * MON-FRI" --desired-capacity 0 --min-size 0 --max-size 0

done < "$1"



