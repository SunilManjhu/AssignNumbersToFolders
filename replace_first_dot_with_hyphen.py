import os

def replace_first_dot_with_hyphen_for_folders_and_files(path):
    for root, dirs, files in os.walk(path):
        # Update folder names
        for i, dir_name in enumerate(dirs):
            original_path = os.path.join(root, dir_name)

            if dir_name.count('.') > 0:
                new_name = dir_name.replace('.', '-', 1)
                new_path = os.path.join(root, new_name)
                os.rename(original_path, new_path)
                dirs[i] = new_name  # Update the dirs list with the new name

        # Update file names
        for i, file_name in enumerate(files):
            original_path = os.path.join(root, file_name)

            if file_name.count('.') > 1:
                new_name = file_name.replace('.', '-', 1)
                new_path = os.path.join(root, new_name)
                os.rename(original_path, new_path)
                files[i] = new_name  # Update the files list with the new name


if __name__ == "__main__":
    path_to_update = r"/path/to/your/directory"  # Change this to your desired directory path
    replace_first_dot_with_hyphen_for_folders_and_files(path_to_update)
