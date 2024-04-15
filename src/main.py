from generate_html_page import *
from textnode import *

if __name__ == "__main__":
    blob_src_path = "./static"
    blob_dest_path = "./public/static"
    copy_dir_content(blob_src_path, blob_dest_path)

    src_path = "./content"
    template = "./template.html"
    dest = "./public"
    generate_pages_recursive(src_path, template, dest)
