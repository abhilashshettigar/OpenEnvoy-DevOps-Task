# Task-2: EC2 Instance Setup with Nginx Web Server

## Overview
This task involves creating an EC2 instance, installing Nginx web server, and configuring it to display a custom "Hello, DevOps!" webpage. We'll use AWS EC2 Connect for secure access.

## Prerequisites
- AWS account with EC2 access
- Basic knowledge of Linux commands
- Web browser for accessing the web server
- AWS Management Console access

## Step-by-Step Guide

### Step 1: Create EC2 Instance

#### 1.1 Launch EC2 Instance via AWS Console
1. **Sign in to AWS Management Console**
   - Go to [AWS Console](https://console.aws.amazon.com/)
   - Sign in with your AWS account credentials

2. **Navigate to EC2 Service**
   - In the AWS Console search bar, type "EC2"
   - Click on "EC2" service

3. **Launch EC2 Instance**
   - Click "Launch Instance" button

4. **Configure Instance Details**
   - **Name**: Enter "DevOps-WebServer"
   - **Application and OS Images**: Select "Amazon Linux 2023 (kernel-6.1)"
   - **Architecture**: Choose "x86"
   - **Instance type**: Select "t2.micro" 
   - **Key pair**:  Procced without any keys

5. **Configure Security Group**
   - Click Edit with "Create security group" [Make sure you keep other details to the Default e.g VPC, Subnet, AZ]
   - **Security group name**: "DevOps-WebServer-SG"
   - **Description**: "Security group for DevOps web server"
   - **Inbound rules**: Add the following rules:
     - **Type**: SSH, **Port**: 22, **Source**: Custom (13.233.177.0/29) #IP range EC2_INSTANCE_CONNECT from ip-ranges.json
     - **Type**: HTTP, **Port**: 80, **Source**: Anywhere-IPv4 (0.0.0.0/0)
     - **Type**: HTTPS, **Port**: 443, **Source**: Anywhere-IPv4 (0.0.0.0/0)
   - **Outbound rules**: Configure restrictive outbound access:
     - **Type**: HTTP, **Port**: 80, **Destination**: 0.0.0.0/0 (for package updates)
     - **Type**: HTTPS, **Port**: 443, **Destination**: 0.0.0.0/0 (for secure connections)

6. **Configure Storage**
   - **Volume type**: General Purpose SSD (gp3)
   - **Size**: 8 GiB (default)
   - **Delete on termination**: Checked (recommended)

7. **Launch Instance**
   - Review your configuration
   - Click "Launch instance"
   - Wait for instance to reach "Running" status

### Step 2: Connect to EC2 Instance

#### 2.1 Using AWS EC2 Connect (Recommended)
1. **Navigate to EC2 Dashboard**
   - In AWS Console, go to EC2 service
   - Click on "Instances" in the left sidebar

2. **Select Your Instance**
   - Find your "DevOps-WebServer" instance
   - Ensure it shows "Running" status
   - Select the instance by clicking the checkbox

3. **Connect to Instance**
   - Click "Connect" button at the top
   - Choose "EC2 Instance Connect" tab
   - Keep default username: "ec2-user"
   - Click "Connect" button

4. **Browser-Based Terminal**
   - A new browser tab will open with terminal access
   - You're now connected to your EC2 instance
   - No SSH keys or PEM files needed

### Step 3: Install and Configure Nginx

#### 3.1 Install Nginx
```bash
# Install Nginx
sudo yum install nginx -y

# Start Nginx service
sudo systemctl start nginx

# Enable Nginx to start on boot
sudo systemctl enable nginx

# Check Nginx status
sudo systemctl status nginx
```

### Step 4: Create Custom Webpage

#### 4.1 Create HTML File
```bash
cd /usr/bin/nginx/
mv index.html index.html@bkp
vi index.html
# Create custom HTML file
<html>
<h1>Hello, DevOps!</h1>
</html>
```

### Step 5: Verify Installation

#### 5.1 Check Nginx Configuration
```bash
# Test Nginx configuration
sudo nginx -t

# Reload Nginx Configuration
nginx -s reload

```

#### 5.2 Access the Webpage
1. **Get Your EC2 Instance's Public IP**
   - In AWS Console, go to EC2 → Instances
   - Find your "DevOps-WebServer" instance
   - Copy the "Public IPv4 address" from the instance details

2. **Access the Webpage**
   - Open a new browser tab
   - Navigate to: `http://YOUR_EC2_PUBLIC_IP`
   - Example: `http://3.250.123.45`

3. **Verify the Webpage**
   - You should see the "Hello, DevOps!" webpage
