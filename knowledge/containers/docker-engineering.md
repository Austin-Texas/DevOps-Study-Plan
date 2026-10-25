# Docker, OCI, image delivery and container runtime engineering

## Architecture
Docker CLI → Docker Engine API → dockerd/containerd → OCI runtime (e.g. runc) → Linux namespaces/cgroups. **Image** is immutable layered content plus metadata; a **container** is an execution instance. Registries include Docker Hub, GHCR, ECR and GitLab Container Registry. A Kubernetes Pod is not the same as a Docker container.

## Reference commands
```bash
docker version
docker info
docker ps -a
docker images
docker inspect <container>
docker logs --tail=100 <container>
docker stats --no-stream
docker network ls
docker volume ls
docker system df
docker compose config
docker compose ps
```
Examples of correct repository names matter: `docker run mongodb` is not a reliable MongoDB image reference; the official MongoDB Hub image is commonly `mongo`. Ansible is typically a management tool, not a service you start by guessing `docker run ansible`. Always verify the image name, publisher, digest and supported usage.

## Build, run and registry
```bash
docker build -t example/app:dev .
docker run --rm --name sample -p 127.0.0.1:8080:80 nginx:stable
docker image inspect nginx:stable
docker login ghcr.io
docker tag example/app:dev ghcr.io/OWNER/app:dev
docker push ghcr.io/OWNER/app:dev
```
The run example binds to localhost; replace image and port mapping only after validating compatibility. Never store registry passwords in source control.

## Production design decisions
Prefer nonroot execution, health checks, least capabilities, bounded logs, explicit CPU/memory resources and pinned deployable digests. For supply chain, discuss SBOM, attestations, image signatures and runtime restrictions. Use multistage builds to reduce runtime surface.

## Troubleshooting tree
Cannot pull → name/tag/auth/DNS/TLS/rate limits. Container exits → entrypoint, logs, exit status, mount/permissions. Cannot reach service → bind interface, published port, bridge/network, host firewall, reverse proxy. Storage disappears → ephemeral write layer versus named/bind volumes.

## Deep questions
Explain overlay filesystem layers and copy-on-write; why a container can be running but unhealthy; differences between Compose orchestration and a Kubernetes control plane.

## Lab
Analyze a non-production Compose application read-only and write a deployment/rollback plan. Avoid restarting trading workloads or other production containers without explicit approval.
