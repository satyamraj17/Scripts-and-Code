import subprocess
import sys


def finding_open_ports(target):
    result = subprocess.run(["nmap", "-T4", "-Pn", "-n", target, "-oN", "open_ports.txt"], capture_output=True, text=True)
    return result.stdout


def aggressive_scan(target, ports_and_services):
    ports = ""
    for keys in ports_and_services.keys():
        ports += keys + ","

    ports = ports[:-1]
    target = sys.argv[1]
    result = subprocess.run(["nmap", "-A", "-Pn", "-p", ports, target, "-oN", "ports_services.txt"], capture_output=True, text=True)
    return result.stdout


def filter_open_ports():
    
    with open("open_ports.txt", "r") as f:
        output = f.readlines()[5:-2]

    ports_and_services = {}

    for p in output:
        port = p.split("open")[0].split("/tcp")[0]
        service = p.split("open")[1].strip()

        ports_and_services[port] = service

    return ports_and_services


def service_enumeration(ports_and_services, target):
    # defined_services = ["ssh", "http", "https", "ftp", "smb", "http-proxy"]
    for port, service in ports_and_services.items():
        # if service == 'ssh':
        #     remote_host = f"root@{target}"
        #     result = subprocess.run(["ssh", remote_host, "-p", port], capture_output=True, text=False, check=True)

        if service == 'http' or service == 'http-proxy':
            print(f"Performing subdirectories scan on {target} on port {port}")
            result = subprocess.run(["ffuf", "-u", f"http://{target}:{port}/FUZZ", "-w", "/usr/share/seclists/Discovery/Web-Content/big.txt"], capture_output=True, text=True, check=True)
            output = result.stdout
            output = output.strip("\n\n").split("\n\n")

            print(f"\n\nPrinting the subdirectories found on {target}\n")
            
            for i in output:
                print(i)
        
        if service == "ftp":
            print(f"Performing anonymous FTP login on {target}")
            


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 enumerate.py <target_ip>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"Running nmap on {target}...\n")
    output = finding_open_ports(target=target)

    print(f"Filtering the open ports and services found...")
    ports_and_services = filter_open_ports()
    print(f"{ports_and_services}\n")

    print(f"Performing aggressive scan on {target}...")
    services_output = aggressive_scan(target=target, ports_and_services=ports_and_services)
    print(f"{services_output}\n")

    port_enumeration = service_enumeration(ports_and_services=ports_and_services, target=target)


if __name__ == "__main__":
    main()