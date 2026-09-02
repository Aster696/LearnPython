import socket

s = socket.socket()
port = 40057
s.bind(('', port))
s.listen(5)
print(f'Server lising on port {port}')

while True:
    c, arr = s.accept()
    print(f'Connected ip {arr[0]}')
    c.send(b'Thank you for connecting')
    c.close()