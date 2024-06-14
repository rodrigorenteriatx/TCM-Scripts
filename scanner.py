#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
# First arg 0 , will be scanner.py
# Second arg is the ip 

if len(sys.argv) ==  2:
    target = socket.gethostbyname(sys.argv[1])
    #If given hostname, internal dns will translate to ip, but we can just give a direct ip address (Recommended)
    #Translate the hostname to ipv4
else:
    print("Invalid amount of args \n Syntax: python3 scanner.py <ip>")

#EXAMPLE
#python3 scanner.py 192.168.204.1

# add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: "+str(datetime.now()))
print("-" * 50)


try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result  = s.connect_ex((target,port))
        # If 0, then open, if not, then it is closed.
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    #will happen if hostname is not resolved
    print("Hostname coud not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to the server")
    sys.exit()


