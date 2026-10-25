# Guided DevOps Human-in-the-Loop study program

**Mode:** guided. **Environment:** Proxmox home lab, four-node Kubernetes, Linux, Windows, Docker, and GitHub/GitLab. No VM access is granted by this repository.

## Study tracks
Linux Administration; Kubernetes; CI/CD & GitOps; Security; Windows Administration; Docker; Networking; Terraform & Ansible. Monitoring/Prometheus/Grafana/Alertmanager/Operator is integrated into Kubernetes and observability labs.

## Operating workflow
1. Pick the first `Ready` assignment in `tasks.csv`.
2. Read the lab's objective, safety classification, prerequisites and expected evidence.
3. Learner executes commands **locally** and reviews all output before sharing. Never paste tokens, passwords, internal DNS names or public IPs if confidential.
4. A mentor reviews evidence, asks the learner to explain findings, and records Pass / Needs work in the tracker.
5. Changes are not performed until the human approval checklist is completed.
6. Advance only when the required lab is passed.

## Approval gates
- **GREEN**: read-only queries and local validation. Safe to run after reviewing commands.
- **AMBER**: test deployments, package installation, config changes. Human approval of commands, scope and rollback plan required.
- **RED**: production, deletion, reboot, firewall, SSH privileges, secrets, storage, destructive changes. Explicit separate approval with backup, impact and recovery plan. Never automate these in this learning repo.

## Starting LAB-001
From a machine with access to a **non-production** Kubernetes context:
```bash
kubectl config current-context
kubectl get nodes -o wide
kubectl get pods -A
kubectl get svc -A
kubectl get events -A --sort-by=.lastTimestamp
```
Or run `bash study-automation/scripts/lab001_collect.sh` to collect **locally** into `study-automation/evidence/`. The script does not upload results, connect to third-party systems, or mutate the cluster. Review and redact any evidence before publishing; this repository is public.
`python3 study-automation/scripts/lab001_validate.py path/to/collection-directory` checks that required files exist and that basic API calls succeeded. It **does not assert the cluster is healthy** or replace human review.

## GitHub Actions
The included `validate-study-kit.yml` validates study files only, never connects to lab machines. Workflow code uses minimal permissions. Lab outputs remain local by default.

## Tracking
Update `tasks.csv` through a reviewed pull request with status `Ready`, `In Progress`, `Review`, `Passed`, or `Needs Work`. Link a GitHub issue/PR and reference a **sanitized** evidence artifact if one is needed. Do not commit raw environment inventories, private logs or sensitive outputs.
