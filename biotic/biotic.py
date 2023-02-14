import serial
from xbee import XBee

# configure serial communication
ser = serial.Serial('/dev/ttyUSB0', 9600)

# create an XBee object and configure it for API mode
xbee = XBee(ser, escaped=True)

# create a network scan request and send it to the coordinator
network_scan_request = xbee.build_command('at', command='ND')
xbee.send(network_scan_request)

# wait for the network scan response
network_scan_response = xbee.wait_read_frame()

# print the network scan results
print('Found %d devices:' % (len(network_scan_response['devices']),))
for device in network_scan_response['devices']:
    print('- Address: %s, PAN ID: %s, Signal Strength: %d' % (
        device['source_addr_extended'],
        device['source_addr'],
        device['rssi']
    ))

# clean up the XBee object and serial connection
xbee.halt()
ser.close()
