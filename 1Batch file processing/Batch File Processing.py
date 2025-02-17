import os
from datetime import datetime


directory = 'Files'

filenames = os.listdir(directory)

for filename in filenames:
    # print(type(filename ))
    filepath = os.path.join(directory,filename)
    with open(filepath,'r') as file:
       content =  file.read()
       words = content.split(' ')
       words_count = len(words)
       # print(words_count)
       day = datetime.now().strftime("%A")
       new_filename = f'{filename[:-4]}-{words_count}-{day}.tx'
       print(new_filename)
       # new_file_path = os.path.join(directory,new_filename)
       # os.rename(filepath,new_file_path)
       # print(f'renamed {filename} to {new_file_path}')


