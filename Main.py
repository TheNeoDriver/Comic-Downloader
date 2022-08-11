from Apps.ComicDownloader import download_comics
from Apps.ComicPagesEnhancer import enhance_pages
from Utilities.Utilities import repeater

@repeater
def quit_program():
    val = None

    print("\nAre you sure you want to close the program? (Y/N)")

    choice = input("-- ")

    if choice.lower() == "y":
        val = True
    elif choice.lower() == "n":
        val = False
    else:
        print("\nThat answer isn't correct. Try again.")
    
    return val


@repeater
def operations():
    val = None

    print("\nChoose a operation:", "\n1.- Download comics.")
    print("2.- Enhance pages of comics.", "\n3.- Quit. \n")
    
    choice = input("-- ")

    match choice.strip():
        case "1":
            download_comics()
        case "2":
            enhance_pages()
        case "3":
            val = quit_program()
            val = None if not val else True
        case _:
            print("That operation doesn't exist. Try again.")
        
    return val


def main():
    print("This application was created by TheNeoDriver.")
    print("License: Public Domain")
    operations()
    print("\nSee you next time!")
    return


if __name__ == '__main__':
    main()
