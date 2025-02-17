import os

directory = 'text_files'
filenames = os.listdir(directory)

for filename in filenames:
    filepaths = os.path.join(directory, filename)

    with open(filepaths,'r') as file:
        content = file.read()

    print(content)

    with open('merged.txt','w') as file:
        file.write(content)




