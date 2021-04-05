import socket
import datetime
from local_machine_info import print_machine_info

host = socket.gethostname()
port = 12345
client_socket = socket.socket()


client_socket.connect((host,port))

mydata = input("Upiši tekst: ")
client_socket.sendall(mydata.encode())
data = client_socket.recv(1024)

print_machine_info()
print(datetime.datetime.now())

if mydata == "Zrinka" :
       print ("Molimo unesite drugo ime , Zrinka unos nije podržan unos")
else : print (data)

#client_socket.close()