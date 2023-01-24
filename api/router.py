from fastapi import APIRouter, UploadFile, HTTPException
from api import service

router = APIRouter()


@router.post("/filter/case_sensitive")
async def filter_case_sensitive(data: list):
    return await service.filter_words(data)


@router.post("/upload/{filename}")
async def combine_data_files(files: list[UploadFile], filename):
    error_files = []
    for file in files:
        if not file.filename.endswith((".csv", ".json")):
            error_files.append(file.filename)
    if error_files:
        raise HTTPException(status_code=415, detail=error_files)
    return await service.combine_files(files, filename)

