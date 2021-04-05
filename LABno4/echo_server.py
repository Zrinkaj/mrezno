import socket
import datetime
from local_machine_info import print_machine_info

host = socket.gethostname()
port = 12345

echo_server = socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)

print_machine_info()
print(datetime.datetime.now())

print ("Cekam klijenta...")
conn, addr = echo_server.accept()
print ('Spojen :' , addr)
while True:
    data = conn.recv(1024)
    if not data : break
    conn.sendall(data)


#conn.close()