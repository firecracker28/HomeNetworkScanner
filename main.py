from NetworkScanner import NetworkScanner
ip = input("Enter your network broadcast address: ")
scanner = NetworkScanner(ip)
scanner.scan()