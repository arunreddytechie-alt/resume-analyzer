import os

from fastapi import APIRouter
from pydantic import BaseModel

from services.parser import parse_file
from services.analyzer import analyze_resume

router = APIRouter()

# Get absolute backend directory safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STORAGE_DIR = os.path.join(BASE_DIR, "storage")

RESUME_DIR = os.path.join(STORAGE_DIR, "resumes")
JOB_DIR = os.path.join(STORAGE_DIR, "jobs")

# Ensure directories exist
os.makedirs(RESUME_DIR, exist_ok=True)
os.makedirs(JOB_DIR, exist_ok=True)


class QuestionRequest(BaseModel):
    resume_id: str
    job_id: str
    question: str


@router.post("/analyze")
def analyze(request: QuestionRequest):

    resume_path = os.path.join(RESUME_DIR, request.resume_id)
    job_path = os.path.join(JOB_DIR, request.job_id)

    resume_text = parse_file(resume_path)
    job_text = parse_file(job_path)

    result = analyze_resume(
        resume_text,
        job_text,
        request.question
    )

    return {
        "success": True,
        "answer": result
    }