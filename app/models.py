from pydantic import BaseModel
from typing import List, Optional

class Application(BaseModel):
    id: int
    name: str
    description: str
    dependencies: List[str]

class Dependency(BaseModel):
    name: str
    version: str
    vulnerabilities: Optional[List[dict]] = []