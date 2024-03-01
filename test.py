import boto3
from datetime import datetime, timedelta

# Initialize a CloudWatch client
cloudwatch_client = boto3.client('cloudwatch')

# Specify your RDS Global Database identifier and the region it's located in
db_identifier = 'your-global-db-identifier'

# Define the time period for the metrics you want to retrieve
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=1)  # Adjust based on your needs

# Retrieve metrics from CloudWatch
response = cloudwatch_client.get_metric_statistics(
    Namespace='AWS/RDS',
    MetricName='GlobalDBReplicationLag',
    Dimensions=[
        {
            'Name': 'DBClusterIdentifier',
            'Value': db_identifier
        },
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,  # 5 minutes in seconds
    Statistics=['Average', 'Maximum'],  # You can specify other statistics as needed
)

# Print the response
print(response)
