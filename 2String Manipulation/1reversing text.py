with open('example.txt','r') as file:
    text = file.read()

words = text.split()
reversed_words = []
for word in words:
    word =  word[::-1]
    reversed_words.append(word)

with open('reversed.txt','w') as file2:
    file2.write(" ".join(reversed_words))