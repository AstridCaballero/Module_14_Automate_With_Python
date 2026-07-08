{
    'cluster': {
        'name': 'string',
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'version': 'string',
        'endpoint': 'string',
        'roleArn': 'string',
        'resourcesVpcConfig': {
            'subnetIds': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ],
            'clusterSecurityGroupId': 'string',
            'vpcId': 'string',
            'endpointPublicAccess': True|False,
            'endpointPrivateAccess': True|False,
            'publicAccessCidrs': [
                'string',
            ],
            'controlPlaneEgressMode': 'AWS_MANAGED'|'CUSTOMER_ROUTED'|'CUSTOMER_ISOLATED'
        },
        'kubernetesNetworkConfig': {
            'serviceIpv4Cidr': 'string',
            'serviceIpv6Cidr': 'string',
            'ipFamily': 'ipv4'|'ipv6',
            'elasticLoadBalancing': {
                'enabled': True|False
            }
        },
        'logging': {
            'clusterLogging': [
                {
                    'types': [
                        'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                    ],
                    'enabled': True|False
                },
            ]
        },
        'identity': {
            'oidc': {
                'issuer': 'string'
            }
        },
        'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED'|'UPDATING'|'PENDING',
        'certificateAuthority': {
            'data': 'string'
        },
        'clientRequestToken': 'string',
        'platformVersion': 'string',
        'tags': {
            'string': 'string'
        },
        'encryptionConfig': [
            {
                'resources': [
                    'string',
                ],
                'provider': {
                    'keyArn': 'string'
                }
            },
        ],
        'connectorConfig': {
            'activationId': 'string',
            'activationCode': 'string',
            'activationExpiry': datetime(2015, 1, 1),
            'provider': 'string',
            'roleArn': 'string'
        },
        'id': 'string',
        'health': {
            'issues': [
                {
                    'code': 'AccessDenied'|'ClusterUnreachable'|'ConfigurationConflict'|'InternalFailure'|'ResourceLimitExceeded'|'ResourceNotFound'|'IamRoleNotFound'|'VpcNotFound'|'InsufficientFreeAddresses'|'Ec2ServiceNotSubscribed'|'Ec2SubnetNotFound'|'Ec2SecurityGroupNotFound'|'KmsGrantRevoked'|'KmsKeyNotFound'|'KmsKeyMarkedForDeletion'|'KmsKeyDisabled'|'StsRegionalEndpointDisabled'|'UnsupportedVersion'|'Other',
                    'message': 'string',
                    'resourceIds': [
                        'string',
                    ]
                },
            ]
        },
        'outpostConfig': {
            'outpostArns': [
                'string',
            ],
            'controlPlaneInstanceType': 'string',
            'controlPlanePlacement': {
                'groupName': 'string',
                'spreadLevel': 'host'|'rack'
            },
            'etcdInstanceType': 'string',
            'etcdPlacement': {
                'spreadLevel': 'host'|'rack'
            }
        },
        'accessConfig': {
            'bootstrapClusterCreatorAdminPermissions': True|False,
            'authenticationMode': 'API'|'API_AND_CONFIG_MAP'|'CONFIG_MAP'
        },
        'upgradePolicy': {
            'supportType': 'STANDARD'|'EXTENDED'
        },
        'zonalShiftConfig': {
            'enabled': True|False
        },
        'remoteNetworkConfig': {
            'remoteNodeNetworks': [
                {
                    'cidrs': [
                        'string',
                    ]
                },
            ],
            'remotePodNetworks': [
                {
                    'cidrs': [
                        'string',
                    ]
                },
            ]
        },
        'computeConfig': {
            'enabled': True|False,
            'nodePools': [
                'string',
            ],
            'nodeRoleArn': 'string'
        },
        'storageConfig': {
            'blockStorage': {
                'enabled': True|False
            }
        },
        'deletionProtection': True|False,
        'controlPlaneScalingConfig': {
            'tier': 'standard'|'tier-xl'|'tier-2xl'|'tier-4xl'|'tier-8xl'
        }
    }
}