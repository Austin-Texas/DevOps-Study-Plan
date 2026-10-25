# AWS — production DevOps architecture and design decisions

## Baseline reference architecture
Route 53 / CloudFront / WAF (as needed) → ALB in public subnets → workloads in private subnets (EKS/ECS or EC2) → private databases (RDS). VPC spans AZs; subnet and route table design controls traffic. ECR stores images; S3 stores artifacts/backups; IAM grants scoped access; CloudWatch and CloudTrail provide operational/audit visibility.

## Concepts a senior engineer must defend
1. **VPC:** CIDRs, subnet sizes, public/private routing, IGW/NAT gateway, endpoints, NACL vs stateful Security Groups.
2. **Identity:** IAM roles, least privilege, AWS Organizations, SCPs, IAM Identity Center, OIDC federation for CI jobs; never commit keys.
3. **Compute:** EC2 vs ECS/Fargate vs EKS; operational overhead, availability and cost tradeoffs.
4. **Data:** EBS vs EFS vs S3; RDS Multi-AZ, snapshots, encryption, recovery testing.
5. **High availability:** AZ spread, scaling, health checks, LB behavior, failure injection with rollback.
6. **Observability:** CloudWatch metrics/logs/alarms, CloudTrail audit history and trace propagation.
7. **Cost:** NAT gateway data processing, inter-AZ traffic, idle load balancers, right sizing, savings plans and budgets.
8. **Multi-account:** separate sandbox/nonprod/prod, centralized logging and governance.

## Read-only CLI discovery (requires authenticated AWS CLI)
```bash
aws sts get-caller-identity
aws configure list
aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,CidrBlock,IsDefault]' --output table
aws ec2 describe-subnets --query 'Subnets[*].[SubnetId,VpcId,AvailabilityZone,CidrBlock]' --output table
aws eks list-clusters --output table
aws s3api list-buckets --query 'Buckets[*].Name' --output table
```
**Caution:** Even read-only inventory can reveal sensitive IDs/names. Redact before sharing. Do not run provisioning until region, account, cost budget and impact are approved.

## AWS deployment example decision record
Requirements: 99.9% availability, predictable traffic, small engineering team, containerized web API. Compare ECS Fargate to EKS: EKS offers Kubernetes ecosystem and portability but adds control-plane and day-2 complexity/cost. If no Kubernetes-specific requirements exist, evaluate ECS first rather than assuming EKS is always better.

## Design exercise
Draw dev/staging/prod boundaries; design egress, secrets, IaC state storage, pipeline authentication, backups, alarms, IAM boundaries and monthly cost guardrails. Prepare a threat/risk and rollback review.
