import socket
from datetime import datetime


# Function to scan ports
def port_scan(target, start_port, end_port):
    try:
        # Convert the target (hostname) to IP address
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Hostname could not be resolved: {target}")
        return

    # Get the current date and time
    scan_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Lists to store open and closed ports
    open_ports = []
    closed_ports = []

    # Print and log the scan time
    print(f"\nPort Scan Report for {target} ({target_ip}) - {scan_time}\n")
    print(f"{'-' * 40}")

    # Open a file to save the scan results
    with open('port_scan_log.txt', 'a') as log_file:
        log_file.write(f"\nPort Scan Report for {target} ({target_ip}) - {scan_time}\n")
        log_file.write(f"{'-' * 40}\n")

        # Iterate through all ports in the given range
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Timeout for socket connection attempt
            result = sock.connect_ex((target_ip, port))  # 0 means the port is open
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
                log_file.write(f"Port {port} is open\n")
            else:
                closed_ports.append(port)
            sock.close()

        # Log the lists of open and closed ports
        if open_ports:
            print(f"\nOpen Ports: {open_ports}")
            log_file.write(f"\nOpen Ports: {open_ports}\n")
        if closed_ports:
            print(f"Closed Ports: {closed_ports[:10]} (showing first 10)")
            log_file.write(f"Closed Ports: {closed_ports[:10]} (showing first 10)\n")

    print(f"\nPort scan completed and logged to port_scan_log.txt")


# Example usage
if __name__ == "__main__":
    target_host = input("Enter target hostname or IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    # Perform the port scan
    port_scan(target_host, start_port, end_port)
