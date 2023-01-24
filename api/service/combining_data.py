import pandas as pd
from glob import glob
import os

li = []
all_files_csv = glob('*.csv')

for filename in all_files_csv:
    df = pd.read_csv(filename, sep=';', index_col=None, header=0)
    li.append(df)

all_files_json = glob('*.json')

for filename in all_files_json:
    df = pd.read_json(filename)
    li.append(df)

dataframe = pd.concat(li, axis=0, ignore_index=True)

print(dataframe)
# dataframe.to_csv("file_name.csv", sep=';')
