import os
import shutil

from_dir = "/Users/username/Downloads"
to_dir = "/Users/username/Documents/Document_Files"

list_of_files = os.listdir(from_dir)

print("List of files in the source directory:")
print(list_of_files)

for file_name in list_of_files:
        name, extension = os.path.splitext(file_name)

print("File name:", name)
print("File extension:", extension)
