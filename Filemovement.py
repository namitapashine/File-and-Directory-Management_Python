import os
import shutil

from_dir = r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Desktop\Namita\VisualStudio\File_Directory_Management\Temp\Source"
to_dir = r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Desktop\Namita\VisualStudio\File_Directory_Management\Temp\Destination"

# List files in the source directory
list_of_files_src = os.listdir(from_dir)
print(f"List of files in Source Directory are : {list_of_files_src}")

# Move each file from the source directory to the destination directory
for file_name in list_of_files_src:
    source_path = os.path.join(from_dir, file_name)
    destination_path = os.path.join(to_dir, file_name)
    
    # Move the file
    shutil.move(source_path, destination_path)

# List files in the destination directory after moving
list_of_files_dst = os.listdir(to_dir)

print("After Shutil.move Execution")
print(f"1. List of files in Source Directory are : {os.listdir(from_dir)}")  # Should be empty after moving all files
print(f"2. List of files in Destination Directory are : {list_of_files_dst}")
