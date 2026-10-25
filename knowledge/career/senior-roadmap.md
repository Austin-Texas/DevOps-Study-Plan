# Senior DevOps / AWS platform engineering roadmap

## Goal
Build the capabilities associated with senior/staff cloud platform or SRE positions. **$250k/year is a compensation aspiration, not an expected salary**: base versus bonus/equity, region, employer, on-call, interview readiness and demonstrated outcomes matter.

## Learning sequence
1. Linux, Git, scripting, networking fundamentals (focus on application/cloud operations, not Cisco certification).
2. Docker, build systems, Kubernetes API and internals.
3. CI/CD with tests, immutable artifacts, security gates.
4. Terraform/OpenTofu, Ansible, GitOps and reproducible infrastructure.
5. AWS: VPC/IAM/ECS/EKS/S3/RDS/Route 53/observability/cost.
6. Prometheus/Grafana/Alertmanager, SLOs, incident response, DR.
7. Senior architecture: HA, multi-account, multi-cluster, platform templates and technical design reviews.

## Portfolio capstones
**Capstone A — Homelab platform:** Proxmox + four-node Kubernetes, GitHub/GitLab pipeline, Argo CD, Helm, monitoring, least-privilege and recoverable storage. Keep existing production trading systems isolated.

**Capstone B — AWS platform:** Provision two-AZ private application architecture with Terraform and protected CI identity. Evaluate ECS vs EKS, budget safeguards and operational burdens.

**Capstone C — Reliability:** Define SLIs/SLOs, generate load, alert on burn rate, stage a controlled outage, restore from backup, write incident report.

**Capstone D — Security-by-design:** Signed images, SBOM, vulnerability scanning, workload identity, secrets and policy-as-code — all relevant to DevOps delivery.

## Interview evidence
For each project retain an architecture decision record (requirements/options/tradeoffs), diagrams, reproducible repo, tests, metrics, failure injection results, postmortem and cost/security review. Quantify outcomes where measured, never fabricate metrics.

## Mastery rubric
1. Can describe architecture and components.
2. Can implement from clean infrastructure.
3. Can explain tradeoffs and verify operations.
4. Can isolate failures under time constraints.
5. Can restore safely and teach the design to others.

Review progress monthly. Favor deep mastery and documented production-style decisions over collecting unrelated tools.
