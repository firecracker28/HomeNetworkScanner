from scapy.layers.l2 import ARP,Ether
from scapy.sendrecv import srp
import re


def validIP(ip):
        expression = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}0$'
        if re.match(expression,ip) is None:
            return False
        else:
            return True

class NetworkScanner:
    """
    This IP must be the broadcast address for your network. For
    further instructions on how to find your broadcast address. Refer to the README.md
    in the repository
    """
    def __init__(self,ip:str):
        if validIP(ip):
            self.ip = ip
        else:
            raise ValueError("Invalid or Incorrect IP address. IP address must be the broadcast address for your network")
    def scan(self):
        activeHosts = []
        arpRequest = ARP(pdst=self.ip)
        ethernetframe = Ether()
        packet = ethernetframe/arpRequest
        packet.show()
        """
        result = srp(packet)[0] #Only uncomment when not at work
        for sent,recived in result:
             activeHosts.append(recived.psrc)
        return activeHosts
        """