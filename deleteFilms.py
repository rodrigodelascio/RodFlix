from sqlConnect import *
from readFilms import readFilmList
import time


def deleteFilm():

    idField = int(input("Insert the FilmID to delete the film: "))

    cursor.execute(f"DELETE FROM tblfilms WHERE FilmID={idField}")

    conn.commit()

    print(f"Film with ID {idField} deleted from table.")

    time.sleep(3)

    readFilmList()

if __name__ == "__main__":
    
    deleteFilm()