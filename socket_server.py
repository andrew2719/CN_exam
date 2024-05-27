import socket

def start_server():
    host = 'localhost'
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening on", host, port)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            conn.sendall(b'Hello Client!')
            conn.close()

if __name__ == "__main__":
    start_server()
