import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def get_sorted_items(directory, is_folder=True):
    """
    Get a sorted list of items (folders or files) in the given directory.
    """
    return sorted(
        [item for item in os.listdir(directory) if (is_folder and os.path.isdir(os.path.join(directory, item))) or (not is_folder and os.path.isfile(os.path.join(directory, item)))],
        key=natural_sort_key
    )


def extract_and_rename_item(directory, item_name, separator, numeric_prefix_counter, is_folder=True):
    """
    Extracts information from the item name, generates a new name with a numeric prefix,
    capitalizes the first character, and renames the item.
    """
    item_path = os.path.join(directory, item_name)
    # Find the index of the separator character
    index = item_name.find(separator)
    if index != -1:
        numeric_prefix_counter += 1
        # Extract the substring after the separator
        new_name = item_name[index + 1 :].strip()

        # Capitalize the first character
        new_name = new_name.capitalize()

        # Create the new item name with a numeric prefix
        numeric_prefix = f"{numeric_prefix_counter:02d} - "
        new_name_with_prefix = numeric_prefix + new_name

        # Create the new path with the updated item name
        new_path = os.path.join(directory, new_name_with_prefix)

        # Rename the item
        # Check if the new path already exists
        if not os.path.exists(new_path):
            # Rename the item
            os.rename(item_path, new_path)
            print(f"Renamed: {item_path} -> {new_path}")
        else:
            print(f"Skipped renaming, path already exists: {new_path}")


    return numeric_prefix_counter


def rename_items_recursive(directory, separator="-", is_folder=True):
    """
    Rename items (folders or files) in the given directory and its subdirectories using a numeric prefix.
    """
    for root, _, items in os.walk(directory):
        numeric_prefix_counter = 0  # Reset the counter for each new directory
        # Only process items (folders or files)
        for item_name in get_sorted_items(root, is_folder):
            numeric_prefix_counter = extract_and_rename_item(
                root, item_name, separator, numeric_prefix_counter, is_folder
            )


# Replace 'D:\\VSCode\\AssignNumbersToFolders' with your actual directory path
directory_path = r"/path/to/your/directory"
										

# Rename folders
rename_items_recursive(directory_path, is_folder=True)

# Rename files
rename_items_recursive(directory_path, is_folder=False)
