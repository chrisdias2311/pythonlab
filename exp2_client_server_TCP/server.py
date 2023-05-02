import socket 

HOST = 'localhost'
PORT = 8000

# Create a new sockert object 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to Host and port 
server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address}")

    message = "Thank you for connecting!"
    client_socket.send(message.encode('utf-8'))

    client_socket.close()