import os
import shutil
import uuid
from services.parser import parse_file
from services.validator import validate_resume_text, validate_job_text

from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

def save_temp_file(file: UploadFile):

    temp_filename = f"temp_{file.filename}"

    temp_path = os.path.join(STORAGE_DIR, temp_filename)

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return temp_path

# Get absolute backend directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct storage paths
STORAGE_DIR = os.path.join(BASE_DIR, "storage")

RESUME_DIR = os.path.join(STORAGE_DIR, "resumes")
JOB_DIR = os.path.join(STORAGE_DIR, "jobs")

# Ensure directories exist
os.makedirs(RESUME_DIR, exist_ok=True)
os.makedirs(JOB_DIR, exist_ok=True)

ALLOWED_TYPES = ["pdf", "docx"]


def validate_file(file: UploadFile):

    extension = file.filename.split(".")[-1].lower()

    if extension not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX allowed"
        )


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    try:

        temp_path = save_temp_file(file)

        text = parse_file(temp_path)

        valid, error = validate_resume_text(text)

        if not valid:

            os.remove(temp_path)

            return {
                "success": False,
                "error": error
            }

        unique_name = f"{uuid.uuid4()}_{file.filename}"

        final_path = os.path.join(RESUME_DIR, unique_name)

        os.rename(temp_path, final_path)

        return {
            "success": True,
            "message": "Resume uploaded successfully"
        }

    except Exception as e:

        print("Upload resume error:", str(e))

        return {
            "success": False,
            "error": str(e)
        }


@router.post("/upload-job")
async def upload_job(file: UploadFile = File(...)):

    try:

        temp_path = save_temp_file(file)

        text = parse_file(temp_path)

        valid, error = validate_job_text(text)

        if not valid:

            os.remove(temp_path)

            return {
                "success": False,
                "error": error
            }

        unique_name = f"{uuid.uuid4()}_{file.filename}"

        final_path = os.path.join(JOB_DIR, unique_name)

        os.rename(temp_path, final_path)

        return {
            "success": True,
            "message": "Job uploaded successfully"
        }

    except Exception as e:

        print("Upload job error:", str(e))

        return {
            "success": False,
            "error": str(e)
        }

@router.get("/jobs")
def list_jobs():

    files = os.listdir(JOB_DIR)

    jobs = []

    for file in files:
        jobs.append({
            "job_id": file,
            "job_name": file
        })

    return {"jobs": jobs}

@router.get("/resumes")
def list_resumes():

    files = os.listdir(RESUME_DIR)

    resumes = []

    for file in files:

        clean_name = file.split("_", 1)[1] if "_" in file else file

        resumes.append({
            "resume_id": file,
            "resume_name": clean_name
        })

    return {"resumes": resumes}