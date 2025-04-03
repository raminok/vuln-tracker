import uvicorn
from fastapi import FastAPI
from routes import applications, dependencies

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, This is API!"}

# Include routers with distinct prefixes
app.include_router(applications.router, prefix="/api/applications")
app.include_router(dependencies.router, prefix="/api/dependencies")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
