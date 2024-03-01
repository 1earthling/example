import boto3

def list_db_identifiers():
    # Create an RDS client
    rds_client = boto3.client('rds')
    
    # Initialize a list to hold DB identifiers
    db_identifiers = []
    
    # Paginate through all DB instances if there are more than the service limit
    paginator = rds_client.get_paginator('describe_db_instances')
    for page in paginator.paginate():
        for db_instance in page['DBInstances']:
            db_identifiers.append(db_instance['DBInstanceIdentifier'])
    
    return db_identifiers

# Get the list of DB identifiers and print them
db_identifiers = list_db_identifiers()
print("RDS DB Instance Identifiers:", db_identifiers)
