## Securing EC2–Internet Communication
1. Use Tight Security Groups:

    - Apply “least privilege” principles: open only required inbound ports (e.g., 80/443 from 0.0.0.0/0 for web servers).

    - Restrict SSH/RDP (22/3389) for admins only, preferably via a bastion/jump host, or by whitelisting corporate/public IPs.

2. Leverage Private Subnets + NAT for Outbound:

    - Place sensitive workloads (databases, app servers) in private subnets with no direct internet access.

    - Deploy a managed NAT Gateway in a public subnet for these resources to initiate outbound connections (patching, package install) without being exposed inbound.

3. Network Access Control Lists (NACLs):

    - Use NACLs as a secondary defense (default allows all; consider locking down if threat model requires it).

4. Patch and Monitor:

    - Regularly update EC2 AMIs and packages.

    - Enable AWS CloudTrail, GuardDuty, and configure security monitoring for network flows and access attempts.

5. Encryption and IAM:

    - Use TLS (1.2+), strong ciphers for data in transit.

    - Restrict IAM permissions for EC2 and VPC resources using roles, policies, and MFA for interactive access