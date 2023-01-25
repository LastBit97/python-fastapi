import os
import pandas as pd
from collections import Counter
from fastapi import UploadFile


def filter_words(words: list) -> set:
    duplicate_words = [key for key, value in Counter(words).items() if value > 1]
    words_lowercase = [word.lower() for word in words]
    duplicate_words_lowercase = [word.lower() for word in duplicate_words]
    words_without_duplicates = [word for word in words_lowercase if word not in duplicate_words_lowercase]
    unique_words = set(words_without_duplicates)
    return unique_words


def combine_files(files: list[UploadFile], result_filename: str):
    li = []
    for file in files:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file, sep=';')
            li.append(df)
        elif file.filename.endswith(".json"):
            df = pd.read_json(file.file)
            li.append(df)
    concat_df = pd.concat(li, ignore_index=True)

    path = os.path.join('data/', result_filename)
    if os.path.isfile(path):
        with open(path, "r") as original_file:
            original_df = pd.read_csv(original_file, sep=';')
            concat_df = pd.concat([original_df, concat_df], ignore_index=True)

    concat_df.to_csv(os.path.join('data/', result_filename), sep=';', index=False)
