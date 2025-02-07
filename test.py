import boto3
from datetime import datetime, timedelta, timezone

# Initialize RDS and Performance Insights clients
rds_client = boto3.client("rds", region_name="us-west-2")  # Change region as needed
pi_client = boto3.client("pi", region_name="us-west-2")  # Same region for PI

# Get all RDS instance identifiers
def get_rds_instances():
    instances = []
    paginator = rds_client.get_paginator("describe_db_instances")
    for page in paginator.paginate():
        for db in page["DBInstances"]:
            if "PerformanceInsightsEnabled" in db and db["PerformanceInsightsEnabled"]:
                instances.append(db["DBInstanceIdentifier"])
    return instances

# Define time range (last 1 hour)
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=1)

# Metrics to fetch
metrics = ["DBLoad", "CallsPerSecond", "Latency"]

# Iterate through each RDS instance
for db_instance in get_rds_instances():
    print(f"\n🔍 Fetching metrics for RDS Instance: {db_instance}")

    try:
        # Get Performance Insights metrics
        response = pi_client.get_resource_metrics(
            ServiceType="RDS",
            Identifier=db_instance,
            MetricQueries=[{"Metric": metric} for metric in metrics],
            StartTime=start_time,
            EndTime=end_time,
            PeriodInSeconds=60,  # 1-minute intervals
        )

        # Print metrics
        for metric in response["MetricList"]:
            print(f"\n📊 Metric: {metric['Key']['Metric']}")
            for datapoint in metric["DataPoints"]:
                print(f"  Timestamp: {datapoint['Timestamp']}, Value: {datapoint['Value']}")

        # Get top SQL statements by DBLoad
        sql_response = pi_client.describe_dimension_keys(
            ServiceType="RDS",
            Identifier=db_instance,
            Metric="DBLoad",
            StartTime=start_time,
            EndTime=end_time,
            PeriodInSeconds=60,
            GroupBy={"Group": "db.sql.statement"},  # Get full SQL statements
            MaxResults=5
        )

        print("\n🔥 Top SQL Statements by Load:")
        for item in sql_response["Keys"]:
            sql_statement = item["Key"]
            load = item["Value"]
            print(f"  SQL: {sql_statement}, Load: {load}")

    except Exception as e:
        print(f"❌ Error fetching Performance Insights for {db_instance}: {e}")
