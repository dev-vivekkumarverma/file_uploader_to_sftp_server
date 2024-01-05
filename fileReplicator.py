import shutil
import os
import random
import string


def copy_files_with_random_names(num_copies):
    current_directory = os.getcwd()
    original_folder = os.path.join(current_directory, "originalFiles")
    files_folder = os.path.join(current_directory, "files")

    if not os.path.exists(files_folder):
        os.makedirs(files_folder)

    if not os.path.exists(original_folder) or not os.path.isdir(original_folder):
        print("Original files folder not found or is not a directory.")
        return

    file_list = [
        file
        for file in os.listdir(original_folder)
        if os.path.isfile(os.path.join(original_folder, file))
    ]

    for file_path in file_list:
        full_file_path = os.path.join(original_folder, file_path)
        file_name, file_extension = os.path.splitext(file_path)
        for _ in range(num_copies):
            random_name = "".join(
                random.choices(string.ascii_letters + string.digits, k=10)
            )  # Generate a random name
            new_file_name = f"{random_name}{file_extension}"
            destination_path = os.path.join(files_folder, new_file_name)
            shutil.copy(full_file_path, destination_path)
            print(f"File {full_file_path} copied as {destination_path}")


# Example usage:
num_of_copies = 100  # Number of copies to create for each file

copy_files_with_random_names(num_of_copies)
