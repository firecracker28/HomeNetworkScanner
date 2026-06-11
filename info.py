from mac_vendor_lookup import MacLookup
import socket
def identifyVendor(self, macAddress:str):
    lookup = MacLookup()
    print("Downloading updated vendors list...")
    lookup.update_vendors()
    print("Looking up vendor")
    vendor = lookup.lookup(mac=macAddress)
    self.vendor = vendor

def getHostname(self,ipAddress:str):
    try:
        print("Host found! Device object updated")
        self.hostname = socket.gethostbyaddr(ipAddress)
    except:
        print("Host not found :(. Defaulting to Unknown")
        self.hostname = "Unknown"