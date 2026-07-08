{
    'NextToken': 'string',
    'Volumes': [
        {
            'AvailabilityZoneId': 'string',
            'OutpostArn': 'string',
            'SourceVolumeId': 'string',
            'Iops': 123,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'VolumeType': 'standard'|'io1'|'io2'|'gp2'|'sc1'|'st1'|'gp3',
            'FastRestored': True|False,
            'MultiAttachEnabled': True|False,
            'Throughput': 123,
            'SseType': 'sse-ebs'|'sse-kms'|'none',
            'Operator': {
                'Managed': True|False,
                'Principal': 'string',
                'HiddenByDefault': True|False
            },
            'VolumeInitializationRate': 123,
            'VolumeId': 'string',
            'Size': 123,
            'SnapshotId': 'string',
            'AvailabilityZone': 'string',
            'State': 'creating'|'available'|'in-use'|'deleting'|'deleted'|'error',
            'CreateTime': datetime(2015, 1, 1),
            'Attachments': [
                {
                    'DeleteOnTermination': True|False,
                    'AssociatedResource': 'string',
                    'InstanceOwningService': 'string',
                    'EbsCardIndex': 123,
                    'VolumeId': 'string',
                    'InstanceId': 'string',
                    'Device': 'string',
                    'State': 'attaching'|'attached'|'detaching'|'detached'|'busy',
                    'AttachTime': datetime(2015, 1, 1)
                },
            ],
            'Encrypted': True|False,
            'KmsKeyId': 'string'
        },
    ]
}