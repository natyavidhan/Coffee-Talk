import socket
import json
from _thread import *

class Server:
    def __init__(self):
        config = json.load(open("config.json"))
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = [config["ip"], config["port"]]
        if ip[0] == "":
            self.host = socket.gethostbyname(socket.gethostname())
        else:
            self.host = ip[0]
        self.port = int(ip[1])

        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            print(str(e))
        self.s.listen(10)
        print("Waiting for a connection")
        self.members = {}
        
    def entry():
        while True:
            conn, addr = self.s.accept()
            start_new_thread(client, (conn, addr))
    
    def broadcast(self, msg, conn):
        for c in self.members:
            if c != conn:
                try:
                    c.send(msg)
                except:
                    pass

    def client(self, conn, addr):
        print("Connected to:", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            self.broadcast(data, conn)
            
        conn.close()
        print("Connection closed")
