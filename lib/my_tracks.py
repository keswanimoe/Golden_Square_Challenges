class MyTracks():
    def __init__(self):
        self.songs = []
        
    def add(self, title):
        self.songs.append(title)
        
    def list(self):
        return self.songs