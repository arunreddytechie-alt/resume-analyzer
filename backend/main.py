from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import upload, analyze

app = FastAPI(title="Resume Analyzer API")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(upload.router)
app.include_router(analyze.router)


@app.get("/")
def root():
    return {"message": "Resume Analyzer API running"}