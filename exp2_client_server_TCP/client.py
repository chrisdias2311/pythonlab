import socket 

HOST = 'localhost'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

data = client