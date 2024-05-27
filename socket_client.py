import socket

def connect_server():
    host = 'localhost'
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = s.recv(1024)
        print('Received:', message.decode())

if __name__ == "__main__":
    connect_server()
