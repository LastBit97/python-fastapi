from io import BytesIO, StringIO
import pandas as pd
from fastapi import UploadFile


async def combine_files(files: list[UploadFile]):
    li = []
    for file in files:
        if file.filename.endswith(".csv"):
            content = await file.read()
            data = BytesIO(content)
            df = pd.read_csv(data, sep=';')
            li.append(df)
            data.close()
        elif file.filename.endswith(".json"):
            content = await file.read()
            s = str(content, 'utf-8')
            data = StringIO(s)
            df = pd.read_json(data)
            li.append(df)
            data.close()
    dataframe = pd.concat(li, axis=0, ignore_index=True)
    print(dataframe)
    dataframe.to_csv("C:/Users/ostbi/pytnon/python-fastapi/data/file_name.csv", sep=';')
