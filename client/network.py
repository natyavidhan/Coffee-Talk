import socket
import json


class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = ip.split(":")
        if ip[0] == "":
            self.host = socket.gethostbyname(socket.gethostname())
        else:
            self.host = ip[0]
        self.port = int(ip[1])
        self.addr = (self.host, self.port)

    def send(self, data):
        try:
            self.client.sendto(data, self.addr)
            response = self.client.recvfrom(2048)[0]
            return response
        except socket.error as e:
            print(str(e))
            return "Error"