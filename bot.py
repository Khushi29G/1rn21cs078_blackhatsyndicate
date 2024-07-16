import socket
import threading

def flood_server(host='127.0.0.1', port=9999):
    """Flood the server with requests."""
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            message = "Flooding the server!"
            client.send(message.encode('utf-8'))
            response = client.recv(4096)
            print(f"Received: {response.decode('utf-8')}")
            client.close()
        except Exception as e:
            print(f"Exception occurred: {str(e)}")

def start_flooding(host='127.0.0.1', port=9999, threads=10):
    """Start multiple threads to flood the server."""
    for _ in range(threads):
        thread = threading.Thread(target=flood_server, args=(host, port))
        thread.start()

if __name__ == "__main__":
    start_flooding()