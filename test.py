import boto3
from botocore.config import Config

def list_s3_buckets_and_files():
    # Disable SSL verification
    boto3_config = Config(
        retries={
            'max_attempts': 10,
            'mode': 'standard'
        },
        verify=False
    )

    s3_client = boto3.client('s3', config=boto3_config)
    s3_resource = boto3.resource('s3', config=boto3_config)

    buckets = s3_client.list_buckets()

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        print(f"Bucket: {bucket_name}")
        
        bucket_resource = s3_resource.Bucket(bucket_name)
        folders = {}

        for obj in bucket_resource.objects.all():
            folder = '/'.join(obj.key.split('/')[:-1])
            if folder not in folders:
                folders[folder] = 0
            folders[folder] += 1

        for folder, count in folders.items():
            print(f"  Folder: {folder}, File Count: {count}")

if __name__ == "__main__":
    list_s3_buckets_and_files()
