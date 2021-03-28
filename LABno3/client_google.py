import socket
client_socket = socket.socket()
host = socket.gethostbyname('www.google.com')
port = 80

client_socket.connect((host,port))
print('Socket se uspješno spojio na Google na port = 'port 'i IP adresu =' host)

client_socket.close()