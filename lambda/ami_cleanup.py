import boto3
import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    retention_days = 7  # Change as needed
    delete_before = datetime.datetime.now() - datetime.timedelta(days=retention_days)

    images = ec2.describe_images(Owners=['self'])['Images']

    for image in images:
        creation_date = datetime.datetime.strptime(
            image['CreationDate'], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        if creation_date < delete_before:
            ec2.deregister_image(ImageId=image['ImageId'])
            print(f"Deleted AMI {image['ImageId']}")

    return "Old AMIs Deleted"
