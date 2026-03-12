# NetSpecter V6 – Cyber Recon Framework

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)

```text
███╗   ██╗███████╗████████╗███████╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║   ███████╗██████╔╝█████╗  ██║        ██║   █████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║   ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║   ███████║██║     ███████╗╚██████╗   ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

It automates reconnaissance tasks such as **port scanning, subdomain discovery, web directory scanning, and technology detection**, while generating structured **JSON and HTML reports**.

---

# 🚀 Overview

NetSpecter combines **asynchronous scanning** with a **command-driven interface** to provide fast and efficient reconnaissance during security assessments.

The framework is designed to be **simple, modular, and extensible** for future modules.

---

# 🌟 Features

* ⚡ Asynchronous high-speed port scanning (1–1024)
* 🌐 Subdomain enumeration
* 📂 Web directory scanning
* 🔎 Web technology detection
* 🌍 WHOIS domain intelligence
* 📊 JSON & HTML report generation
* 🧠 Modular command-driven design
* 💻 Easy to extend

---

# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/alimusa80/NetSpecter-Cyber-Recon-Framework.git
cd NetSpecter-Cyber-Recon-Framework
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

* Python **3.8+**
* aiohttp
* python-whois

---

# 💻 Usage

Run NetSpecter:

```bash
python netspecter.py
```

You will be prompted for:

```
Target (domain/IP):
Command (scan | webscan | subdomains | full):
```

---

# 📋 Commands

| Command    | Description                                           |
| ---------- | ----------------------------------------------------- |
| scan       | Asynchronous port scan                                |
| webscan    | Directory scan + technology detection                 |
| subdomains | Subdomain enumeration                                 |
| full       | Complete scan (WHOIS + subdomains + ports + web scan) |

---

# 🧪 Example Usage

```
Target: example.com
Command: full
```

Example output:

```
WHOIS Lookup...
Registrar: NameCheap

Enumerating subdomains...
[FOUND] api.example.com
[FOUND] dev.example.com

Starting port scan...
[OPEN] 22
[OPEN] 80
[OPEN] 443

Scanning directories...
[DIR] http://example.com/admin
[DIR] http://example.com/login

Detecting technologies...
[TECH] nginx
```

---

# 🗂 Reports

NetSpecter automatically generates reports after each scan:

```
netspecter_report.json
netspecter_report.html
```

Reports contain:

* Target information
* Open ports
* Subdomains
* Discovered directories
* Detected technologies
* Scan duration

---

# 📦 Project Structure

```
NetSpecter-Cyber-Recon-Framework
│
├── netspecter.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚠ Disclaimer

This tool is intended **for educational purposes and authorized security testing only**.

Do **not** use NetSpecter against systems without permission.

The author is not responsible for misuse.

---

# 👨‍💻 Author

Ali Musa

GitHub: https://github.com/alimusa80
