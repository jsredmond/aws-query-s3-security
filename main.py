import boto3

client = boto3.client('s3')
querybuckets = client.list_buckets()
buckets = [bucket['Name'] for bucket in querybuckets['Buckets']]

for bucket in buckets:
    try:
        bucket = client.get_bucket_encryption(Bucket=bucket)
    except client.exceptions.ClientError:
        print('The S3 bucket %s has no encryption configured!' % bucket)