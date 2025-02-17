import os

directory = 'files'

filenames = os.listdir(directory)

filepaths = os.walk('files')

def get_content(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        return content

file_content = {}

for root,dir,files in filepaths:
    print(root,dir,files)
    for filename in files:
       filepath = os.path.join(root,filename)
       # print(filepath)
       content = get_content(filepath)
       if content in file_content:
           print(f"Duplicate found : {filepath}")
           print(f"original file :{file_content.get(content)}")
       else:
           file_content[content] = filepath




