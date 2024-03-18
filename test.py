import boto3

def list_redis_clusters():
    # Create an ElastiCache client
    elasticache = boto3.client('elasticache')

    # Retrieve all Redis cluster descriptions
    response = elasticache.describe_cache_clusters(ShowCacheNodeInfo=True)
    
    # Check if any clusters exist
    if response['CacheClusters']:
        print("Listing Redis clusters:")
        for cluster in response['CacheClusters']:
            # Filter for Redis clusters
            if cluster['Engine'] == 'redis':
                print(f"Cluster ID: {cluster['CacheClusterId']}, Status: {cluster['CacheClusterStatus']}")
    else:
        print("No Redis clusters found.")

if __name__ == "__main__":
    list_redis_clusters()
