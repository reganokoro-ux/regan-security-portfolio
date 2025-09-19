import socket

# Define the target (localhost)
target = "127.0.0.1"
# Common ports to scan
ports = [22, 80, 443, 3306, 8080]

print(f"Scanning {target} for open ports...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    sock.close()
