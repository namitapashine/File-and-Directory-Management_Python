import os
import shutil

from_dir = r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Downloads"
to_dir = r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Downloads\Downloadedimages"

# Ensure the destination directory exists
if not os.path.exists(to_dir):
    os.mkdir(to_dir)

# List files in the source directory
list_of_files = os.listdir(from_dir)
#print("List of files:", list_of_files)



for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    # Skip if there is no file extension (i.e., it's a directory or unknown type)
    if extension == "":
        continue

    # Check if the file is an image based on the extension
    if extension.lower() in ['.gif', '.png', '.jpg', '.jpeg']:
        # Construct full paths for the source and destination
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, file_name)

        # Move the file
        print(f"Moving {file_name} ...")
        shutil.move(path1, path2)

print("Files moved successfully.")
