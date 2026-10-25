# DevOps security and senior troubleshooting (not a standalone cybersecurity track)

## Minimum platform security
IAM least privilege and federation, TLS/cert lifecycle, secrets rotation, image provenance, RBAC, namespace isolation, admission policy, NetworkPolicy, hardened runner identities and audit trails. Do not put access tokens, kubeconfigs, SSH keys or private IP inventories in a public repository.

## Cross-layer incident workflow
1. State impact and timeline; identify last known-good condition.
2. Check deployment changes, infrastructure events and blast radius.
3. Follow the request path: DNS → TLS → load balancer → Service → Pod → app dependencies → database/storage.
4. Correlate logs, metrics, traces and events; identify strongest evidence.
5. Propose lowest-risk mitigation with explicit operator approval.
6. Confirm recovery with synthetic checks and SLO metrics.
7. Produce blameless postmortem with follow-up actions.

## Diagnostic cheat sheet
```bash
# Kubernetes
kubectl get nodes -o wide
kubectl get pods -A
kubectl get events -A --sort-by=.lastTimestamp
kubectl describe pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace> --previous

# Linux
systemctl --failed
journalctl -p err -b --no-pager
ss -lntup
df -h
free -h

# Docker
docker ps -a
docker inspect <container>
docker logs --tail=100 <container>
```

## Failure signatures
- Pending: scheduler constraint, quota, node capacity, storage
- OOMKilled: memory pressure/limit vs application allocation
- CrashLoopBackOff: process crashes, probes, missing dependencies
- 503: healthy backend count, readiness, endpoints, ingress/gateway
- DNS intermittency: CoreDNS, upstream, timeout, CNI path
- PVC Pending: CSI, storage class, quota, topology
- Pipeline succeeds but app fails: distinguish build artifact from deployed digest, runtime config and health checks

## Human approval matrix
GREEN: only read status/logs and run local syntax checks. AMBER: install tool/deploy to disposable test namespace after review. RED: production, deletion, credential/privilege/firewall/storage changes require explicit scoped signoff, backup/rollback and verification.
