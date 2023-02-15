import json
import nmap3

nmap = nmap3.Nmap()

os_results = nmap.nmap_os_detection("192.168.0.115")

print(json.dumps(os_results, indent=4))