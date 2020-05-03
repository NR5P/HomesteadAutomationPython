import socket
import thread

class SocketCom:
    def __init__(self):
        IP = socket.gethostname()
        PORT = 1234
        ADDR = (IP, PORT)
        HEADERSIZE = 64
        DISCONNECT_MSG = "~disconnect~"
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.bind(ADDR)
        s.listen(5)
    
    def handle_client(self, conn, addr):
        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode("utf-8").strip()
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode("utf-8")
                if msg == DISCONNECT_MSG:
                    connected = False
        conn.close()

    def start(self):
        print("server starting...")
        print(f"server listening on port {PORT}")
        socket.listen()
        while True:
            conn, addr = socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr)) 
            thread.start()
            print(f"active connections: {threading.activeCount() - 1}")