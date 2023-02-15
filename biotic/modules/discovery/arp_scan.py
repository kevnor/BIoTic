from scapy.layers.l2 import ARP, Ether, srp
from get_vendor import get_vendor
import time


def arp_scan(ip):
    # create ARP packet
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # send packet and receive response
    response = srp(packet, timeout=3, verbose=0)[0]

    # extract information from response
    clients = []
    for sent, received in response:
        vendor = get_vendor(received.hwsrc)
        time.sleep(1)
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'vendor': vendor})

    # print results
    print("Available devices in the network:")
    print("IP" + " "*18 + "MAC" + " "*18 + "Vendor")
    for client in clients:
        print("{:16}    {}    {}".format(client['ip'], client['mac'], client['vendor']))


arp_scan("192.168.0.0/24")
