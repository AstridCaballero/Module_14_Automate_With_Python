{
    'InstanceStatuses': [
        {
            'AvailabilityZone': 'string',
            'AvailabilityZoneId': 'string',
            'OutpostArn': 'string',
            'Operator': {
                'Managed': True|False,
                'Principal': 'string',
                'HiddenByDefault': True|False
            },
            'Events': [
                {
                    'InstanceEventId': 'string',
                    'Code': 'instance-reboot'|'system-reboot'|'system-maintenance'|'instance-retirement'|'instance-stop',
                    'Description': 'string',
                    'NotAfter': datetime(2015, 1, 1),
                    'NotBefore': datetime(2015, 1, 1),
                    'NotBeforeDeadline': datetime(2015, 1, 1)
                },
            ],
            'InstanceId': 'string',
            'InstanceState': {
                'Code': 123,
                'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
            },
            'InstanceStatus': {
                'Details': [
                    {
                        'ImpairedSince': datetime(2015, 1, 1),
                        'Name': 'reachability',
                        'Status': 'passed'|'failed'|'insufficient-data'|'initializing'
                    },
                ],
                'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
            },
            'SystemStatus': {
                'Details': [
                    {
                        'ImpairedSince': datetime(2015, 1, 1),
                        'Name': 'reachability',
                        'Status': 'passed'|'failed'|'insufficient-data'|'initializing'
                    },
                ],
                'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
            },
            'AttachedEbsStatus': {
                'Details': [
                    {
                        'ImpairedSince': datetime(2015, 1, 1),
                        'Name': 'reachability',
                        'Status': 'passed'|'failed'|'insufficient-data'|'initializing'
                    },
                ],
                'Status': 'ok'|'impaired'|'insufficient-data'|'not-applicable'|'initializing'
            }
        },
    ],
    'NextToken': 'string'
}