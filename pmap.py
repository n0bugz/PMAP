import argparse
import socket
import threading

def port_scan(target, ports):
    try:
        ip = socket.gethostbyname(target)
    except socket.herror:
        print(f'[-] Cannot resolve {target}: Unknown host')
        return
    try:
        tgt_name = socket.gethostbyaddr(ip)
        print(f'\n[+] Scan Results for: {tgt_name[0]}')
    except socket.herror:
        print(f'\n[+] Scan Results for: {ip}')

    # TODO:Create a better output
    for ports in ports:
        t = threading.Thread(target=scan, args=(target, int(ports)))
        t.start()

def scan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        results = s.connect_ex((target, port)) # Returns a 0 if successful
        if results == 0:
            print("%s/tcp %s - open" % (port, socket.getservbyport(port, 'tcp')))
        else:
            print("%s/tcp - %s - closed" % (port, socket.getservbyport(port, 'tcp')))

        s.close()
    except KeyboardInterrupt:
        print("\n Exiting Programing!")
        sys.exit()
    except socket.gaierror:
        print("[!] Hostname could not be resolved!")
        sys.exit()
    except socket.herror:
        print("[!] Server not responding")
        sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='pmap.py -t TARGET -p PORTS'
              '\nexample: python3 pmap.py -t 192.168.227.121 -p 21,80')

    parser.add_argument('-t', type=str, metavar='TARGET_HOST', help='specify target host (IP address or domain name)')
    parser.add_argument('-p', required=True, type=str, metavar='TARGET_PORTS',help='specify target port[s] separated by comma ''(no spaces)')
    args = parser.parse_args()

    # Incorporate with nmap?

    if args.p is not None:
        args.tgt_ports = str(args.p).split(',')
        port_scan(args.t, args.tgt_ports)
