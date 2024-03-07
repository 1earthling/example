import boto3

def list_writer_instances_aurora():
    rds_client = boto3.client('rds')
    writer_instances = []

    # Describe all DB clusters
    clusters = rds_client.describe_db_clusters()
    for cluster in clusters['DBClusters']:
        for member in cluster['DBClusterMembers']:
            if member['IsClusterWriter']:
                writer_instances.append(member['DBInstanceIdentifier'])

    return writer_instances

# For Aurora
writer_instances_aurora = list_writer_instances_aurora()
print("Aurora Writer Instances:", writer_instances_aurora)
