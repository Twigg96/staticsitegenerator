from textnode import *
import os, shutil
from generate_page import generate_page


def check_directory(destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)


def copy_content(source, destination):
    items = os.listdir(source)
    for item in items:
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copying {source_path} to {destination_path}")
        else:
            os.mkdir(destination_path)
            copy_content(source_path, destination_path)


def main():
    check_directory("public")
    copy_content("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


main()
