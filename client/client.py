from audio import Audio
from network import Network
from threading import Thread
import socket
import tkinter as tk
from tkinter import ttk

class Client:
    def __init__(self, ip):
        self.network = Network(ip)
        self.audio = Audio()
        self.start()

    def process(self):
        while True:
            data = self.audio.get()
            if data:
                data = self.network.send(data)
                self.audio.play(data)

    def start(self):
        Thread(target=self.process).start()
        

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee talk Client")
        self.root.geometry("500x200")
        self.root.resizable(False, False)
        
        title = tk.Label(text="Coffee talk", font=("Consolas", 25), anchor="center")
        title.place(x=0, y=15, width=500, height=30)
        
        tk.Label(text="Host:", font=("Consolas", 15), anchor="center").place(x=25, y=50, width=55, height=20)
        
        self.hostInput = tk.Entry(font=("Consolas", 15))
        self.hostInput.place(x=85, y=50, width=100, height=20)
        
        tk.Label(text="Port:", font=("Consolas", 15), anchor="center").place(x=220, y=50, width=55, height=20)
        
        self.portInput = tk.Entry(font=("Consolas", 15))
        self.portInput.place(x=265, y=50, width=100, height=20)
        
        joinButton = tk.Button(text="Join", font=("Consolas", 15), command=self.join)
        joinButton.place(x=410, y=48, width=55, height=24)
    
    def join(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()