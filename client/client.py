from audio import Audio
from network import Network
from threading import Thread
import socket
import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee talk Client")
        self.root.geometry("500x200")
        self.root.resizable(False, False)
        self.audio = Audio()
        self.network = None
        self.isMuted = True
        
        title = tk.Label(text="Coffee talk", font=("Consolas", 25), anchor="center")
        title.place(x=0, y=15, width=500, height=30)
        
        tk.Label(text="Host:", font=("Consolas", 15), anchor="center").place(x=25, y=50, width=55, height=20)
        
        self.hostInput = tk.Entry(font=("Consolas", 13))
        self.hostInput.place(x=85, y=50, width=100, height=20)
        
        tk.Label(text="Port:", font=("Consolas", 15), anchor="center").place(x=210, y=50, width=55, height=20)
        
        self.portInput = tk.Entry(font=("Consolas", 13))
        self.portInput.place(x=265, y=50, width=100, height=20)
        
        joinButton = tk.Button(text="Join", font=("Consolas", 15), command=self.join)
        joinButton.place(x=410, y=48, width=55, height=24)
        
        self.muteButton = tk.Button(text="Unmute", font=("Consolas", 15), command=self.mute)
        self.muteButton.place(x=315, y=125, width=80, height=30)
        
        tk.Label(text="Members", font=("Consolas", 15), anchor="center").place(x=50, y=80, width=80, height=30)
        
        self.memberList = tk.Listbox(font=("Consolas", 13))
        self.memberList.place(x=50, y=110, width=250, height=70)
    
    def join(self):
        ip = f"{self.hostInput.get()}:{self.portInput.get()}"
        print(f"Joining {ip}")
        self.network = Network(ip)
        Thread(target=self.process).start()
    
    def mute(self):
        if self.isMuted:
            self.isMuted = False
            self.muteButton.config(text="Mute")
        else:
            self.isMuted = True
            self.muteButton.config(text="Unmute")
    
    def process(self):
        while True:
            try:
                if self.network:
                    data = b"" if self.isMuted else self.audio.get()
                    data = self.network.send(data)
                    self.audio.play(data)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()