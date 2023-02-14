import os
import usb.core
from usb.backend import libusb1

be = libusb1.get_backend()
dev = usb.core.find(backend=be)
