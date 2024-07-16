import socket

def start_server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(10)
    print(f"Server listening on {ip}:{port}")

    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr}")
        conn.close()

if __name__== "__main__":
    target_ip = "127.0.0.1"  
    target_port = 8081  
    start_server(target_ip, target_port)