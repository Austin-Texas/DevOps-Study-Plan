# Prometheus, Alertmanager, Grafana and SRE

## What the stack does
- **Prometheus Server:** scrapes metrics targets and stores time series; executes PromQL and evaluates alert rules.
- **Prometheus Operator:** reconciles CRDs such as Prometheus, Alertmanager, ServiceMonitor, PodMonitor and PrometheusRule.
- **Alertmanager:** groups, routes, silences and deduplicates alerts to receivers.
- **Grafana:** dashboards and queries to metrics/logs/traces backends, but not the Prometheus storage engine.
- **Exporters:** node-exporter and kube-state-metrics expose different kinds of data.

Architecture: exporter/application metric endpoint ← scrape by Prometheus → time series / rule evaluations → Alertmanager notification. Grafana queries Prometheus to visualize metrics.

## Read-only cluster inventory
```bash
kubectl get pods -A | grep -Ei 'prometheus|grafana|alertmanager'
kubectl get crd | grep monitoring.coreos.com
kubectl get servicemonitors,podmonitors,prometheusrules -A
kubectl get svc -A | grep -Ei 'prometheus|grafana'
```
CRD queries may error if the operator is not installed. Do not treat the error as proof the cluster is broken.

## Basic PromQL
```promql
up
sum(rate(container_cpu_usage_seconds_total{container!=""}[5m])) by (namespace)
sum by (node) (kube_pod_status_phase{phase="Running"})
rate(http_requests_total[5m])
```
Some metrics require appropriate exporters and labels; query availability is deployment-dependent.

## SRE fundamentals
SLI = measure of service health (e.g., successful requests / total requests). SLO = target for SLI over a window. Error budget = allowed unreliability. Understand alert fatigue, burn-rate alerts, cardinality, retention, storage pressure, HA, RPO/RTO and missing telemetry.

## Senior lab
Plan kube-prometheus-stack; define ServiceMonitor selectors, retention, PVC sizing, ingress/TLS, credentials and alert routing. After change approval, create dashboards for node CPU/memory, deployment availability and application latency. Simulate a failure in a disposable test workload and validate detection and recovery.
