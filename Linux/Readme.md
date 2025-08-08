# 🐧 Linux Core Topics to Know (Structured Checklist)

| **Area**            | **Key Topics**                                   | **Must-Know Commands / Concepts**                         |
|---------------------|--------------------------------------------------|------------------------------------------------------------|
| **File & Directory**| Navigation, permissions, hidden files            | `ls`, `cd`, `chmod`, `chown`, `find`, `stat`              |
| **User Management** | Create users, groups, sudo, shell types          | `useradd`, `usermod`, `groupadd`, `/etc/passwd`           |
| **Process Mgmt**    | Run, kill, prioritize, background/foreground     | `ps`, `top`, `kill`, `nice`, `jobs`, `bg`, `fg`           |
| **File Permissions**| rwx, numeric & symbolic modes, umask             | `chmod`, `chown`, `umask`, `getfacl`, `setfacl`           |
| **Networking**      | Check ports, services, firewall basics           | `netstat`, `ss`, `curl`, `ping`, `iptables`, `nc`         |
| **Package Mgmt**    | Install, remove, update packages                 | `apt`, `yum`, `dnf`, `rpm`, `dpkg`                        |
| **System Services** | Enable/disable/start/stop services               | `systemctl`, `service`, `journalctl`                      |
| **Logs & Monitoring**| Syslogs, auth logs, disk usage, uptime          | `tail`, `journalctl`, `du`, `df`, `uptime`, `top`         |
| **Scripting**       | Bash basics: loops, conditionals, arguments      | `if`, `for`, `$1`, `case`, `functions`                    |
| **Crontab & Jobs**  | Scheduling, timing syntax                        | `crontab -e`, `at`, `cron`                                |

Linux Core Topics for DevOps
1️⃣ Linux Basics & Filesystem
Directory structure (/bin, /etc, /var, /home, /tmp, /opt)

Navigation commands: ls, pwd, cd, tree

File operations: touch, cat, less, head, tail, cp, mv, rm

File types: regular, directory, symbolic links (ln, ln -s)

2️⃣ User & Permissions Management
useradd, usermod, passwd, deluser

Groups: groupadd, gpasswd

File permissions (rwx), chmod, chown, umask

Special permissions: setuid, setgid, sticky bit

Non-interactive shells for service accounts (/sbin/nologin)

3️⃣ Process & Resource Management
View processes: ps, top, htop, pgrep

Kill/stop processes: kill, killall

Priorities: nice, renice

System monitoring: uptime, free, vmstat, iostat

4️⃣ Package & Service Management
Package managers:

Debian/Ubuntu: apt, dpkg

RHEL/CentOS: yum, dnf, rpm

Service management: systemctl, service

Enable/disable at boot: systemctl enable|disable

5️⃣ Networking
IP config: ip addr, ifconfig

Connectivity: ping, curl, wget

Port scanning: netstat, ss

DNS lookup: dig, nslookup

SSH & SCP: ssh user@host, scp file user@host:/path

6️⃣ Logs & Monitoring
Log locations: /var/log/

Common logs: syslog, auth.log, messages

Viewing logs: less, tail -f, journalctl

Filtering logs: grep, awk, sed

7️⃣ Shell Scripting & Automation
Variables, conditionals (if, case)

Loops (for, while, until)

Functions and script arguments ($1, $2)

Redirections: >, >>, <, |, 2>

Cron jobs: crontab -e

8️⃣ File Search & Text Processing
Search: find, locate

Content search: grep, egrep, fgrep

Text processing: cut, sort, uniq, wc

Replace/edit: sed, awk

9️⃣ Storage & Disk Management
Disk usage: df, du

Mounting: mount, umount

Partition tools: fdisk, lsblk

Swap management

🔟 Linux in DevOps Context
Linux in Docker (container base images)

Linux in Kubernetes nodes

Using Ansible on Linux servers

Environment variables for CI/CD pipelines

Permissions for deployment automation

✅ Tip: In DevOps interviews, they often check

File permissions (chmod, chown)

Log analysis (grep, awk)

Service management (systemctl)

SSH and SCP usage

Simple Bash scripting

