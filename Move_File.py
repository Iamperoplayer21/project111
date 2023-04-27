import os
import shutil

from_dir = "/Users/username/Downloads"
to_dir = "/Users/username/Documents/Document_Files"

list_of_files = os.listdir(from_dir)

print("List of files in the source directory:")
print(list_of_files)
