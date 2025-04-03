from fastapi import APIRouter, HTTPException
from models import Application
from database import applications_db
from services import fetch_vulnerabilities

router = APIRouter()

@router.post("/applications/")
def create_application(app: Application):
    applications_db.append(app)
    return {"message": "Application added successfully"}

@router.get("/applications/")
def list_applications():
    return applications_db

@router.get("/applications/{app_id}/dependencies")
def get_application_dependencies(app_id: int):
    app = next((a for a in applications_db if a.id == app_id), None)
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")

    dependencies = []
    for dep in app.dependencies:
        package, version = dep.split("==")
        vulnerabilities = fetch_vulnerabilities(package, version)
        dependencies.append({"name": package, "version": version, "vulnerabilities": vulnerabilities})

    return dependencies
