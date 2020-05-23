import socket, threading

class SocketCom:
    def __init__(self):
        self.IP = socket.gethostname()
        self.PORT = 1234
        self.ADDR = (self.IP, self.PORT)
        self.HEADERSIZE = 64
        self.DISCONNECT_MSG = "~disconnect~"
        self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketServer.bind(self.ADDR)
        #s.listen(5)
    
    def handle_client(self, conn, addr):
        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode("utf-8").strip()
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode("utf-8")
                if msg == DISCONNECT_MSG:
                    connected = False
                else:
                    socketBodyHandler = socketBodyHandler(msg)
                conn.send("received".encode("utf-8"))
        conn.close()

    def start(self):
        print("server starting...")
        print(f"server listening on port {self.PORT}")
        self.socketServer.listen()
        while True:
            conn, addr = self.socketServer.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr)) 
            thread.start()
            print(f"active connections: {threading.activeCount() - 1}")