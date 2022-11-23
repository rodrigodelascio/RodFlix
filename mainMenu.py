from readFilms import readFilmList
from insertFilm import addFilm
from updateFilm import updateFilm
from deleteFilms import deleteFilm
from selectByFilter import filterFilms


def menuOptions():

    options = 0
    
    while options not in ["1", "2", "3", "4", "5", "6"]:
        print(
            "\nRodFlix Menu Options\n\n1. View all films\n2. Add film\n3. Update film information\n4. Delete film\n5. Filter films\n6. Exit"
        )
        
        options = input("\nEnter one of the options above: ")
        
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"The option {options} is not a valid choice, please select from the list below.\n")
    
    return options


mainProgram = True

while mainProgram:
    mainMenu = menuOptions()

    if mainMenu == "1":
        readFilmList()
    elif mainMenu == "2":
        addFilm()
    elif mainMenu == "3":
        updateFilm()
    elif mainMenu == "4":
        deleteFilm()
    elif mainMenu == "5":
        filterFilms()
    else:
        mainProgram = False

print("\nExiting program...\n")