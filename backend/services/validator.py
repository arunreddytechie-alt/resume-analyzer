# backend/services/validator.py

def validate_resume_text(text):

    if not text or len(text.strip()) < 200:
        return False, "Resume content is empty or unreadable."

    keywords = [
        "experience",
        "education",
        "skills",
        "project",
        "work",
        "engineer",
        "developer"
    ]

    text_lower = text.lower()

    score = sum(1 for k in keywords if k in text_lower)

    if score < 2:
        return False, "Uploaded file does not appear to be a valid resume."

    return True, None


def validate_job_text(text):

    if not text or len(text.strip()) < 200:
        return False, "Job description content is empty or unreadable."

    keywords = [
        "responsibilities",
        "requirements",
        "qualifications",
        "skills",
        "experience",
        "job",
        "role"
    ]

    text_lower = text.lower()

    score = sum(1 for k in keywords if k in text_lower)

    if score < 2:
        return False, "Uploaded file does not appear to be a valid job description."

    return True, None