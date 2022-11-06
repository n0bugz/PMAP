# PMAP
Simple port mapping tool

usage: pmap.py -t TARGET -p PORTS
example: python3 pmap.py 192.168.227.121 -p 21,80

options:
  -h, --help       show this help message and exit
  -t TARGET_HOST   specify target host (IP address or domain name)
  -p TARGET_PORTS  specify target port[s] separated by comma (no spaces)
