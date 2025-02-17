numbers_input = input("Enter a series of numbers separated by spaces:\n")
list_number = []

most_frequency_number = {}

for i in numbers_input.split():
    list_number.append(int(i))
print(list_number)
total_number = len(list_number)
sum = 0

for i in list_number:
    sum+= i

for number in list_number:
    if not number in most_frequency_number:
        most_frequency_number[number] = 1
    else:
        most_frequency_number[number]+=1

max_frequency = max(most_frequency_number,key=most_frequency_number.get)

average_number = sum / total_number

print('Number Analysis Results')
print('-'*20)
print(f'Total number is {total_number}')
print(f'Sum of number is {sum}')
print(most_frequency_number)
print(f'Most frequency number: {max_frequency} (appears {most_frequency_number[max_frequency]}  times)')
print(f'Average number is {average_number}')