from fastapi import APIRouter, UploadFile, HTTPException
from api.service import case_sensitive_filtering
from api.service import combining_data
import pandas as pd
from io import BytesIO

router = APIRouter()


@router.post("/filter/case_sensitive")
async def filter_case_sensitive(data: list):
    return await case_sensitive_filtering.filter_words(data)


@router.post("/upload")
async def combine_data_files(files: list[UploadFile]):
    error_files = []
    for file in files:
        if not file.filename.endswith((".csv", ".json")):
            error_files.append(file.filename)
    if error_files:
        raise HTTPException(status_code=415, detail=error_files)
    await combining_data.combine_files(files)
    return {"filenames": [file.filename for file in files]}


        # contents = await file.read()
        # data = BytesIO(contents)
        # df = pd.read_csv(data)
        # print(df)
        # data.close()

