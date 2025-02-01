import nmap

def scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024', '-sV')

    for host in nm.all_hosts():
        print(f"Scanning: {host}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port} | State: {nm[host][proto][port]['state']} | Service: {nm[host][proto][port]['name']}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    scan(target_ip)
