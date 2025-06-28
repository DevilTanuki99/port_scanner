import socket

def banner():
    print( 
    f" /$$$$$$$                    /$$        /$$$$$$\n"
    f"| $$__  $$                  | $$       /$$__  $$\n"
    f"| $$  \ $$/$$$$$$  /$$$$$$ /$$$$$$    | $$  \__/ /$$$$$$$ /$$$$$$ /$$$$$$$ /$$$$$$$  /$$$$$$  /$$$$$$\n" 
    f"| $$$$$$$/$$__  $$/$$__  $|_  $$_/    |  $$$$$$ /$$_____/|____  $| $$__  $| $$__  $$/$$__  $$/$$__  $$\n"
    f"| $$____| $$  \ $| $$  \__/ | $$       \____  $| $$       /$$$$$$| $$  \ $| $$  \ $| $$$$$$$| $$  \__/\n"
    f"| $$    | $$  | $| $$       | $$ /$$   /$$  \ $| $$      /$$__  $| $$  | $| $$  | $| $$_____| $$\n"      
    f"| $$    |  $$$$$$| $$       |  $$$$/  |  $$$$$$|  $$$$$$|  $$$$$$| $$  | $| $$  | $|  $$$$$$| $$\n"      
    f"|__/     \______/|__/        \___/$$$$$\______/ \_______/\_______|__/  |__|__/  |__/\_______|__/\n"      
    f"                                |______/\n"
    f"Create by: @DevilTanuki99\n"
    )

# fungsi untuk memindai 1 port tertentu
def scan_port(ip, port):
    try:
        # Membuat socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Menentukan waktu tunggu koneksi (timeout)
        sock.settimeout(0.5)

        # Mencoba menyambung ke alamat IP dan port
        result = sock.connect_ex((ip, port))

        # Menutup socket setelah digunakan
        sock.close()

        # Mengembalikan True jika port terbuka
        return result == 0
    except:
        # Jika terjadi kesalahan (misalnya host tidak ditemukan), anggap port tertutup
        return False

GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# main funcion
def main():
    print(f"{DARK_GREEN}")
    banner()

    # input alamat IP atau hostname
    target = input("Input IP address or hostname: ")

    print("\n+--------- PORT LIST ---------+\n"
          "| 20 : FTP (Data Transfer)    +\n"
          "| 21 : FTP (Control)          +\n"
          "| 22 : SSH                    +\n"
          "| 23 : Telnet                 +\n"
          "| 25 : SMTP                   +\n"
          "| 53 : DNS                    +\n"
          "| 68 : DHCP Client            +\n"
          "| 80 : HTTP                   +\n"
          "| 110 : POP3                  +\n"
          "| 123 : NTP                   +\n"
          "| 143 : IMAP                  +\n"
          "| 161 : SNMP                  +\n"
          "| 443 : HTTPS                 +\n"
          "| 1433 : Microsoft SQL Server +\n"
          "| 1521 : Oracle DB            +\n"
          "| 3306 : MySQL                +\n"
          "| 3389 : RDP                  +\n"
          "| 8080 : HTTP Alt             +\n"
          "| 27017 : MongoDB             +\n"
          "+-----------------------------+\n"
          )

    # port list
    port_list = [20, 21, 22, 23, 25, 53, 68, 80, 110, 123, 143, 161, 443, 1433, 1521, 3306, 3389, 8080, 27017]

    # menampilkan info scanning
    print(f"Scanning {target} from port in list...\n")

    for port in port_list:
        if scan_port(target, port):
            print(f"{GREEN}[OPEN✅] Port {port} Open")
        else:
            print(f"{RED}[CLOSE❌] Port {port} Closed")

    print(f"\n{CYAN}Scanning complete!{RESET}")
if __name__ == "__main__":
    main()