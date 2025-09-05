# AWS Resource Lister

A Python script that lists AWS resources across different services in a specified region. This tool helps you quickly inventory your AWS resources for a given region and service.

## Features

- **Multi-Service Support**: Lists resources from EC2, S3, Lambda, DynamoDB, and RDS
- **Region-Specific**: Filter resources by AWS region
- **Detailed Information**: Shows comprehensive details for each resource type
- **Error Handling**: Graceful error handling with informative messages
- **AWS Credential Validation**: Verifies AWS credentials before execution

## Supported Services

- **EC2**: Lists instances with name, type, and state information
- **S3**: Lists buckets in the specified region with creation dates
- **Lambda**: Lists functions with runtime and code size information
- **DynamoDB**: Lists tables with status and item count
- **RDS**: Lists database instances with engine, status, and class information

## Prerequisites

- Python 3.6 or higher
- AWS CLI configured with appropriate credentials
- Required AWS permissions for the services you want to list

## Installation

### Step 1: Set up Virtual Environment (Recommended)

It's recommended to use a virtual environment to isolate project dependencies:

**Create virtual environment:**
```bash
# Navigate to the project directory
cd Task-4/

# Create virtual environment
python3 -m venv aws_resource_lister_env

# Or using virtualenv (if installed)
virtualenv aws_resource_lister_env
```

**Activate virtual environment:**

*On macOS/Linux:*
```bash
source aws_resource_lister_env/bin/activate
```

*On Windows:*
```bash
# Command Prompt
aws_resource_lister_env\Scripts\activate

# PowerShell
aws_resource_lister_env\Scripts\Activate.ps1
```

**Deactivate virtual environment (when done):**
```bash
deactivate
```

### Step 2: Install Dependencies

With your virtual environment activated, install the required dependencies:

```bash
pip install -r requirement.txt
```

Or install boto3 directly:
```bash
pip install boto3
```

### Step 3: Configure AWS Credentials

```bash
aws configure
```
   
Or set environment variables:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

## Usage

### Basic Syntax
```bash
python aws_resource_lister.py <service> <region>
```

### Examples

**List EC2 instances in us-east-1:**
```bash
python aws_resource_lister.py ec2 us-east-1
```

**List S3 buckets in eu-west-1:**
```bash
python aws_resource_lister.py s3 eu-west-1
```

**List Lambda functions in ap-southeast-1:**
```bash
python aws_resource_lister.py lambda ap-southeast-1
```

**List DynamoDB tables in us-west-2:**
```bash
python aws_resource_lister.py dynamodb us-west-2
```

**List RDS instances in ca-central-1:**
```bash
python aws_resource_lister.py rds ca-central-1
```

## Output Examples

### EC2 Instances
```
Connected to AWS as: arn:aws:iam::123456789012:user/your-username

=== EC2 Instances in us-east-1 ===
Instance: i-1234567890abcdef0
  Name: Web Server
  Type: t3.micro
  State: running
------------------------------
Instance: i-0987654321fedcba0
  Name: Database Server
  Type: t3.small
  State: stopped
------------------------------
Total EC2 instances: 2
```

### S3 Buckets
```
=== S3 Buckets in us-east-1 ===
Bucket: my-app-bucket
  Created: 2023-01-15 10:30:00+00:00
------------------------------
Bucket: backup-storage
  Created: 2023-02-20 14:45:00+00:00
------------------------------
Total S3 buckets in us-east-1: 2
```

## Required AWS Permissions

The script requires the following AWS permissions for each service:

### EC2
- `ec2:DescribeInstances`

### S3
- `s3:ListAllMyBuckets`
- `s3:GetBucketLocation`

### Lambda
- `lambda:ListFunctions`

### DynamoDB
- `dynamodb:ListTables`
- `dynamodb:DescribeTable`

### RDS
- `rds:DescribeDBInstances`

### STS (for credential validation)
- `sts:GetCallerIdentity`

## Error Handling

The script includes comprehensive error handling:

- **Credential Validation**: Checks AWS credentials before execution
- **Service-Specific Errors**: Handles errors for each AWS service gracefully
- **Permission Errors**: Provides clear messages for insufficient permissions
- **Network Errors**: Handles connectivity issues

## Troubleshooting

### Common Issues

1. **"Cannot connect to AWS"**
   - Run `aws configure` to set up credentials
   - Check if AWS credentials are properly configured
   - Verify AWS CLI installation

2. **"Access Denied" errors**
   - Ensure your AWS user/role has the required permissions
   - Check IAM policies for the services you're trying to access

3. **"No such file or directory"**
   - Make sure you're running the script from the correct directory
   - Verify Python is installed and accessible

4. **Empty results**
   - Verify the region has resources for the specified service
   - Check if resources exist in the specified region

5. **Virtual Environment Issues**
   - Make sure you've activated the virtual environment before running the script
   - Verify that dependencies are installed in the correct environment
   - Check that Python is pointing to the virtual environment's Python

### Debug Mode

For debugging, you can modify the script to add more verbose logging or run with Python's debug mode:

```bash
python -u aws_resource_lister.py ec2 us-east-1
```

## Contributing

To extend this script:

1. Add new service functions following the existing pattern
2. Update the main function to handle new services
3. Add appropriate error handling
4. Update this README with new service information

## License

This script is provided as-is for educational and operational purposes.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify AWS credentials and permissions
3. Ensure you're using the correct region and service names
