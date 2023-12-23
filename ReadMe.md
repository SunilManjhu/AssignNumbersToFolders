# Folder Renamer

The **Folder Renamer** is a Python script designed to rename folders within a specified directory. It extracts information from existing folder names, adds a numeric prefix, and then renames the folders accordingly.

## Usage

1. **Installation:**
   - Clone this repository or download the `folder_renamer.py` script.

2. **Configuration:**
   - Open the `folder_renamer.py` script in a text editor.
   - Replace the `directory_path` variable with the actual path of the directory containing the folders you want to rename.

3. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using the following command:
     ```bash
     python folder_renamer.py
     ```

4. **View Results:**
   - The script will print information about the renaming process, including the old and new folder names.

## Modular Structure

The program has been modularized for better readability and maintainability. Key functions include:

- **get_sorted_directories(directory):**
  - Returns a sorted list of directories in the given directory.

- **extract_and_rename_folder(directory, folder_name, separator, numeric_prefix_counter):**
  - Extracts information from the folder name, generates a new name with a numeric prefix, and renames the folder.

- **rename_folders(directory, separator="-"):**
  - Renames folders in the given directory using a numeric prefix. It utilizes the above functions for a modular approach.

## Example

Suppose you have the following folders:

    01 - First Folder
    02 - Second Folder
    03 - Third Folder


After running the script, the folders will be renamed with numeric prefixes:

    01 - First Folder -> 01 - First Folder
    02 - Second Folder -> 02 - Second Folder
    03 - Third Folder -> 03 - Third Folder


## Note

- Ensure that you have the necessary permissions to rename folders in the specified directory.

- Backup important data before running the script, as it modifies folder names.

Feel free to customize the script and adapt it to your specific needs!

