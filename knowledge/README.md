# Senior DevOps / AWS / Platform Engineering Knowledge Base

**Target:** deep production engineering capability toward senior/staff roles and a long-term $250k total compensation goal. Salary is not guaranteed; it depends on market, location, specialization, interview performance, and experience.

This is **not** just a checklist. Each chapter includes architecture, why it matters, commands, failure modes, design tradeoffs, an exercise and assessment questions. The existing website is preserved; these documents are Markdown content for future website integration.

## Curriculum (18 sections)
1. Linux and systems administration
2. Windows infrastructure for DevOps
3. Git and version control
4. Docker and container engineering
5. Kubernetes control-plane architecture
6. Kubernetes workloads and administration
7. Kubernetes networking
8. AWS infrastructure and architecture
9. CI/CD engineering
10. Terraform / OpenTofu and infrastructure as code
11. Ansible and operational automation
12. GitOps, Helm and platform engineering
13. Prometheus, Alertmanager, Grafana and observability
14. Infrastructure and software delivery security
15. SRE, resilience and incident operations
16. Internal developer platforms and multi-cluster operations
17. Senior architecture design and tradeoffs
18. Advanced cross-system troubleshooting

### Excluded
Standalone cybersecurity/SOC and Cisco-specific routing certifications or labs. **Retained**: the security and networking required to run DevOps systems (IAM, TLS, RBAC, VPC, CNI, supply chain).

## Learning evidence standard
For each chapter: explain the data path, draw the architecture, execute read-only commands, predict outcomes, inspect failure modes, write a runbook, and defend a design decision. Never run destructive examples without an approved isolated lab and rollback plan.

## Content index
- [Linux operations](linux/senior-linux-operations.md)
- [Docker and OCI](containers/docker-engineering.md)
- [Kubernetes internals](kubernetes/control-plane-and-workloads.md)
- [Kubernetes production networking](kubernetes/networking-and-storage.md)
- [AWS architecture](aws/aws-production-architecture.md)
- [CI/CD, Terraform, Ansible and GitOps](delivery/automation-and-gitops.md)
- [Monitoring and SRE](observability/prometheus-and-sre.md)
- [DevOps security and incident diagnostics](operations/security-and-troubleshooting.md)
- [Roadmap and portfolio](career/senior-roadmap.md)

## Existing automation
A separate draft pull request contains guided HITL lab collection scripts. Review it separately before using those scripts. This branch does not deploy to any VM, alter AWS resources, or modify production applications.

## Upstream documentation
https://kubernetes.io/docs/ ; https://docs.aws.amazon.com/ ; https://docs.docker.com/ ; https://docs.gitlab.com/ci/ ; https://developer.hashicorp.com/terraform/docs ; https://docs.ansible.com/ ; https://argo-cd.readthedocs.io/
