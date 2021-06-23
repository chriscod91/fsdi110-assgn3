class Album: 


    #class constructor
    def __init__(self, id, title, artist, price, genre, year):
         self.id = id
         self.title = title
         self.genre = genre
         self.artist = artist
         self.price = price
         self.year = year
         self.songs = []

    def __str__(self):
        return f"{self.id} - {self.title}"    