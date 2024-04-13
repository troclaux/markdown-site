import os
import shutil

from textnode import *

# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree


def copy_dir_content(src, dest):
    if os.path.exists(dest):
        print(f"removing {dest} folder")
        shutil.rmtree(dest)
    print(f"creating {dest} folder")
    os.mkdir(dest)
    for item in os.listdir(src):
        source_item_path = f"{src}/{item}"
        if os.path.isfile(source_item_path):
            print(f"copying {source_item_path} to {dest}")
            shutil.copy(source_item_path, dest)
        else:
            print(f"copying {source_item_path} directory to {dest}")
            copy_dir_content(source_item_path, f"{dest}/{item}")


if __name__ == "__main__":
    source = "./public"
    destination = "./test"

    copy_dir_content(source, destination)
