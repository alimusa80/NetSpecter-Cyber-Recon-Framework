import asyncio
import socket
import aiohttp
import json
import whois
from datetime import datetime

print("="*75)
print("                 NetSpecter V6 Cyber Recon Framework")
print("="*75)

target = input("Target (domain/IP): ").strip()
command = input("Command (scan | webscan | subdomains | full): ").strip()

try:
    target_ip = socket.gethostbyname(target)
except:
    target_ip = target

start_time = datetime.now()

results = {
    "target": target,
    "ip": target_ip,
    "ports": [],
    "subdomains": [],
    "directories": [],
    "tech": []
}

# --------------------
# PORT SCANNER
# --------------------

async def scan_port(port):

    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(target_ip, port),
            timeout=0.5
        )

        print(f"[OPEN] {port}")

        results["ports"].append(port)

        writer.close()
        await writer.wait_closed()

    except:
        pass


async def port_scan():

    print("\nStarting port scan...\n")

    tasks = []

    for port in range(1,1025):
        tasks.append(scan_port(port))

    await asyncio.gather(*tasks)

# --------------------
# SUBDOMAIN ENUM
# --------------------

async def subdomain_enum():

    print("\nEnumerating subdomains...\n")

    words = [
        "www","mail","ftp","api","dev","test",
        "admin","portal","beta","stage"
    ]

    for w in words:

        domain = f"{w}.{target}"

        try:
            ip = socket.gethostbyname(domain)

            print(f"[FOUND] {domain}")

            results["subdomains"].append(domain)

        except:
            pass

# --------------------
# DIRECTORY SCANNER
# --------------------

async def dir_scan():

    print("\nScanning directories...\n")

    paths = [
        "admin","login","dashboard",
        "backup","api","dev","test"
    ]

    async with aiohttp.ClientSession() as session:

        for p in paths:

            url = f"http://{target}/{p}"

            try:
                async with session.get(url, timeout=4) as r:

                    if r.status < 404:

                        print(f"[DIR] {url}")

                        results["directories"].append(url)

            except:
                pass

# --------------------
# TECH DETECTION
# --------------------

async def tech_detect():

    print("\nDetecting technologies...\n")

    url = f"http://{target}"

    async with aiohttp.ClientSession() as session:

        try:
            async with session.get(url) as r:

                server = r.headers.get("Server")

                if server:
                    print(f"[TECH] {server}")
                    results["tech"].append(server)

        except:
            pass

# --------------------
# WHOIS LOOKUP
# --------------------

def whois_lookup():

    print("\nWHOIS Lookup...\n")

    try:
        w = whois.whois(target)

        print(f"Registrar: {w.registrar}")

    except:
        print("WHOIS lookup failed")

# --------------------
# REPORT GENERATION
# --------------------

def save_reports():

    duration = datetime.now() - start_time
    results["duration"] = str(duration)

    with open("netspecter_report.json","w") as f:
        json.dump(results,f,indent=4)

    html = f"""
<html>
<head>
<title>NetSpecter Report</title>
<style>
body{{background:#111;color:#eee;font-family:Arial}}
table{{border-collapse:collapse;width:80%}}
td,th{{border:1px solid #444;padding:8px}}
th{{background:#222}}
</style>
</head>
<body>

<h1>NetSpecter Recon Report</h1>

<p>Target: {target}</p>
<p>IP: {target_ip}</p>
<p>Duration: {duration}</p>

<h2>Open Ports</h2>
<ul>
"""

    for p in results["ports"]:
        html += f"<li>{p}</li>"

    html += "</ul><h2>Subdomains</h2><ul>"

    for s in results["subdomains"]:
        html += f"<li>{s}</li>"

    html += "</ul><h2>Directories</h2><ul>"

    for d in results["directories"]:
        html += f"<li>{d}</li>"

    html += "</ul></body></html>"

    with open("netspecter_report.html","w") as f:
        f.write(html)

    print("\nReports saved:")
    print("netspecter_report.json")
    print("netspecter_report.html")

# --------------------
# COMMAND SYSTEM
# --------------------

async def main():

    if command == "scan":
        await port_scan()

    elif command == "subdomains":
        await subdomain_enum()

    elif command == "webscan":
        await dir_scan()
        await tech_detect()

    elif command == "full":
        whois_lookup()
        await subdomain_enum()
        await port_scan()
        await dir_scan()
        await tech_detect()

    else:
        print("Unknown command")

    save_reports()

asyncio.run(main())
