import os
import shutil

from block_functions import *


# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree

# os.listdir
# os.path.join
# os.path.isfile
# pathlib.Path


def copy_dir_content(src, dest):
    if os.path.exists(dest):
        print(f"removing {dest} folder")
        shutil.rmtree(dest)
    print(f"creating {dest} folder")
    os.mkdir(dest)
    for item in os.listdir(src):
        source_item_path = os.path.join(src, item)
        destination_item_path = os.path.join(dest, item)
        if os.path.isfile(source_item_path):
            print(f"copying {source_item_path} to {destination_item_path}")
            shutil.copy(source_item_path, destination_item_path)
        else:
            print(f"copying {source_item_path} directory to {destination_item_path}")
            copy_dir_content(source_item_path, destination_item_path)


def generate_pages_recursive(src, templ, dest):
    for item in os.listdir(src):
        source_item_path = os.path.join(src, item)
        if os.path.isfile(source_item_path) and item[-3:] == ".md":
            print(f"copying {source_item_path} to {dest}")
            generate_page(source_item_path, templ, f"{dest}/{item[:-3]}.html")
        else:
            print(f"copying {source_item_path} directory to {dest}")
            generate_pages_recursive(source_item_path, templ, f"{dest}/{item}")


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise Exception("No title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {dest_path} from {from_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    with open(template_path, "r") as f:
        template = f.read()
        converted_content = template.replace("{{ Title }}", title).replace(
            "{{ Content }}", html
        )

    with open(dest_path, "w") as f:
        f.write(converted_content)
