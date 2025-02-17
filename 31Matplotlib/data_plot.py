import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

file_path = 'data.txt'
with open(file_path,'r') as file:
    datas = file.readlines()


datas_values = []

for data in datas:
    value = float(data.strip('\n'))
    datas_values.append(value)

print(datas_values)

plt.figure(figsize=(10,6))
plt.plot(datas_values,marker = 'o',linestyle='-')
plt.show()