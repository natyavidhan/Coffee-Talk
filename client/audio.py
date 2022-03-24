import pyaudio

class Audio:
    def __init__(self):
        chunk_size = 1024
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)

    def play(self, data):
        try:
            self.playing_stream.write(data)
        except:
            pass


    def get(self):
        try:
            data = self.recording_stream.read(1024)
            return data
        except:
            pass