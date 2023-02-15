import nmap3
import json

nmap = nmap3.Nmap()
results = nmap.nmap_version_detection("192.168.0.115")

print(json.dumps(results, indent=4))
