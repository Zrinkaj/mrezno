import socket , ssl , pprint
from datetime import datetime
from local_machine_info import print_machine_info

print_machine_info()
print(datetime.now())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s,
                            ca_certs="server.crt",
                            cert_reqs=ssl.CERT_REQUIRED)
                        
ssl_sock.connect(('localhost', 10023))

print(repr(ssl_sock.getpeername()))
print(ssl_sock.cipher())
print(pprint.pformat(ssl_sock.getpeercert()))

ssl_sock.write("boo!")

if False:
    ssl_sock.write("""GET / HTTP/1.0r
    Host: www.verisign.comnn""")

    data = ssl_sock.read()

    ssl_sock.close()