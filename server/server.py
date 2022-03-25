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
        
        self.members = []
    
    def broadcast(self, msg, sender):
        for member in self.members:
            if member != sender:
                try:
                    self.s.sendto(msg, member)
                except Exception as e:
                    self.members.remove(member)
                    print(str(e))
    
    def start(self):
        while True:
            try:
                msg, addr = self.s.recvfrom(2048)
                if addr not in self.members:
                    self.members.append(addr)
                self.broadcast(msg, addr)
            except Exception as e:
                print(str(e))
            
server = Server()
Thread(target=server.start).start()