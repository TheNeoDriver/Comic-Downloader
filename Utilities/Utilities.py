from os import scandir, mkdir


def repeater(func):
    """Repeats a function call until the function
    returns values other than None.
    Returns the values of the function"""

    def wrapper(*args, **kwargs):
        flag = True
        while flag:
            val = func(*args, **kwargs)
            flag = False if not (val is None) else True
        return val
    
    return wrapper


def create_folder_in_path(path = "", folder_name = ""):
    folder_name = folder_name.strip()

    path_folders = scandir(path)
    path_folders = [folder.name.lower() for folder in path_folders]

    if not folder_name.lower() in path_folders:
        mkdir(f"{path}/{folder_name}")

    return
