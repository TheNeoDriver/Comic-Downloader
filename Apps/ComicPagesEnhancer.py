from Apps.ComicPagesEnhancerCore import Core
from Utilities.Utilities import repeater
from Utilities.ProgressBar import progressbar
import os
from PIL import Image


@repeater
def select_path_or_file(path = ".", request = "Choose the number"):
    result_path = None

    folders = os.scandir(path)
    folders = [folder.name for folder in folders]

    names = ""
    for i, folder in enumerate(folders):
        names += f"\n{i+1}.- {folder}."

    print(f"\n{request}: {names} \n")
    choice_num = input("-- ")

    if not choice_num.strip().isdigit():
        print("\nThat isn't a number. Try Again")
    
    else:
        choice_num = int(choice_num) - 1
        result_path = f"{path}/{folders[choice_num]}"

    return result_path


@repeater
def select_number(request):
    value = None

    number = input(f"{request}:- ")

    if number.strip().isdigit():
        value = int(number)
    else:
        print("\nThat isn't a number. Try Again.")

    return value


@repeater
def change_parameters(image_reference_path):
    operations = None

    img = Image.open(image_reference_path)

    contrast = select_number("Enter the level of contrast")
    brightness = select_number("Enter the level of brightness")
    color = select_number("Enter the level of color")

    img = Core.change_brightness(img, brightness)
    img = Core.change_contrast(img, contrast)
    img = Core.change_color(img, color)
    img.show()

    ready = input("Are you satisfied with the change? (Y/N):- ")
    ready = ready.lower()
    
    if ready == "y":
        operations = {
            Core.change_brightness: brightness,
            Core.change_contrast: contrast,
            Core.change_color: color
        }
    else:
        print("Ok. Let's do it again!")

    img.close()

    return operations


def enhance(issue_path, operations):
    images_paths = os.scandir(issue_path)
    images_paths = [f"{issue_path}/{image.name}" for image in images_paths]

    for img_path in images_paths:
        image = Image.open(img_path)

        for key, value in operations.items():
            image = key(image, value)
        
        image.save(img_path)

    return


def enhance_pages():
    folders = os.scandir(".")
    folders = [folder.name.lower() for folder in folders]

    if not "comics" in folders:
        print("\nThe comics folder doesn't exist. Download any comic and try again.")
        return

    request = "Select the number comic you want for enhance the quality of its pages"
    comic_path = select_path_or_file("./Comics", request)

    request = "Select the number of the issue you want"
    issue_path = select_path_or_file(comic_path, request)

    request = "Select the number of the image you want to use as reference to apply the changes to all images."
    image_reference_path = select_path_or_file(issue_path, request)

    operations = change_parameters(image_reference_path)
    enhance(issue_path, operations)

    return
