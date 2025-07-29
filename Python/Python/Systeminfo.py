import os
import socket
import getpass

print("Hostname:", socket.gethostname())
print("IP Address:", socket.gethostbyname(socket.gethostname()))
print("Current User:", getpass.getuser())
print("Current Directory:", os.getcwd())
