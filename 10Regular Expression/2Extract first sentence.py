import os
import re

directory = 'sentence'

filenames = os.listdir(directory)
first_sentence_list = []
for filename in filenames:
    filepath = os.path.join(directory,filename)
    with open(filepath,'r') as file:
        content = file.read()
    pattern = r'[A-Za-z0-9,;"\'\s\-()]+[.!?]'
    first_sentence = re.findall(pattern,content)
    first_sentence_list.append(first_sentence[0])

for firstsentence in first_sentence_list:
    print(firstsentence)

    with open('first_sentence.txt','w') as file:
          file.write("".join(first_sentence_list))