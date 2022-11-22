from sqlConnect import *
from readFilms import readFilmList
import time


def updateFilm():

    idField = int(input("Insert the FilmID to update the film: "))

    fieldName = input("Which field would you like to update (Title, YearReleased, Rating, Duration, Genre)? Make your choice: ").title()

    newFieldValue = input(f"Enter the new value for {fieldName}: ")

    newFieldValue = "'" + newFieldValue + "'"

    print(f"The new field value inserted is {newFieldValue}.")


    cursor.execute(f"UPDATE tblfilms SET {fieldName} = {newFieldValue} WHERE FilmID = {idField}")

    conn.commit()


    print(f"Film with ID {idField} updated in table.")

    time.sleep(3)

    readFilmList()


if __name__ == "__main__":

    updateFilm()