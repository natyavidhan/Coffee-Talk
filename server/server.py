import socket
import json
from threading import Thread

class Server:
    def __init__(self):
        config = json.load(open("config.json"))
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = [config["ip"], config["port"]]
        if ip[0] == "":
            self.host = socket.gethostbyname(socket.gethostname())
        else:
            self.host = ip[0]
        self.port = int(ip[1])

        try:
            self.s.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))
        
        members = []
    
    def broadcast(self, msg):
        for member in members:
            try:
                self.s.sendto(msg.encode('utf-8'), member)
            except:
                pass
    
    def start(self):
        while True:
            msg, addr = self.s.recvfrom(1024)
            if addr not in members:
                members.append(addr)
            self.broadcast(msg.decode('utf-8'))
            
        

server = Server()
Thread(target=server.start).start()