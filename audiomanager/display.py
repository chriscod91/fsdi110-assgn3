import os

def print_menu():
    print("-"*30)
    print("** audio manager **")
    print("-" * 30)

    print("[1] register album")
    print("[2] register song")
    print("[3] print catalog")
    print("[5] Count all the song in the system")
    print("[6] Total $ in the catalog")

    print("[7] Delete album")# only delete if there are no songs on it 
    print("[8] Delete Song")

    print("[9] print the most expensive album")# only delete if there are no songs on it 
    print("[10] print the unique genres")

    print("[q] quit")


def clear():
    if(os.name == 'nt'):
        os.system('cls')

    else: 
        os.system('clear')

    #os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text):
    clear()
    print("-" * 30)
    print(text)
    print("-" * 30)



       