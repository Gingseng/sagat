import socket
import threading

def receive_messages(sock):
    while True:
        message = sock.recv(1024).decode('utf-8')
        print(message)

# Get server information from the user
server_ip = input("Enter server IP: ")
server_port = int(input("Enter server port: "))
username = input("Enter your username: ")

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Send the username to the server
client_socket.send(username.encode('utf-8'))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Main loop to send messages
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
