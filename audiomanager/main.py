"""
App: audio manager
author: chris codina
functionalilty:
     -register albums
     -register songs 
     -display catalog
"""

#import 

from display import print_menu, clear , print_header
from album import Album 
from song import Song
import pickle

#globals
catalog = []

#functions 
def serialize_data():
    try:
        writter = open('songmanager.data', 'wb') # WB write binary
        pickle.dump(catalog, writter)
        writter.close()
        print(" **Darta saved!!")

    except:
        print("**error: data was not saved!")


def deserialize_data():
    try:
        reader = open('songManager.data', 'rb') # rb read binary
        temp_list = pickle.load(reader)
        reader.close()

        for item in temp_list:
            catalog.append(item)

        print(f"loaded {len(catalog)} album")    

    except:
        print("**error: no data was loaded!")


def register_album(): 
    print_header("register album")

    title = input("provide the title:  ")
    genre = input("provide the genre: ")
    artist = input("provide the artists name: ")
    price = float(input("provide the price: "))
    release_year = int(input("provide release year: "))
 
    id = 1 
    if(len(catalog) > 0):
        id = catalog[-1].id + 1
        

    album = Album(id, title, artist, genre, price, release_year)
    catalog.append(album)
    print("ALBUM SAVED!")

def print_catalog(show_songs):
    print_header("your current catalog")
    # iterate the list and print each album 

    for album in catalog:
        print(album)

    if(show_songs):
        print("-" * 30)
        id = input("select an album to see the songs, or [x] to close")
        if(id == 'x'): return

        try:
    # find the album with that id
            the_id = int(id)

            found = False
            for album in catalog:
                if(album.id == the_id):
                    found = True
                    print_header("songs of the album: " + album.title)
            # print the songs of album
                for song in album.songs:
                    print(song)

                return album # return the selected album

            if(not found):
                print("*error: invalid id, try again")

        except:
            print("invalid entry, try again")


def register_song():
    print_catalog(False)
    id = int(input("please select an id: "))

    # validate the id 
    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            print_header("register a song" + album.title)
            title = input("provide the title: ")
            length_secs = input("provide the length in secs: ")
            author = input("provide the author: ")

            id = 1 
            if(len(album.songs) > 0):
                id = album.songs[-1].id + 1

            song = Song(id, title, length_secs, author)
            album.songs.append(song)
            
    if(not found):
        print("**ERROR: inlaid id try again ")

def delete_song():
    album = print_catalog(True)
    print("-" * 30)
    id = int (input("select the id of the song to delete: "))

    found = False
    for song in album.songs:
        if(song.id == id):
            found = True
            album.songs.remove(song)
            print("song removed!")

    if(not found):
        print("*error: invalid id, try again")
    #instructions
deserialize_data()
input("press enter to continue...")

option = ''    
while(option != 'q'):
    clear()   
    print_menu()
    option = input("please select an option: ")

    if(option == 'q'):
        break 

    if(option == '1'):
        register_album()
        serialize_data()

    if(option == '2'):
        register_song()    
        serialize_data()

    if(option == '3'):
        print_catalog(True)


    if(option == '8'):
        delete_song()
        serialize_data()

    input("press enter to continue...")  

print("goodbyte")             