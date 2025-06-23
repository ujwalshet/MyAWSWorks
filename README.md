# AWS Project
EC2 Instance Health Monitoring using AWS Lambda and SNS

A serverless project to monitor the health of the EC2 instances using AWS Lambda. If any EC2 instance is found to be unhealthy or stopped state, an email alert is sent using SNS. Basically, it checks the beow mentioned points:

Checks the health of all the EC2 instances every 5 minutes
Detects the system health basically the status of the instance
Sends alert email with instance ID and status
Its most effective, fully automated and cost effective (Uses free tier resources) this will give an additional layer of monitoring

Components :

Amazon EC2: The compute instances being monitored

AWS Lambda: Python fun triggered every 5 minutes

CloudWatch EventBridge: Schedule to invoke Lambda

SNS (Simple Notification Service): Sends alert emails

IAM Role: Grants Lambda access to EC2 and SNS

Benefits :

No third-party monitoring tool required
Works entirely on AWS Free Tier
Easily extendable: reboot unhealthy instances, send Slack alerts, write to S3, etc...

Deployment Steps

Create an SNS Topic Name: EC2HealthAlerts Add your email as a subscriber and confirm it
Create an IAM Role - Lambda Add permissions: ec2:DescribeInstanceStatus sns:Publish logs:* (optional - CloudWatch logging)
Create the Lambda Function Runtime: Python 3.10 Paste the code above Replace TOPIC_ARN with your actual SNS ARN
Create a CloudWatch EventBridge Rule Schedule: rate(5 minutes) Target: your Lambda fun 
