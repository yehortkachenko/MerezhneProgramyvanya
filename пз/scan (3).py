import socket

def scan_selected_ports(host, ports):
    print(f"Сканування вибраних портів на {host}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Порт {port} відкритий")
            else:
                print(f"Порт {port} закритий")

host = "127.0.0.1"  
ports = [22, 80, 443]  
scan_selected_ports(host, ports)
