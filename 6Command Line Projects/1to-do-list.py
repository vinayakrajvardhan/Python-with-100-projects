from datetime import datetime

todo_item_list = []

while True:
    todo = input("Enter the todo item: Type done to exit")

    if todo == 'done'.lower():
        break
    todo_item_list.append(todo)

content = "\n".join(todo_item_list)

day = datetime.now().strftime('%A')
filename = f'{day}.tx'
with open(filename, 'w') as file:
    file.write(content)

print(f'your file is stored at:{filename}')
