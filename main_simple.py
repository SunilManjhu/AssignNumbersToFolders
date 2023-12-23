import os


def rename_folders(directory, separator="-"):
    # Get a sorted list of directories
    directories = sorted(
        [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    )

    numeric_prefix_counter = 0
    for folder_name in directories:
        folder_path = os.path.join(directory, folder_name)
        # Find the index of the separator character
        index = folder_name.find(separator)
        if index != -1:
            numeric_prefix_counter = numeric_prefix_counter + 1
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


# Replace 'D:\\VSCode\\AssignNumbersToFolders' with your actual directory path
directory_path = r"path\to\folders"
rename_folders(directory_path)