import boto3
from datetime import datetime, timedelta

class RedisMetrics:
    def __init__(self):
        self.elasticache = boto3.client('elasticache')
        self.cloudwatch = boto3.client('cloudwatch')
        # Assuming total memory for cache.r6g.2xlarge is 64GB (convert to bytes)
        self.node_type_memory = {
            'cache.r6g.2xlarge': 64 * 1024 ** 3  # 64 GB in bytes
        }

    def fetch_clusters_by_node_type(self, node_type):
        clusters = self.elasticache.describe_cache_clusters(ShowCacheNodeType=True)
        filtered_cluster_ids = [
            cluster['CacheClusterId']
            for cluster in clusters['CacheClusters']
            if cluster['CacheNodeType'] == node_type and cluster['Engine'] == 'redis'
        ]
        return filtered_cluster_ids

    def fetch_cloudwatch_metrics(self, cluster_id, metric_name):
        now = datetime.utcnow()
        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ElastiCache',
            MetricName=metric_name,
            Dimensions=[{'Name': 'CacheClusterId', 'Value': cluster_id}],
            StartTime=now - timedelta(days=1),
            EndTime=now,
            Period=3600,
            Statistics=['Average', 'Maximum']
        )
        return response['Datapoints']

    def calculate_metrics(self, node_type, metric_name):
        cluster_ids = self.fetch_clusters_by_node_type(node_type)
        metrics = []
        for cluster_id in cluster_ids:
            data_points = self.fetch_cloudwatch_metrics(cluster_id, metric_name)
            for point in data_points:
                metrics.append((point['Average'], point['Maximum']))

        if metrics:
            avg_metric = sum([metric[0] for metric in metrics]) / len(metrics)
            max_metric = max([metric[1] for metric in metrics])
            return avg_metric, max_metric
        else:
            return 0, 0

    def get_cpu_usage(self, node_type):
        return self.calculate_metrics(node_type, 'CPUUtilization')

    def get_memory_usage(self, node_type):
        avg_memory_bytes, max_memory_bytes = self.calculate_metrics(node_type, 'FreeableMemory')
        total_memory_bytes = self.node_type_memory.get(node_type, 1)  # Default to 1 to avoid division by zero

        # Adjust the calculation for percent memory usage
        avg_memory_usage_percent = ((total_memory_bytes - avg_memory_bytes) / total_memory_bytes) * 100
        max_memory_usage_percent = ((total_memory_bytes - max_memory_bytes) / total_memory_bytes) * 100

        return avg_memory_usage_percent, max_memory_usage_percent

# Example usage
if __name__ == "__main__":
    metrics = RedisMetrics()
    node_type = 'cache.r6g.2xlarge'

    avg_cpu, max_cpu = metrics.get_cpu_usage(node_type)
    print(f"Average CPU Usage: {avg_cpu}%, Maximum CPU Usage: {max_cpu}%")

    avg_memory, max_memory = metrics.get_memory_usage(node_type)
    print(f"Average Memory Usage: {avg_memory}%, Maximum Memory Usage: {max_memory}%")
