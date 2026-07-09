import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-west-2")

# get volumes with tag 'prod'
volume_prod = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )

# iterate over the list of 'prod' volumes
for volume in volume_prod['Volumes']:
    # get all snapshots for the specific volume
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id', # from describe_snapshots()
                'Values': [
                    volume['VolumeId'], # from describe_volumes()
                ]
            },
        ]
    )

    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    # delete the snapshot
    for snap in sorted_by_date[2:]:
        response = ec2_client.delete_snapshot(
            SnapshotId=snap['SnapshotId']
        )
        print(response)



