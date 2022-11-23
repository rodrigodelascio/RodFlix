from sqlConnect import *
import time


# Release year order by

def filterYearReleased():

    orderBy = {"1": "ASC", "2": "DESC"}

    options = 0

    while options not in ["1","2"]:

        print("\n1. Ascending\n2. Descending")

        options = input("\nChoose how to order films by release date (1-2): ")

        if options not in ["1","2"]: 

            print(f"\nThis option is not valid, please select 1 or 2 from the list below.\n")
        
        else:
            break

    
    time.sleep(3)

    cursor.execute(f"SELECT * from tblfilms ORDER BY yearReleased {orderBy[options]}")
    
    row = cursor.fetchall()
    
    for record in row:
    
        print(record)


# Rating filter

def filterRating():

    filterRtng = {'1': 'U', '2': 'PG', '3': '12A', '4': '15', '5': '18'}

    options = 0 

    while options not in ["1","2","3","4","5"]:

        print("\n1. U\n2. PG\n3. 12A\n4. 15\n5. 18")

        options = input("\nChoose rating to filter films (1-5): ")

        if options not in ["1","2","3","4","5"]: 

            print("\nThis option is not valid, please select 1, 2, 3, 4 or 5 from the list below.\n")
        
        else:
            break

    
    time.sleep(3)
    
    cursor.execute(f"SELECT * from tblfilms WHERE rating = '{filterRtng[options]}'")
    
    row = cursor.fetchall()
    
    for record in row:
        print(record)


# Genre filter

def filterGenre():

    filterGnr = {'1': 'Action', '2': 'Adventure', '3': 'Animation', '4': 'Comedy', '5': 'Crime', '6': 'Drama', '7': 'Fantasy', '8': 'Kids & Family', '9': 'Romance', '10': 'Sci-fi', '11': 'Thriller', '12': 'Western'}

    options = 0 

    while options not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:

        print("\n1. Action\n2. Adventure\n3. Animation\n4. Comedy\n5. Crime\n6. Drama\n7. Fantasy\n8. Kids & Family\n9. Romance\n10. Sci-fi\n11. Thriller\n12. Western")

        options = input("\nChoose genre to filter films (1-12): ")

        if options not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:

            print("\nThis option is not valid, please select between 1 and 12 from the list below.\n")
        
        else:
            break


    time.sleep(3)
    
    cursor.execute(f"SELECT * from tblfilms WHERE genre LIKE '%{filterGnr[options]}%'")
    
    row = cursor.fetchall()
    
    for record in row:
        print(record)


# Filter all films

def filterFilms():

    options = 0

    while options not in ["1","2","3"]:

        print("\nChoose your filter from the following options:\n\n1. By genre\n2. By rating\n3. By release year")

        options = input("\nSelect category to filter or order films (1-3): ")

        if options not in ["1","2","3"]: 

            print("\nThis option is not valid, please select between 1, 2 or 3 from the list below.\n")
        
        elif options == "1":
            filterGenre()
        
        elif options == "2":
            filterRating()

        elif options == "3":
            filterYearReleased()