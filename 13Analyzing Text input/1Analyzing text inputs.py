text = input("Enter a block of text for analysis:\n")
print("Text analysis results")
print("-" * 20)
character = len(text)

def remove_punctuation(text:str):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in punctuation:
        text = text.replace(char,"")
    return text

words = len(text.split(" "))

sentences = text.count('.') + text.count('!') + text.count('?')

word_frequency = {}
word_list = remove_punctuation(text).lower().split(" ")







for word in word_list:
    if not word in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

most_frequent_word = max(word_frequency,key=word_frequency.get)

length_words = [len(word) for word in word_list]

average_words_length = sum(length_words)/len(length_words)

average_sentence_length = words/sentences


print(f'Total character is {character}')
print(f'Total words is {words}')
print(f'Total sentences is {sentences}')
print(f'Most frequent word is :{most_frequent_word} (used {word_frequency[most_frequent_word]} times )')
print(f'Average words length {average_words_length}')
print(f'Average sentences length {average_sentence_length}')






