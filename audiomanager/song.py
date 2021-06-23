class Song:


    def __init__(self, id, title, length_secs, author):
        self.id = id
        self.title = title
        self.length_secs = length_secs
        self.author = author


    def __init__(self):
        return f"{self.id} {self.title} {self.length_secs}secs"