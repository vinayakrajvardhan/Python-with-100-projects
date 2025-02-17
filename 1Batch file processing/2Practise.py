import os
from datetime import datetime

directory = 'Files'

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory,filename)
    with open(filepath,'r') as file:
        content = file.read()
        words_count = content.split(' ')
        words = len(words_count)
        # print(words)
        day = datetime.now().strftime("%A")
        new_filename = f'{filename[:-4]}-{words}-{day}.txt'
        print(new_filename)
        # new_filepath=os.path.join(directory,new_filename)
        # os.rename(filepath,new_filepath)


