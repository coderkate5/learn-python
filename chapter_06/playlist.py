# The len method
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)
    
    def __str__(self):
        return self.name + " playlist with " + str(len(self)) + " songs."
    

my_playlist = Playlist("Favorites")
my_playlist.add_song("Song 1")
my_playlist.add_song("Song 2")
my_playlist.add_song("Song 3")

print(my_playlist)
print("Number of songs: ", len(my_playlist))