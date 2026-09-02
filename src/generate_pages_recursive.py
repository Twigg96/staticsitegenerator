from generate_page import generate_page
import os


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    new_files = os.listdir(dir_path_content)
    for file in new_files:
        source_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(source_path):
            name, extension = os.path.splitext(dest_path)
            complete_path = name + ".html"
            generate_page(source_path, template_path, complete_path, basepath)

        else:
            os.mkdir(dest_path)
            generate_pages_recursive(source_path, template_path, dest_path, basepath)
