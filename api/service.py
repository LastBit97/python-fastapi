import os
import pandas as pd
from collections import Counter
from io import BytesIO
from fastapi import UploadFile
from config import ROOT_DIR


async def filter_words(words: list) -> set:
    duplicate_words = [key for key, value in Counter(words).items() if value > 1]
    words_lowercase = [word.lower() for word in words]
    duplicate_words_lowercase = [word.lower() for word in duplicate_words]
    words_without_duplicates = [word for word in words_lowercase if word not in duplicate_words_lowercase]
    unique_words = set(words_without_duplicates)
    # print(words)
    # print(duplicate_words)
    # print(words_lowercase)
    # print(duplicate_words_lowercase)
    # print(words_without_duplicates)
    # print(unique_words)
    return unique_words


async def combine_files(files: list[UploadFile], result_filename: str):
    li = []
    for file in files:
        content = await file.read()
        with BytesIO(content) as data:
            if file.filename.endswith(".csv"):
                df = pd.read_csv(data, sep=';')
                li.append(df)
            elif file.filename.endswith(".json"):
                df = pd.read_json(data)
                li.append(df)
    combined_df = pd.concat(li, ignore_index=True)
    print(combined_df)
    combined_df.to_csv(os.path.join(ROOT_DIR, 'data/', result_filename), sep=';')
