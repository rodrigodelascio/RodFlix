from sqlConnect import *


def readFilmList():
    cursor.execute("SELECT * FROM TBLFILMS")
    row = cursor.fetchall()

    for record in row:
        print(record)


if __name__ == "__main__":
    
    readFilmList()