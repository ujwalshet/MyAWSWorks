import boto3
import logging
 
ec2 = boto3.client('ec2')
sns = boto3.client('sns')
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
TOPIC_ARN = 'arn:aws:sns:us-east-1:851725424827:EC2HealthAlerts'
 
def lambda_handler(event, context):
    logger.info("Lambda function started")
    response = ec2.describe_instance_status(IncludeAllInstances=True)
    unhealthy = []
 
    for status in response['InstanceStatuses']:
        instance_id = status['InstanceId']
        state = status['InstanceState']['Name']
        sys_status = status['SystemStatus']['Status']
        inst_status = status['InstanceStatus']['Status']
 
        logger.info(f"{instance_id}: {state}, system={sys_status}, instance={inst_status}")
 
        if state in ['stopped', 'stopping', 'shutting-down', 'terminated'] or sys_status != 'ok' or inst_status != 'ok':
            unhealthy.append(f"{instance_id}: {state}, system={sys_status}, instance={inst_status}")
 
    if unhealthy:
        message = "Unhealthy EC2 Instances Detected:\n\n" + "\n".join(unhealthy)
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="EC2 Health Alert",
            Message=message
        )
        logger.info("SNS alert successfully sent.")
    else:
        logger.info("All instances are healthy.")
