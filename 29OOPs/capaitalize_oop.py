class File:
    def __init__(self,file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path,'r') as file:
            text = file.read()
            return text


    def write(self,content):
        with open(f'capitalize_{self.file_path}','w') as file:
            file.write(content)


class Text:
    def __init__(self,input_text:str):
        self.input_text = input_text

    def capitalize(self):
        words = self.input_text.split(".")
        capitalize_word = []
        for word in words:
            word.capitalize()
            capitalize_word.append(word)
        capatilize_text  = " ".join(capitalize_word)
        return capatilize_text

file = File('example.txt')
content = file.read()
text = Text(content)
capitalize_text = text.capitalize()
file.write(capitalize_text)