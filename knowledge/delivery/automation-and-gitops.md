# Git, CI/CD, Terraform, Ansible and GitOps — production delivery

## The delivery chain
Developer PR → unit/integration tests → SAST/SCA/secret checks → reproducible image build → SBOM/sign/scan → registry → approval → GitOps manifest change → Argo CD reconcile → health verification → rollback.

## Git commands
```bash
git status
git switch -c feature/example
git diff --check
git log --oneline --decorate -10
git fetch --prune
git diff origin/main...HEAD
```
Protect main, prefer reviewed PRs, avoid hardcoded secrets, and use immutable deployment artifacts.

## CI/CD design
Know runners, jobs, stages, caching vs artifacts, environment protection, manual gates, concurrency, OIDC workload identities, deployment locks, supply-chain attestations and rollback. Never use a self-hosted runner with broad host privileges on production as a default.

## Terraform/OpenTofu
Providers, resources, data sources, modules, state, plan/apply, drift, remote state locking, version pinning and testing.
```bash
terraform fmt -check
terraform validate
terraform plan -out=tfplan
terraform show -no-color tfplan
```
**Important:** `plan` may contact providers and can include sensitive values in local plan files. `apply` changes infrastructure and needs approval. Store state securely, with encryption, access restrictions and backups.

## Ansible
Inventory, roles, idempotence, handlers, facts, Vault, check mode and privilege escalation.
```bash
ansible-inventory -i inventory.ini --list
ansible-playbook --syntax-check -i inventory.ini site.yml
ansible-playbook --check --diff -i inventory.ini site.yml
```
Check mode is not universally side-effect-free; review modules and target inventory before any run.

## Kubernetes GitOps
- Helm: chart templates, values, release state.
- Kustomize: environment overlays and patches.
- Argo CD/Flux: continuously compare declarative Git state with live cluster; health, diff and sync.
- Restrict auto-sync / prune for sensitive environments. Manage CRDs, Secrets and ordering explicitly.

## Delivery troubleshooting
Failed build → source/toolchain/caching. Failed image pull → auth/digest. Argo CD out-of-sync → drift or render failure. Deployment unhealthy → readiness/probe/config/dependencies. Distinguish rollback of manifests from rollback of schema and data.

## Lab
Build a pipeline that runs static tests on a fake application and gates **all** infrastructure-changing stages behind an explicit manual review. Demonstrate one failed check and resolution.
