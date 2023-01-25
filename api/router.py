import os
import logging

from fastapi import APIRouter, UploadFile, HTTPException, Request, Response
from fastapi.responses import FileResponse
from api import service

router = APIRouter()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt='%H:%M:%S',
    )


@router.post("/filter/case_sensitive")
def filter_case_sensitive(data: list, request: Request):
    logging.info(f"request {request.method} {request.url}")
    return service.filter_words(data)


@router.post("/upload/{filename}")
def combine_data_files(files: list[UploadFile], filename: str, request: Request):
    logging.info(f"request {request.method} {request.url}")
    error_files = []
    for file in files:
        if not file.filename.endswith((".csv", ".json")):
            error_files.append(file.filename)
    if error_files:
        raise HTTPException(status_code=415, detail=error_files)
    service.combine_files(files, filename)
    return {"filename": filename}


@router.get("/load/{filename}")
def load_file(filename: str, request: Request):
    logging.info(f"request {request.method} {request.url}")
    path = os.path.join('data/', filename)
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail="file not found: " + filename)
