import os
import shutil

# Define the source directory 
from_dir = (r"C:\Users\kumar\Dropbox\My PC (LAPTOP-TIMLB0BS)\Downloads")

# Define  target directories for each file types

to_image_dir = os.path.join(from_dir, "Images")
to_pdf_dir = os.path.join(from_dir, "PDFs")
to_text_dir = os.path.join(from_dir, "TextFiles")
to_excel_dir = os.path.join(from_dir, "ExcelFiles")
to_video_dir = os.path.join(from_dir, "Videos")
to_python_dir = os.path.join(from_dir, "PythonFiles")
to_zip_dir = os.path.join(from_dir, "ZipFiles")
to_rar_dir = os.path.join(from_dir, "RarFiles") 
to_other_dir = os.path.join(from_dir, "Others")

# Create target directories if they don't exist
for dir_path in [to_image_dir, to_pdf_dir, to_text_dir, to_excel_dir, to_video_dir, to_python_dir, to_zip_dir, to_rar_dir, to_other_dir]:
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

# List files in the source directory
list_of_files = os.listdir(from_dir)
print("List of files:", list_of_files)

# Segregate files based on their extensions
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    path1 = os.path.join(from_dir, file_name)

    # Skip if there is no file extension
    if extension == "":
        continue

    # Check the file type and move it to the corresponding directory
    if extension.lower() in ['.gif', '.png', '.jpg', '.jpeg']:
        print(f"Moving {file_name} to Images...")
        shutil.move(path1, to_image_dir)
    elif extension.lower() == '.pdf':
        print(f"Moving {file_name} to PDFs...")
        shutil.move(path1, to_pdf_dir)
    elif extension.lower() in ['.txt', '.doc', '.docx']:
        print(f"Moving {file_name} to TextFiles...")
        shutil.move(path1, to_text_dir)
    elif extension.lower() in ['.xls', '.xlsx']:
        print(f"Moving {file_name} to ExcelFiles...")
        shutil.move(path1, to_excel_dir)
    elif extension.lower() in ['.mp4', '.mp3', '.avi']:
        print(f"Moving {file_name} to Videos...")
        shutil.move(path1, to_video_dir)
    elif extension.lower() == '.py':
        print(f"Moving {file_name} to PythonFiles...")
        shutil.move(path1, to_python_dir)
    elif extension.lower() == '.zip':
        print(f"Moving {file_name} to ZipFiles...")
        shutil.move(path1, to_zip_dir)
    elif extension.lower() == '.rar':
        print(f"Moving {file_name} to RarFiles...")
        shutil.move(path1, to_rar_dir)  # Move to RAR files directory
    else:
        print(f"Moving {file_name} to Others...")
        shutil.move(path1, to_other_dir)

print("Files segregated successfully.")