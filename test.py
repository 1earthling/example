import boto3
from datetime import datetime, timedelta

class RedisMetrics:
    def __init__(self):
        self.elasticache = boto3.client('elasticache')
        self.cloudwatch = boto3.client('cloudwatch')
        # Map of node types to their total memory in bytes (for memory percentage calculation)
        self.node_type_memory = {
            'cache.r6g.large': 15.25 * 1024**3,  # Example entry, adjust according to actual memory
        }

    def fetch_cloudwatch_metrics(self, cluster_id, metric_name):
        """Fetch CloudWatch metrics for a given metric name and cluster ID."""
        now = datetime.utcnow()
        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ElastiCache',
            MetricName=metric_name,
            Dimensions=[{'Name': 'CacheClusterId', 'Value': cluster_id}],
            StartTime=now - timedelta(days=1),
            EndTime=now,
            Period=3600,  # Example: 1 hour
            Statistics=['Average', 'Maximum']
        )
        return response['Datapoints']

    def calculate_metrics(self, cluster_id, metric_name):
        """Calculate and return average and maximum metric values for a given cluster."""
        data_points = self.fetch_cloudwatch_metrics(cluster_id, metric_name)
        metrics = [(point['Average'], point['Maximum']) for point in data_points]

        if metrics:
            avg_metric = sum([metric[0] for metric in metrics]) / len(metrics)
            max_metric = max([metric[1] for metric in metrics])
            return avg_metric, max_metric
        else:
            return 0, 0

    def get_cpu_usage(self, cluster_id):
        """Get average and maximum percent CPU usage for a given cluster."""
        return self.calculate_metrics(cluster_id, 'CPUUtilization')

    def get_memory_usage(self, cluster_id, node_type):
        """Get average and maximum percent memory usage for a given cluster."""
        avg_memory_bytes, max_memory_bytes = self.calculate_metrics(cluster_id, 'FreeableMemory')
        total_memory_bytes = self.node_type_memory.get(node_type, 1)  # Avoid division by zero

        avg_memory_usage_percent = ((total_memory_bytes - avg_memory_bytes) / total_memory_bytes) * 100
        max_memory_usage_percent = ((total_memory_bytes - max_memory_bytes) / total_memory_bytes) * 100

        return avg_memory_usage_percent, max_memory_usage_percent

# Example usage
if __name__ == "__main__":
    metrics = RedisMetrics()
    cluster_id = 'your-cluster-id-here'
    node_type = 'cache.r6g.large'  # Example node type, adjust as needed

    avg_cpu, max_cpu = metrics.get_cpu_usage(cluster_id)
    print(f"Average CPU Usage: {avg_cpu}%, Maximum CPU Usage: {max_cpu}%")

    avg_memory, max_memory = metrics.get_memory_usage(cluster_id, node_type)
    print(f"Average Memory Usage: {avg_memory}%, Maximum Memory Usage: {max_memory}%")
