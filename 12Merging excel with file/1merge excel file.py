import os

import pandas as pd


directory = 'excel_file'
filenames = os.listdir(directory)

filepaths = [os.path.join(directory,filename) for filename in filenames]


dataframes = []
for filepath in filepaths:
    df = pd.read_excel(filepath)
    dataframes.append(df)

print(dataframes)


merged_df = pd.concat(dataframes,ignore_index=True)
print(merged_df)

merged_df.to_excel('excel_file/merged.xlsx',index=False)


