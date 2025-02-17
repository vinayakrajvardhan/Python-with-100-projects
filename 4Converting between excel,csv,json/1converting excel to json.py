import openpyxl
import pandas

df = pandas.read_excel('europe.xlsx')
df.to_json('euorpe.json',orient='records',lines=True)