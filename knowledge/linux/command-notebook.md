# Linux Command Notebook

Living reference for the **DevOps Study Plan → Linux Administration → Commands** section. Every entry records the command, use case, flags/arguments, safety level, checks, and learning notes. Add new commands by following this format. Last expanded: 2026-11-13.

> **Safety:** Documentation examples are not blanket authorization to run commands. Treat destructive commands as study-only until the exact target, backup, change window, and rollback are reviewed. Never paste a destructive example into a production shell.

## 1. `su - hakkari`

**Category:** Users & identity  
**Risk:** LOW  
**Purpose:** Switch to user hakkari with a full login environment.

| Token / flag | Explanation |
| --- | --- |
| `su` | Switch user (no option). |
| `-` | Login-shell option: load the target user's environment and use their home directory. |
| `hakkari` | Target username; requires authorization and usually that user's password, unless invoked by root. |

**Notes / warnings:** Verify with whoami, pwd, and echo $HOME. On systems where direct su is restricted, use sudo -iu hakkari if authorized.

---

## 2. `cd ~/`

**Category:** Paths & navigation  
**Risk:** LOW  
**Purpose:** Change to the current user's home directory.

| Token / flag | Explanation |
| --- | --- |
| `cd` | Shell built-in: change directory. |
| `~/` | Tilde expands to the current user's home directory; the trailing / is a path separator, not a flag. |

**Notes / warnings:** ~/ on its own is a path expression, not a command. Use cd ~/ to navigate. cd ~hakkari/ targets hakkari's home when it exists.

---

## 3. `sudo rm -rf /home/username/`

**Category:** Files & deletion  
**Risk:** HIGH  
**Purpose:** Recursively and forcibly delete a user-home directory and everything beneath it.

| Token / flag | Explanation |
| --- | --- |
| `sudo` | Execute with elevated privileges after permission checks. |
| `rm` | Remove files and directories. |
| `-r` | Recursive: traverse and remove directories and their contents. |
| `-f` | Force: ignore nonexistent paths and suppress most confirmation prompts; it does not make deletion recoverable. |
| `/home/username/` | Absolute target path; placeholder must never be copied to a real system without deliberate validation. |

**Notes / warnings:** DANGEROUS / DESTRUCTIVE. Do not execute on production hosts or use for routine account removal. Preview the target with ls -ld -- /home/username/ and find /home/username/ -maxdepth 2 -print; confirm backups and rollback. For account management, review sudo userdel -r username separately after checking running processes and data ownership.

---

## 4. `sudo apt install ansible`

**Category:** Packages & Ansible  
**Risk:** MEDIUM  
**Purpose:** Install the Ansible package from configured APT repositories on Debian/Ubuntu.

| Token / flag | Explanation |
| --- | --- |
| `sudo` | Run package management with administrative privileges. |
| `apt` | APT package-management frontend. |
| `install` | Subcommand: resolve dependencies and install the named package. |
| `ansible` | Name of the software package; not a flag. |

**Notes / warnings:** Inspect proposed package changes before confirming. Usually run sudo apt update first if package indexes are stale; verify with ansible --version. On some systems use an isolated Python environment if a newer Ansible release is required.

---

## 5. `whoami`

**Category:** Inspection & verification  
**Risk:** LOW  
**Purpose:** Display the effective username of the current process.

| Token / flag | Explanation |
| --- | --- |
| `whoami` | Outputs current effective user; no flags here. |

**Notes / warnings:** Useful immediately after su - hakkari.

---

## 6. `pwd`

**Category:** Inspection & verification  
**Risk:** LOW  
**Purpose:** Print the current working directory.

| Token / flag | Explanation |
| --- | --- |
| `pwd` | Print working directory; no flags here. |

**Notes / warnings:** Confirm cd ~/ or a new login shell changed directory.

---

## 7. `ls -ld -- /home/username/`

**Category:** Inspection & verification  
**Risk:** LOW  
**Purpose:** Inspect a directory itself instead of listing its contents.

| Token / flag | Explanation |
| --- | --- |
| `ls` | List filesystem metadata. |
| `-l` | Long listing with permissions, ownership, and timestamps. |
| `-d` | List the directory itself rather than its contents. |
| `--` | Terminate options to prevent path names being interpreted as flags. |
| `/home/username/` | Directory to inspect. |

**Notes / warnings:** Read-only check before considering any deletion.

---

## 8. `find /home/username/ -maxdepth 2 -print`

**Category:** Inspection & verification  
**Risk:** LOW  
**Purpose:** Preview file and directory names within two levels of the target.

| Token / flag | Explanation |
| --- | --- |
| `find` | Walk a directory tree. |
| `/home/username/` | Search root. |
| `-maxdepth 2` | Limit traversal to depth two; deeper contents are not shown. |
| `-print` | Print each matched path. |

**Notes / warnings:** Read-only preview; it does not inventory deeply nested content. Avoid exposing sensitive filenames in shared logs.

---

## 9. `sudo apt update`

**Category:** Packages & Ansible  
**Risk:** MEDIUM  
**Purpose:** Refresh repository package indexes; does not itself upgrade installed packages.

| Token / flag | Explanation |
| --- | --- |
| `sudo` | Elevate privileges. |
| `apt` | Package management frontend. |
| `update` | Refresh the package metadata cache. |

**Notes / warnings:** On managed hosts, follow the organization's patch-control process.

---

## 10. `ansible --version`

**Category:** Packages & Ansible  
**Risk:** LOW  
**Purpose:** Print installed Ansible version and its runtime details.

| Token / flag | Explanation |
| --- | --- |
| `ansible` | Ansible CLI executable. |
| `--version` | Display version and exit. |

**Notes / warnings:** If not found, check installation and PATH.

## Template for new commands

### `example --option value`

- **Category:**
- **Risk:** Low / Medium / High
- **Purpose:**
- **Tokens and flags:** Explain each subcommand, option, argument, and shell operator.
- **Example:**
- **Expected output / verification:**
- **Warnings / production impact:**
- **Rollback or safer alternative:**
- **Date / lab notes:**

## References

- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/)
- [Linux man-pages](https://man7.org/linux/man-pages/)
- [Debian APT documentation](https://manpages.debian.org/apt)
- [Ansible documentation](https://docs.ansible.com/)
