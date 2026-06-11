from scapy.all import IP, TCP, sr1, send

COMMON_PORTS = [21, 22, 23, 53, 80, 443, 1194, 3389]

def scan_ports(mode:str, ip:str):
    open_ports = []
    if mode == "quick":
        for port in COMMON_PORTS:
            # Build SYN packet
            packet = IP(dst=ip) / TCP(dport=port, flags="S")
            print("Sending scanning packets")
            # Send packet and wait for response
            response = sr1(packet, timeout=1, verbose=0)

            if response is None:
                continue

            # Check if SYN-ACK (port is open)
            if response.haslayer(TCP):
                if response[TCP].flags == 0x12:  # SYN-ACK
                    open_ports.append(port)

                    # Send RST to cleanly close connection
                    rst = IP(dst=ip) / TCP(dport=port, flags="R")
                    send(rst, verbose=0)
    elif mode == "full":
        for port in range(0,65535):
            # Build SYN packet

            packet = IP(dst=ip) / TCP(dport=port, flags="S")
            print("Sending scanning packets")
            # Send packet and wait for response
            response = sr1(packet, timeout=1, verbose=0)

            if response is None:
                continue

            # Check if SYN-ACK (port is open)
            if response.haslayer(TCP):
                if response[TCP].flags == 0x12:  # SYN-ACK
                    open_ports.append(port)

                    # Send RST to cleanly close connection
                    rst = IP(dst=ip) / TCP(dport=port, flags="R")
                    send(rst, verbose=0)
    else:
        raise ValueError("Invalid mode for port scanning")
    return open_ports