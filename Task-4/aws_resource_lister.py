import boto3
import sys

def list_ec2_resources(region):
    """List EC2 instances"""
    try:
        ec2 = boto3.client('ec2', region_name=region)
        
        print(f"\n=== EC2 Instances in {region} ===")
        response = ec2.describe_instances()
        
        instance_count = 0
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_count += 1
                instance_id = instance['InstanceId']
                instance_type = instance['InstanceType']
                state = instance['State']['Name']
                
                # Get instance name from tags
                name = "No Name"
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                            break
                
                print(f"Instance: {instance_id}")
                print(f"  Name: {name}")
                print(f"  Type: {instance_type}")
                print(f"  State: {state}")
                print("-" * 30)
        
        print(f"Total EC2 instances: {instance_count}")
        
    except Exception as e:
        print(f"Error listing EC2 resources: {e}")

def list_s3_resources(region):
    """List S3 buckets"""
    try:
        s3 = boto3.client('s3', region_name=region)
        
        print(f"\n=== S3 Buckets in {region} ===")
        response = s3.list_buckets()
        
        bucket_count = 0
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            created = bucket['CreationDate']
            
            # Check if bucket is in the specified region
            try:
                location = s3.get_bucket_location(Bucket=bucket_name)
                bucket_region = location.get('LocationConstraint') or 'us-east-1'
                
                if bucket_region == region:
                    bucket_count += 1
                    print(f"Bucket: {bucket_name}")
                    print(f"  Created: {created}")
                    print("-" * 30)
            except:
                continue  # Skip if can't access bucket location
        
        print(f"Total S3 buckets in {region}: {bucket_count}")
        
    except Exception as e:
        print(f"Error listing S3 resources: {e}")

def list_lambda_resources(region):
    """List Lambda functions"""
    try:
        lambda_client = boto3.client('lambda', region_name=region)
        
        print(f"\n=== Lambda Functions in {region} ===")
        response = lambda_client.list_functions()
        
        functions = response['Functions']
        for func in functions:
            name = func['FunctionName']
            runtime = func['Runtime']
            size = func['CodeSize']
            
            print(f"Function: {name}")
            print(f"  Runtime: {runtime}")
            print(f"  Code Size: {size} bytes")
            print("-" * 30)
        
        print(f"Total Lambda functions: {len(functions)}")
        
    except Exception as e:
        print(f"Error listing Lambda resources: {e}")

def list_dynamodb_resources(region):
    """List DynamoDB tables"""
    try:
        dynamodb = boto3.client('dynamodb', region_name=region)
        
        print(f"\n=== DynamoDB Tables in {region} ===")
        response = dynamodb.list_tables()
        
        tables = response['TableNames']
        for table_name in tables:
            table_info = dynamodb.describe_table(TableName=table_name)
            table = table_info['Table']
            
            status = table['TableStatus']
            item_count = table.get('ItemCount', 0)
            
            print(f"Table: {table_name}")
            print(f"  Status: {status}")
            print(f"  Items: {item_count}")
            print("-" * 30)
        
        print(f"Total DynamoDB tables: {len(tables)}")
        
    except Exception as e:
        print(f"Error listing DynamoDB resources: {e}")

def list_rds_resources(region):
    """List RDS instances"""
    try:
        rds = boto3.client('rds', region_name=region)
        
        print(f"\n=== RDS Instances in {region} ===")
        response = rds.describe_db_instances()
        
        instances = response['DBInstances']
        for db in instances:
            db_id = db['DBInstanceIdentifier']
            engine = db['Engine']
            status = db['DBInstanceStatus']
            db_class = db['DBInstanceClass']
            
            print(f"Database: {db_id}")
            print(f"  Engine: {engine}")
            print(f"  Status: {status}")
            print(f"  Class: {db_class}")
            print("-" * 30)
        
        print(f"Total RDS instances: {len(instances)}")
        
    except Exception as e:
        print(f"Error listing RDS resources: {e}")

def main():
    """Main function"""
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python aws_simple_lister.py <service> <region>")
        print("\nSupported services: ec2, s3, lambda, dynamodb, rds")
        print("Example: python aws_simple_lister.py ec2 us-east-1")
        sys.exit(1)
    
    service = sys.argv[1].lower()
    region = sys.argv[2]
    
    # Check AWS credentials
    try:
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print(f"Connected to AWS as: {identity.get('Arn', 'Unknown')}")
    except Exception as e:
        print("Error: Cannot connect to AWS. Please check your credentials.")
        print("Run 'aws configure' to set up your credentials.")
        sys.exit(1)
    
    # List resources based on service
    if service == 'ec2':
        list_ec2_resources(region)
    elif service == 's3':
        list_s3_resources(region)
    elif service == 'lambda':
        list_lambda_resources(region)
    elif service == 'dynamodb':
        list_dynamodb_resources(region)
    elif service == 'rds':
        list_rds_resources(region)
    else:
        print(f"Error: Unsupported service '{service}'")
        print("Supported services: ec2, s3, lambda, dynamodb, rds")
        sys.exit(1)
    
    print("\nDone!")

if __name__ == "__main__":
    main()