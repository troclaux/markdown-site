from generate_html_page import *
from textnode import *

if __name__ == "__main__":
    source = "./public"
    destination = "./test"

    copy_dir_content(source, destination)
