import pdfplumber


word_occurrence  = {}

with pdfplumber.open('pdf1.pdf') as file:
    pages = file.pages
    for page in pages:
        print(type(page.extract_text()))
        print(page.extract_text())
        words = page.extract_text().split(" ")
        for word in words:
            if not word in word_occurrence:
                word_occurrence[word] = 1
            else:
                word_occurrence[word] += 1
print(len(words))
print(word_occurrence)







