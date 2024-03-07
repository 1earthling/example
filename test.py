import boto3
from datetime import datetime, timedelta

class DatabaseMetrics:
    def __init__(self, db_identifier):
        self.db_identifier = db_identifier
        self.cloudwatch = boto3.client('cloudwatch')
        self.namespace = 'AWS/RDS'
        self.period = 300  # 5 minutes
        self.end_time = datetime.utcnow()
        self.start_time = self.end_time - timedelta(hours=1)  # Default to last hour
    
    def get_metric_statistics(self, metric_name, statistics):
        response = self.cloudwatch.get_metric_statistics(
            Namespace=self.namespace,
            MetricName=metric_name,
            Dimensions=[{'Name': 'DBInstanceIdentifier', 'Value': self.db_identifier}],
            StartTime=self.start_time,
            EndTime=self.end_time,
            Period=self.period,
            Statistics=statistics,
        )
        return response['Datapoints']
    
    def avg_cpu_usage(self):
        datapoints = self.get_metric_statistics('CPUUtilization', ['Average'])
        return sum(d['Average'] for d in datapoints) / len(datapoints) if datapoints else None

    def max_cpu_usage(self):
        datapoints = self.get_metric_statistics('CPUUtilization', ['Maximum'])
        return max(d['Maximum'] for d in datapoints) if datapoints else None
    
    def avg_mem_usage(self):
        datapoints = self.get_metric_statistics('FreeableMemory', ['Average'])
        total_memory_bytes = 32 * 1024 * 1024 * 1024  # Example for db.r5.xlarge
        avg_freeable = sum(d['Average'] for d in datapoints) / len(datapoints) if datapoints else total_memory_bytes
        return ((total_memory_bytes - avg_freeable) / total_memory_bytes) * 100

    def max_mem_usage(self):
        datapoints = self.get_metric_statistics('FreeableMemory', ['Maximum'])
        total_memory_bytes = 32 * 1024 * 1024 * 1024  # Example for db.r5.xlarge
        max_freeable = min(d['Maximum'] for d in datapoints) if datapoints else total_memory_bytes
        return ((total_memory_bytes - max_freeable) / total_memory_bytes) * 100

    def avg_number_of_connections(self):
        datapoints = self.get_metric_statistics('DatabaseConnections', ['Average'])
        return sum(d['Average'] for d in datapoints) / len(datapoints) if datapoints else None
