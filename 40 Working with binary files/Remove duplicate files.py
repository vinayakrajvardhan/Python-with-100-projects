import os

directory = 'files1'

filenames = os.walk(directory)


def get_content(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        return content


file_content = {}

for root, directory, files in filenames:
    # print(root, directory, files)

    for file in files:
        # print(file)
        filepath = os.path.join(root, file)
        print(filepath)
        content = get_content(filepath)
        print(content)
        if content in file_content:
            os.remove(filepath)
        else:
            file_content[content] = filepath
