import socket
import sys
from datetime import datetime

file = open("Port-Scanner.txt", "w")


try:
    host = input("PLease enter host to scan: ") 
    print(f"Finding Open Ports @{host}...")
    host_ip = socket.gethostbyname(host)
    file.write(f"Scanning Host: {host_ip}\n")
    
    t1 = datetime.now()
    print(f"Start Time: {t1}")
    file.write((f"Start Time: {t1}\n"))
    
    
    
    for port in range(1, 1025):
        # AF_INET covers ipv4 addresses, #AF_INET6 would be ipv6
        # SOCK_STREAM ensures we are using TCP, SOCK.DGRAM can be used for UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)
        result = sock.connect_ex((host_ip, port))

        if result == 0:
            print(f"Port {port} Open")
            file.write(f"Port {port} Open\n")
            


except socket.gaierror:
    print("Hostname you entered is invalid")
    sys.exit()
except socket.error:
    print("Could not connect to server")
    sys.exit()


t2 = datetime.now()
print(f"End Time: {t2}")
file.write((f"End Time: {t2}\n\n"))

total_time = t2 - t1
print(f"Total Time: {total_time}")
file.write((f"Total Time: {total_time}\n\n\n"))