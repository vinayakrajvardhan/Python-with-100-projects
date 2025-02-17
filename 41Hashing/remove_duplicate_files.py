import os
import hashlib

filepath = os.walk('files1')

def get_content(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        has_value = hashlib.sha256(content).hexdigest()
        return has_value

file_contents = {}

for root, dirs, files in filepath:
    for filename in files:
        filepath = os.path.join(root, filename)
        hash_value = get_content(filepath)
        if hash_value in file_contents:
            os.remove(filepath)
        else:
            file_contents[hash_value] = filepath





