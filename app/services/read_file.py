def get_file_content(file_path):
    users = []
    with open(file_path) as file:
        content = file.read()
    users = content.split("\n")
    return users
