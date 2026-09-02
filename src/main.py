from textnode import *
import os, shutil, sys
from generate_pages_recursive import generate_pages_recursive


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
    basepath = sys.argv
    check_directory("docs")
    copy_content("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()
