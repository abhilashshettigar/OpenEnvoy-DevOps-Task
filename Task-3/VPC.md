## VPC Setup Steps
1. Plan the CIDR Range and Naming Conventions:

    - Choose a non-overlapping, private IPv4 CIDR (e.g., 10.0.0.0/16). This provides a scalable address space and avoids future conflicts with other networks (on-premises VPN, peering, etc.).

    - Establish a logical naming convention for all resources (VPCs, subnets, route tables, etc.) to maintain clarity in larger environments.

2. Create the VPC:

    - In AWS Console or via CLI, create a VPC using the planned CIDR block (example: 10.0.0.0/16).

    - Disable “auto-assign public IPv4 address” by default for all subnets. Only assign where absolutely needed (e.g., web servers).

3. Design Subnets:

    - Divide the VPC into public and private subnets across at least two Availability Zones for high availability. Use smaller CIDRs per subnet (like /24, 10.0.1.0/24 - public, 10.0.2.0/24 - private).

    - Public subnets are for resources needing internet access (e.g., load balancers, bastion hosts); private subnets are for internal services and databases.

4. Add Internet Gateway and Attach to VPC:

    - Create and attach an Internet Gateway to the VPC. This enables internet access for public subnets.

5. Route Tables:

    - Configure a separate route table for the public subnet, with a 0.0.0.0/0 route pointing to the Internet Gateway.

    - Use a separate route table for private subnets. By default, they have no internet route. Optionally, add a NAT Gateway to allow outbound internet access from private subnets (for updates, package installs, etc.).

    - Always associate subnets with the correct route tables explicitly to avoid confusion down the line.

6. Network ACLs and Security Groups:

    - Fine-tune Network ACLs for coarse-grained subnet-level controls if required, but rely primarily on security groups for “stateful” and granular traffic control at the instance level.

    - Create minimal security group inbound/outbound rules required for your specific application (e.g., allow TCP 80/443 for the public web server only).

7. (Optional) VPC Endpoints:

    - Use VPC Endpoints (Gateway or Interface) to privately connect to AWS services like S3, DynamoDB, etc., without traversing the internet.