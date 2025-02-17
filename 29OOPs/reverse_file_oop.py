class File:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        return text

    def write(self, content):
        with open(f'reversed_{self.file_path}', 'w') as file:
            file.write(content)


class Text:
    def __init__(self, input_text):
        self.input_text = input_text

    def reversed_word(self):
        words = self.input_text.split()
        reversed_word = []
        for word in words:
            word = word[::-1]
            reversed_word.append(word)
        reversed_text = " ".join(reversed_word)
        return reversed_text


file = File('example.txt')
content = file.read()

text = Text(content)
reversed_text = text.reversed_word()

file.write(reversed_text)
