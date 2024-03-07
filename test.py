import boto3

def list_writer_db_instances():
    rds_client = boto3.client('rds')
    db_instances = rds_client.describe_db_instances()
    writer_instances = []

    for db_instance in db_instances['DBInstances']:
        # Exclude read replicas by checking if the ReadReplicaSourceDBInstanceIdentifier attribute exists
        if 'ReadReplicaSourceDBInstanceIdentifier' not in db_instance:
            writer_instances.append(db_instance['DBInstanceIdentifier'])

    return writer_instances

# Get the list of writer DB instances and print them
writer_db_instances = list_writer_db_instances()
print("Writer DB Instance Identifiers:", writer_db_instances)
