with open('snowwhite.txt','r') as file:
    words = file.read()
    capatalize_word = []
    content  = words.split(' ')
    for word in content:
        capatalize_word.append(word.title())

with open('capatalize.txt','w') as file:
    file.write(" ".join(capatalize_word))