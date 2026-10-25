# Kubernetes — control plane, node components and workloads

## Control-plane system components
- **kube-apiserver**: authenticated API entry point; authorization, admission and persistence via etcd.
- **etcd**: consistent key-value store; Raft quorum, snapshots and recovery.
- **kube-scheduler**: assigns unscheduled Pods to nodes using filter and score plugins.
- **kube-controller-manager**: reconciliation loops (Deployment/ReplicaSet, endpoints, nodes and more).
- **cloud-controller-manager**: cloud integration when applicable.

## Node system components
- **kubelet**: realizes PodSpecs and reports node/Pod status.
- **CRI runtime**: containerd or CRI-O; OCI runtime executes containers.
- **kube-proxy**: Service datapath implementation where installed; some eBPF CNIs replace it.
- **CNI**: Pod networking, often plugins such as Cilium, Calico or Flannel.
- **CSI**: storage lifecycle; **CoreDNS** is typically a cluster add-on.

## Pod creation data path
`kubectl apply` → API authentication/authorization/admission → object persisted → Deployment controller creates ReplicaSet → ReplicaSet creates Pods → scheduler binds Pod to node → kubelet pulls image through runtime → CNI configures Pod networking → probes & conditions determine readiness → Service EndpointSlices include ready endpoints.

## Kubernetes API resources (not background daemons)
Workloads: Pods, Deployments, ReplicaSets, DaemonSets, StatefulSets, Jobs, CronJobs. Config: ConfigMaps, Secrets, Namespace, LimitRange, ResourceQuota. Policies: NetworkPolicy, PodDisruptionBudget, PriorityClass, Role, ClusterRole, RoleBinding, ClusterRoleBinding, ServiceAccount. Extensions: CRDs, admission webhooks, ValidatingAdmissionPolicy, Operators.

Pod naming is immutable. To create another Pod from a YAML template: `cp pods/pod-template.yaml pods/newpod.yaml`, edit `metadata.name` in the copy, then `kubectl apply -f pods/newpod.yaml`. Do not attempt to rename a live Pod or override names with unsupported flags.

## Read-only commands
```bash
kubectl config current-context
kubectl get nodes -o wide
kubectl get pods -A -o wide
kubectl get deployments,daemonsets,statefulsets -A
kubectl get events -A --sort-by=.lastTimestamp
kubectl get --raw='/readyz?verbose'
kubectl api-resources
kubectl describe pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace> --previous
```

## Failures
Pending Pod: constraints, unavailable resources, taints, PVC binding, scheduling Events. CrashLoopBackOff: process exit, OOM, probes, config, dependencies. NotReady node: kubelet, CRI, CNI, disk pressure and connectivity. API unavailability: front-end LB, certs, admission latency, etcd quorum or storage.

## Senior design exercise
Compare a one-control-plane four-node lab to an HA topology with three control-plane nodes. Define failure domains, quorum, backup strategy, upgrade sequence, RPO and RTO. Do not assume your current four nodes have any particular roles until verified.
