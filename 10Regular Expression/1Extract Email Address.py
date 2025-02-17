import os
import re

directory = 'documents'

filenames = os.listdir(directory)

all_emails = []

for filename in filenames:
    filepath = os.path.join(directory,filename)
    with open(filepath,'r') as file:
        content = file.read()
        print(content)

    pattern = '[a-zA-Z0-9._-]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]{2}'
    emails  =  re.findall(pattern,content)
    all_emails.extend(emails)



    with open('all_emails.txt','w') as file:
        email = " ".join(all_emails)
        file.write(email)

print(all_emails)