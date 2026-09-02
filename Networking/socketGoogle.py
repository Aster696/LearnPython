import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error: %s" %(err))

port = 80

try: 
    host_ip = socket.gethostbyname('www.google.com')
except:
    print("There was error resolving the host")
    sys.exit()

s.connect((host_ip, port))

print("Socket connected has successfully connected to google", host_ip, port)