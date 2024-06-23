import os

def temp_cleaner():
    # Get the path to the %temp% folder on your system
    temp_folder = os.getenv("TEMP")

    if temp_folder:
        # List all files in the %temp% folder
        temp_files = os.listdir(temp_folder)

        # Specify the file extensions you want to delete (e.g., .txt, .tmp, .log)
        file_extensions_to_delete = ['.txt', '.tmp', '.log']

        # Iterate through the files in the folder
        for filename in temp_files:
            # Check if the file has one of the specified extensions
            if any(filename.endswith(extension) for extension in file_extensions_to_delete):
                file_path = os.path.join(temp_folder, filename)
                try:
                    # Delete the file
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    else:
        print("Could not determine the TEMP folder location.")

# Call the temp_cleaner function
temp_cleaner()
