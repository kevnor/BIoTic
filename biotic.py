# Import the necessary libraries
# Import the necessary libraries
from scapy.all import *
from scapy.layers.l2 import Ether, ARP

# Define the subnet to scan
subnet = "192.168.0.0/24"

# Send an ARP request to the broadcast address and wait for responses
responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=subnet), timeout=2, verbose=0)

# Loop through each response
for response in responses:
    # Extract the IP and MAC addresses from the response
    ip = response[1].psrc
    mac = response[1].hwsrc
    # Print the IP and MAC addresses
    print(f"IP: {ip} MAC: {mac}")


