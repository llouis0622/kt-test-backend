from fastapi import APIRouter
from app.data.dummy_data import CATEGORIES, SUBCATEGORIES, OPTIONS

router = APIRouter()

@router.get("/categories")
def get_categories():
    return CATEGORIES

@router.get("/categories/{category_id}/subcategories")
def get_subcategories(category_id: int):
    return SUBCATEGORIES.get(category_id, [])

@router.get("/subcategories/{subcategory_id}/options")
def get_options(subcategory_id: int):
    return OPTIONS.get(subcategory_id, []) 