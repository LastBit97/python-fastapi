from fastapi import APIRouter
from api.service import case_sensitive_filtering

router = APIRouter()


@router.post("/filter/case_sensitive")
async def filter_case_sensitive(data: list):
    return await case_sensitive_filtering.filter_words(data)
