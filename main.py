import boto3

client = boto3.client('s3')
querybuckets = client.list_buckets()
buckets = [bucket['Name'] for bucket in querybuckets['Buckets']]

for bucket in buckets:
    try:
        bucket = client.get_bucket_encryption(Bucket=bucket)
    except client.exceptions.ClientError:
        print('The S3 bucket %s has no encryption configured!' % bucket)

for bucket in client.list_buckets()['Buckets']:
  bucket = bucket['Name']
  response = client.get_bucket_versioning(Bucket=bucket)
  if 'Status' in response and response['Status'] == 'Enabled':
    print('The S3 bucket %s does not have versioning configured!' % bucket)