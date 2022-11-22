from sqlConnect import *
import time


def addFilm():

    # set empty list
    films = []

    # get user input
    title = input("Film title: ")

    yearreleased = int(input("Year released: "))

    rating = input("Rating: ")

    duration = int(input("Duration (in mins): "))

    genre = input("Genre: ")

    # append user input data to list
    films.append(title)

    films.append(yearreleased)

    films.append(rating)

    films.append(duration)

    films.append(genre)

    # insert data from list to the table
    cursor.execute("INSERT INTO tblfilms VALUES(NULL, ?,?,?,?,?)", films)

    conn.commit()

    print(f"{title} inserted to RodFlix.")

    time.sleep(3)

    # get entire record from inserted film
    cursor.execute("SELECT * FROM tblfilms")

    row = cursor.fetchall()

    for record in row:

        print(record)

# invoke subroutine
if __name__ == "__main__":

    addFilm()