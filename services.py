from device import Device

def deviceServices(device:Device,openPorts:list):
    services = []
    if 21 in openPorts:
        services.append("FTP")
    if 22 in openPorts:
        services.append("SSH")
    if 23 in openPorts:
        services.append("Telenet")
    if 25 in openPorts:
        services.append("SMTP")
    if 53 in openPorts:
        services.append("DNS")
    if 80 in openPorts:
        services.append("HTTP")
    if 433 in openPorts:
        services.append("HTTPS")
    if 1194 in openPorts:
        services.append("OpenVPN")
    if 3389 in openPorts:
        services.append("RDP")
    device.services = services