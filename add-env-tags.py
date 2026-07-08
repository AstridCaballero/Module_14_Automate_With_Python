import boto3

ec2_client_frankfurt = boto3.client('ec2',region_name='eu-central-1')
ec2_resource_frankfurt = boto3.resource('ec2', region_name='eu-central-1')

ec2_client_Paris = boto3.client('ec2',region_name='eu-west-3')
ec2_resource_Paris = boto3.resource('ec2', region_name='eu-west-3')

instances_ids_frankfurt = []
instances_ids_Paris = []

reservations_frankfurt = ec2_client_frankfurt.describe_instances()['Reservations']
for res in reservations_frankfurt:
    instances = res['Instances']
    for ins in instances:
        instances_ids_frankfurt.append(ins['InstanceId'])

response = ec2_resource_frankfurt.create_tags(
    Resources=instances_ids_frankfurt,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

reservations_Paris = ec2_client_Paris.describe_instances()['Reservations']
for res in reservations_Paris:
    instances = res['Instances']
    for ins in instances:
        instances_ids_Paris.append(ins['InstanceId'])

response = ec2_resource_Paris.create_tags(
    Resources=instances_ids_Paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)