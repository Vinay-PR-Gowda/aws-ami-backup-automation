import boto3
import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ['i-xxxxxxxxxxxxxxxxx']  # Replace with your instance IDs
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    for instance in instances:
        response = ec2.create_image(
            InstanceId=instance,
            Name=f"AMI-Backup-{instance}-{date}",
            Description="Automated AMI Backup",
            NoReboot=True
        )
        print(f"AMI {response['ImageId']} created for instance {instance}")

    return "AMI Creation Completed"
