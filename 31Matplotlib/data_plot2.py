import matplotlib.pyplot as plt
import os


directory = 'plot'

filenames = os.listdir(directory)

data_values = []

for filename in filenames:
    filepaths = os.path.join(directory,filename)
    with open(filepaths,'r') as file:
        data = file.read()
        data_values.append(float(data))

print(data_values)

plt.figure(figsize=(10,6))
plt.plot(data_values,marker='o', linestyle='-', color='b')
plt.title('Numbers from Text Files')
plt.xlabel('File Name')
plt.ylabel('Number')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


