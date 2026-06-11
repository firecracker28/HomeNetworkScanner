class Device:

    def __init__(self,ip:str,mac:str):
        self.ip = ip
        self.mac = mac

        self.vendor = "Unknown"
        self.hostname = "Unknown"
        self.deviceGuess = None

        self.openPorts = []
        self.services = []

        self.riskLevel = None
        self.riskScore = None

        self.reasons = []
    
    def loadDeviceDetails(self):
        pass
    
    def __str__(self):
        return f"Device: {self.hostname}-{self.vendor}"
