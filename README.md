📄 NetSpecter V6 – Cyber Recon Framework
███╗   ██╗███████╗████████╗███████╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║   ███████╗██████╔╝█████╗  ██║        ██║   █████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║   ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║   ███████║██║     ███████╗╚██████╗   ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

               NetSpecter V6 – Cyber Recon Framework
🚀 Overview

NetSpecter V6 is a modular Python cyber reconnaissance framework designed for security researchers, penetration testers, and network analysts.

It automates network discovery, subdomain enumeration, web directory scanning, and technology detection while generating structured JSON and HTML reports.

NetSpecter combines high-speed asynchronous scanning with a command-driven interface for efficient, professional reconnaissance.

🌟 Features

⚡ Asynchronous high-speed port scanning (1–1024 by default)

🌐 Subdomain discovery using common prefixes or custom wordlists

📂 Web directory brute-force scanning

🔎 Web technology detection (Apache, Nginx, etc.)

🌍 WHOIS domain intelligence

📊 JSON & HTML report generation

🧠 Modular command-driven design (scan, webscan, subdomains, full)

💻 Extensible for future modules

🛠 Installation

Clone the repository:

git clone (https://github.com/alimusa80/NetSpecter-Cyber-Recon-Framework/blob/main/netspecter.py)
cd netspecter

Install dependencies:

pip install -r requirements.txt

Dependencies include:

Python 3.8+

aiohttp

python-whois

colorama

rich

💻 Usage

Run NetSpecter:

python netspecter.py
Commands
Command	Description
scan	Asynchronous port scan
webscan	Web directory scan & technology detection
subdomains	Subdomain enumeration
full	Complete scan: WHOIS + subdomains + ports + web
Example Usage
Target: example.com
Command: full

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
🗂 Reports

NetSpecter generates structured reports in:

reports/netspecter_report.json – JSON format for automation or further analysis

reports/netspecter_report.html – Interactive HTML report with open ports, subdomains, and directories

Reports are automatically saved to the reports/ folder after each scan.

📦 Project Structure
netspecter/
│
├── netspecter.py            # Main CLI entry
├── requirements.txt         # Python dependencies
├── README.md
│
├── modules/                 # Core scanning modules
│   ├── port_scanner.py
│   ├── subdomain_enum.py
│   ├── web_scanner.py
│   ├── tech_detect.py
│   └── whois_lookup.py
│
├── reports/                 # Generated scan reports
│
├── wordlists/               # Subdomain & directory wordlists
│   ├── subdomains.txt
│   └── directories.txt
│
└── utils/                   # Utilities (banner, reporter)
    ├── banner.py
    └── reporter.py
