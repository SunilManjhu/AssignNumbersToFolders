import os


def get_sorted_directories(directory):
    """
    Get a sorted list of directories in the given directory.
    """
    return sorted(
        [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    )


def extract_and_rename_folder(directory, folder_name, separator, numeric_prefix_counter):
    """
    Extracts information from the folder name, generates a new name with a numeric prefix,
    and renames the folder.
    """
    folder_path = os.path.join(directory, folder_name)
    # Find the index of the separator character
    index = folder_name.find(separator)
    if index != -1:
        numeric_prefix_counter += 1
        # Extract the substring after the separator
        new_name = folder_name[index + 1 :].strip()

        # Create the new folder name with a numeric prefix
        numeric_prefix = f"{numeric_prefix_counter:02d} - "
        new_name_with_prefix = numeric_prefix + new_name

        # Create the new path with the updated folder name
        new_path = os.path.join(directory, new_name_with_prefix)

        # Rename the folder
        os.rename(folder_path, new_path)
        print(f"Renamed: {folder_path} -> {new_path}")

    return numeric_prefix_counter


def rename_folders(directory, separator="-"):
    """
    Rename folders in the given directory using a numeric prefix.
    """
    numeric_prefix_counter = 0
    directories = get_sorted_directories(directory)

    for folder_name in directories:
        numeric_prefix_counter = extract_and_rename_folder(
            directory, folder_name, separator, numeric_prefix_counter
        )


# Replace 'D:\\VSCode\\AssignNumbersToFolders' with your actual directory path
directory_path = r"path\to\folders"
rename_folders(directory_path)
