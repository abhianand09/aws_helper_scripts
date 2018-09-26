#!/bin/bash
set -e

DATE=$(date +%Y-%m-%d_%H-%M) 
INSTANCE_ID=$1
SOURCE_REGION=$2
DESTINATION_REGION=$3

if (( $# != 3 )); then
    printf "Illegal number of arguments \n"
    printf "Usage: ./ami.sh instance-id source-region destination-region"
    exit 1
fi



INST_NAME="$(aws ec2 describe-tags \
--region "$SOURCE_REGION" \
--filters Name=resource-id,Values="$INSTANCE_ID" Name=key,Values=Name \
--query Tags[].Value --output text)"

printf "Requesting AMI for instance $INSTANCE_ID $INST_NAME \n"

SOURCE_IMAGE="$(aws ec2 create-image \
 --region "$SOURCE_REGION" \
 --instance-id "$INSTANCE_ID" \
 --name "$INST_NAME"-"$DATE" \
 --description "$INST_NAME"-"$DATE" --no-reboot)"


aws ec2 wait image-available --image-ids "$SOURCE_IMAGE" --region "$SOURCE_REGION"

printf "AMI for instance $INSTANCE_ID $INST_NAME completed \n"
printf "AMI id for $SOURCE_REGION: $SOURCE_IMAGE \n"

COPIED_IMAGE="$(aws ec2 copy-image \
--source-region "$SOURCE_REGION" \
--region "$DESTINATION_REGION" \
--name "$INST_NAME"-"$DATE" \
--source-image-id "$SOURCE_IMAGE" )"

aws ec2 wait image-available --image-ids "$COPIED_IMAGE" --region "$DESTINATION_REGION"

printf "AMI copied from $SOURCE_REGION to $DESTINATION_REGION for instance $INSTANCE_ID $INST_NAME \n"
printf "AMI id for $DESTINATION_REGION : $COPIED_IMAGE \n"



