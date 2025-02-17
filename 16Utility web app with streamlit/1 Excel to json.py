import pandas


df = pandas.read_excel('europe.xlsx')

json_record = df.to_json('europe.json',orient='records')

