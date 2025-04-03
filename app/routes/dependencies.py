from fastapi import APIRouter
from database import dependencies_db

router = APIRouter()

@router.get("/dependencies/")
def list_dependencies():
    return dependencies_db
