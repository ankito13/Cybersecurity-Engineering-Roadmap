Cybersecurity Engineering Roadmap: Level 0 Foundation

This repository tracks my hands-on technical progression into Platform Security and Cloud Engineering. The Level 0 deliverables focus on core infrastructure fundamentals: Linux command-line operations, OS automation, network socket programming, and cryptographic hashing.


 *Linux & Bash Automation*

Automated bash scripts executing system health checks and network diagnostics.

1) system_health.sh: Monitors active processes, queries disk usage, and appends time-stamped logs to prevent data overwrites.
2) network_check.sh: Evaluates network connectivity to target IPs using ICMP packets and conditional exit-status logic ($?).

 *Python Security Tools*
Practical CLI utilities demonstrating network interaction, file I/O, and data validation.

01_ip_validator.py: Validates IPv4/IPv6 inputs using error handling and the ipaddress library.
02_log_parser.py: Opens and parses raw system logs using context managers (with open()) and string manipulation.
03_port_scanner.py: Scans target networks for open TCP ports utilizing low-level network socket connections.
04_http_inspector.py: Inspects server response codes and extracts security headers using the requests library.
05_hash_generator.py: Converts plaintext credentials into irreversible hexadecimal SHA-256 signatures using hashlib.
