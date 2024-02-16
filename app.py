from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

import os
os.system('clear')

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

    artist_repository = ArtistRepository(self._connection)
    artists = artist_repository.all()

    album_repository = AlbumRepository(self._connection)
    albums = album_repository.all()

    print("Welcome to the music library manager!")
    while True:
        print("\nWhat would you like to do?")
        print(" 1 - List all artists")
        print(" 2 - List all albums")
        print(" 3 - Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
           for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        elif choice == '2':
           for album in albums:
              print(f"{album.id}: {album.title} ({album.release_year})")
        elif choice == '3':
           print("Goodbye!")
           break
        else:
           print("Invalid choice, Please enter a valid option.")

if __name__ == '__main__':
    app = Application()
    app.run()


# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# # Retrieve all albums
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# # List all albums out
# for album in albums:
#     print(album)


