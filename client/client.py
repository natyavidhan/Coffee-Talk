from audio import Audio
from network import Network
from threading import Thread
import socket


class Client:
    def __init__(self, ip):
        self.network = Network(ip)
        self.audio = Audio()

    def recieve(self):
        while True:
            try:
                data = self.network.client.recv(1024)
                self.audio.play(data)
            except:
                pass
    
    def send(self):
        while True:
            try:
                data = self.audio.get()
                self.network.client.sendall(data)
            except:
                pass

    def start(self):
        t1 = Thread(target=self.recieve)
        t2 = Thread(target=self.send)
        t1.start()
        t2.start()
        
client = Client(f"{socket.gethostbyname(socket.gethostname())}:42069")
client.start()