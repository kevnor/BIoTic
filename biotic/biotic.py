import usb.core
import socket

print(socket.if_nameindex())

# find all USB devices
"""devices = usb.core.find(find_all=True)

# iterate over the devices and print their information
for device in devices:
    print('Device:', device)
    print('  - Manufacturer:', usb.util.get_string(device, device.iManufacturer))
    print('  - Product:', usb.util.get_string(device, device.iProduct))
    print('  - Serial:', usb.util.get_string(device, device.iSerialNumber))
    print()"""