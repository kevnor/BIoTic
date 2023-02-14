import sys
from scapy.sendrecv import sniff
from scapy.config import conf

conf.dot15d4_protocol = "zigbee"


def packet_handler(packet):
    print(packet.summary())


sniff(offline=sys.stdin.buffer, prn=packet_handler, store=0)
