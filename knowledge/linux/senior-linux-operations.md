# Linux systems administration — senior notes and commands

## Architecture / mental model
Application request → process → syscalls → kernel scheduler, memory subsystem, VFS, network stack → hardware or hypervisor. PID 1 (`systemd` on common distributions) manages services and dependencies; journal logs help correlate failures. Containers share the host kernel, unlike virtual machines.

## Operational baseline (read-only)
```bash
uname -a
cat /etc/os-release
uptime
systemctl --failed
systemctl status ssh --no-pager
journalctl -p warning -b --no-pager | tail -50
free -h
vmstat 1 5
df -hT
lsblk -f
ip -brief address
ip route
ss -tulpn
```
*Interpretation:* `load average` is runnable + uninterruptible task demand, **not CPU percentage**. `free` includes reclaimable cache; use `available`, swap, PSI and OOM evidence. Disk space and inode exhaustion are different (`df -h` versus `df -i`).

## Processes, systemd, failure isolation
```bash
ps aux --sort=-%cpu | head
systemctl list-units --type=service --state=running
systemctl cat ssh
journalctl -u ssh --since '1 hour ago' --no-pager
dmesg --level=err,warn | tail -50
```
Service crash approach: identify unit → exit code → last logs → dependency failures → port conflicts → permissions → resource constraints. Do not blindly restart before capturing evidence.

## Network diagnostics
```bash
getent hosts example.com
resolvectl status
curl -I --max-time 5 https://example.com
ip -s link
ss -tnp
tracepath 1.1.1.1
```
Distinguish DNS failure, routing failure, TCP failure, TLS failure and HTTP 5xx. Avoid treating an ICMP ping as proof an application works.

## Storage and permissions
Study VFS, mount namespaces, inode exhaustion, file descriptors, LVM/ZFS, NFS, iSCSI, quotas, backups and restore tests. `chmod`, `chown`, ACLs and Linux capabilities are separate mechanisms. Avoid using 777 permissions as a workaround.

## Design review
- How do you determine whether a VM is CPU, memory, disk-I/O or network constrained?
- What would you capture *before* restarting a malfunctioning service?
- How does a systemd restart policy interact with an application crash loop?

## Lab
Collect a sanitized host inventory, classify all failed units, and produce a root-cause hypothesis with validation evidence. Changes require human approval.
