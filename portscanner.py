import socket
import pyfiglet
from tqdm import tqdm
from colorama import init, Fore, Style

print(pyfiglet.figlet_format("Port Scanner"))

init()

def check_port(ip, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: {Fore.GREEN}Otwarty{Style.RESET_ALL}")
            open_ports.append(port)
        else:
            print(f"Port {port}: {Fore.RED}Zamknięty{Style.RESET_ALL}")
        sock.close()
    except:
        print(f"Port {port}: {Fore.RED}Błąd{Style.RESET_ALL}")

def ping_ip(ip):
    print(f"Skanowanie portów dla {ip}")
    open_ports = []
    for port in tqdm(range(1, 65536)):
        check_port(ip, port, open_ports)

    print(f"Otwarte porty dla {ip}: {open_ports}")

ip = input("Podaj adres IP: ")
ping_ip(ip)
