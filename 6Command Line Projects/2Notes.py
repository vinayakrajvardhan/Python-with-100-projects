from datetime import datetime

notes_item = []


while True:
    note = input("Enter the notes: Type 'exit' to quit:")
    if note == 'exit'.lower():
        break
    notes_item.append(note)

content = "\n".join(notes_item)
day = datetime.now().strftime('%A')
filename = f'{day}.txt'

with open(filename,'w') as file:
    file.write(content)