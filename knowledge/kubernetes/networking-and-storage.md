# Kubernetes network and storage datapaths

## Networking concepts
Pod IPs must route between nodes according to the cluster network model. Services present virtual endpoints backed by EndpointSlices; CoreDNS answers cluster service names. Traffic may traverse iptables/nftables, IPVS in supported legacy deployments or eBPF depending on implementation. Separate Service routing from Ingress/Gateway HTTP routing and external load balancing.

Network data path to explain:
Client → DNS → external load balancer / Gateway → Kubernetes Service → eligible EndpointSlice backend → Pod network interface → application port.

## Read-only diagnostics
```bash
kubectl get svc,endpointslices -A
kubectl get ingress,ingressclass -A
kubectl get networkpolicy -A
kubectl get pods -n kube-system -o wide
kubectl describe svc <service> -n <namespace>
kubectl get pod <pod> -n <namespace> -o yaml
```
Ingress requires an Ingress controller. Gateway API resources need CRDs and an implementation. NetworkPolicy needs a CNI enforcing policies; YAML alone does not guarantee enforcement.

## Storage
`PVC` requests storage; `StorageClass` selects a provisioner; `PV` represents provisioned backing storage; CSI controls allocation, attach, stage and publish as applicable. Access modes RWO/RWX/RWOP describe requested access semantics, not magical multiwriter safety.

```bash
kubectl get storageclass
kubectl get pv
kubectl get pvc -A
kubectl describe pvc <claim> -n <namespace>
```

## Senior failures
DNS returns address but app fails → test TCP/TLS and backing EndpointSlices. Service has no backend → verify selectors/readiness. Node-to-node traffic fails → CNI routes, firewall, encapsulation/MTU. PVC Pending → StorageClass, provisioner, node topology, quota. Stateful workloads require consistent application backups, not only PV snapshots.

## Exercise
Trace one request end-to-end, write a packet-path diagram and prove the exact failure layer with read-only output.
