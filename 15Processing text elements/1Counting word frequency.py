import os

directory = 'text_files'

filenames = os.listdir(directory)

dictionary_frequency = {}

for filename in filenames:
    filepath = os.path.join(directory,filename)

    with open(filepath,'r') as file:
        contents = file.read()
    print(contents)

    for word in contents.split():
        if not word in dictionary_frequency:
            dictionary_frequency[word] = 1
        else:
            dictionary_frequency[word] +=1

    with open('count_frequency.txt','w') as file:
        for word,item in dictionary_frequency.items():
           file.write(f'{word}:{item}\n')

print(dictionary_frequency)
