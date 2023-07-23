def get_file_content(file_path):
    with open(file_path) as file:
        content = file.read()
    return content
