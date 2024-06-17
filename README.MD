# Rename Folders Script

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory where the script is located.
3. Set the selected directory path to the variable `DIR_PATH`.
4. The script will rename the folders in the specified directory according to the selected normalization function.
5. Follow the prompts to enter the new names for the folders.

```bash
python main.py
```

## Example

Let's say you have a directory structure like this:

```
- project
    - folder1
    - folder2
    - folder3
```

And you want to rename `folder1` to `new_folder1`, `folder2` to `new_folder2`, and `folder3` to `new_folder3`.
Simply run the script, enter the new names when prompted, and the script will rename the folders accordingly.

## Configuration

You can customize the behavior of the script by providing your own normalization functions. These functions should take a string as input and return a string.

## Notes

- Make sure you have Python installed on your machine.
- This script only renames folders, not files.
- Double-check the new names before proceeding.
