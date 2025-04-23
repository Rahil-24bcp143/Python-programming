
import os
import shutil

source = "sample.txt"
target_dir = "new_folder"

os.makedirs(target_dir, exist_ok=True)
shutil.copy(source, os.path.join(target_dir, "sample.txt"))
