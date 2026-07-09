import os
import boto3
import schedule

region = os.environ.get("AWS_REGION", "eu-west-2")
ec2_client = boto3.client('ec2', region_name=region)

def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        try:
            new_snapshot = ec2_client.create_snapshot(
                VolumeId=volume['VolumeId']
            )
            print(new_snapshot)
        except Exception as e:
            print(f"Error occurred while creating snapshot for volume {volume['VolumeId']}: {e}")

schedule.every(20).seconds.do(create_volume_snapshots)

# start the scheduler
while True:
    schedule.run_pending()

