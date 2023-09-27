import pandas as pd
import os

path = '/Users/branata.kurniawan/Documents/personal/ICT601/combine/folder'
file_list = os.listdir(path)

combine = []

for file in file_list:
    if file.endswith('.xlsx'):
        df1 = pd.read_excel(os.path.join(path, file))
        df2 = pd.read_excel(os.path.join(path, file), skiprows=13)
        # Do something with the dataframe, such as print or process the data

        state = df1.iloc[4, 1]
        industry = df1.iloc[6, 1]

        df2['State'] = state
        df2['Industry'] = industry
        combine.append(df2)

combine_df = pd.concat(combine)
combine_df.to_excel('combine.xlsx', index=False)
        