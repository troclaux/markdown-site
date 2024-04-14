from block_functions import *


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
