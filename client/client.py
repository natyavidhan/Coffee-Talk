from audio import Audio
from network import Network
from threading import Thread
import socket


class Client:
    def __init__(self, ip):
        self.network = Network(ip)
        self.audio = Audio()

    def process(self):
        while True:
            data = self.audio.get()
            if data:
                data = self.network.send(data)
                self.audio.play(data)

    def start(self):
        Thread(target=self.process).start()
        
client = Client(f":42069")
client.start()