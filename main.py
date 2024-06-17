import os
from typing import Callable

def rename_folders(path: str, normalize_function: Callable[[str], str]) -> None:

    """
    This function renames all the folders in the given path using the normalize_function. 
    The normalize_function should take a string as input and return a string.

    Args:
        path (str): The path to the directory containing the folders to be renamed
        normalize_function (Callable[[str], str]): A function that takes a string as input and returns a string

    Returns:
        None
    """

    for folder in os.listdir(path):

        if os.path.isdir(os.path.join(path, folder)):
            old_name: str = os.path.join(path, folder)
            new_name: str = os.path.join(path, normalize_function(folder))
            os.rename(old_name, new_name)
            print(f"renamed folder: {old_name} -> {new_name}")
        

def normalize_filename(file_name: str) -> str:
    """
    This function normalizes a file name by converting it to lowercase.

    Args:
        file_name (str): The file name to be normalized
    Returns:
        str: The normalized file name
    """
    return file_name.lower()


def main() -> None:
    DIR_PATH = "../leetcode-solutions"
    rename_folders(DIR_PATH, normalize_filename)


if __name__ == "__main__":
    main()