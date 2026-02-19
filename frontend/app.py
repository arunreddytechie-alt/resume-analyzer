import streamlit as st
import requests

# ======================
# Config
# ======================

BACKEND_URL = "http://localhost:8000"

ALLOWED_TYPES = ["pdf", "docx"]

st.set_page_config(
    page_title="Resume Analyzer AI",
    page_icon="📄",
    layout="wide"
)

# ======================
# Session state init
# ======================

if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

if "job_uploaded" not in st.session_state:
    st.session_state.job_uploaded = False

if "selected_resume" not in st.session_state:
    st.session_state.selected_resume = None

if "selected_job" not in st.session_state:
    st.session_state.selected_job = None


# ======================
# Backend API functions
# ======================

def fetch_resumes():

    try:
        response = requests.get(f"{BACKEND_URL}/resumes")

        if response.status_code == 200:
            return response.json().get("resumes", [])

    except Exception as e:
        st.error("Cannot connect to backend")

    return []


def fetch_jobs():

    try:
        response = requests.get(f"{BACKEND_URL}/jobs")

        if response.status_code == 200:
            return response.json().get("jobs", [])

    except Exception:
        st.error("Cannot connect to backend")

    return []


# ======================
# Upload functions
# ======================

def upload_resume():

    file = st.session_state.resume_file

    if file is None:
        return

    with st.spinner("Uploading resume..."):

        files = {
            "file": (
                file.name,
                file.getvalue(),
                file.type
            )
        }

        try:

            response = requests.post(
                f"{BACKEND_URL}/upload-resume",
                files=files
            )

            data = response.json()

            if data.get("success"):

                st.session_state.resume_uploaded = True

                st.success(data.get("message", "Resume uploaded"))

                st.rerun()

            else:

                st.error(data.get("error", "Resume upload failed"))

        except Exception as e:

            st.error("Backend connection failed")


def upload_job():

    files = st.session_state.job_files

    if not files:
        return

    for file in files:

        with st.spinner(f"Uploading {file.name}..."):

            payload = {
                "file": (
                    file.name,
                    file.getvalue(),
                    file.type
                )
            }

            try:

                response = requests.post(
                    f"{BACKEND_URL}/upload-job",
                    files=payload
                )

                data = response.json()

                if data.get("success"):

                    st.session_state.job_uploaded = True

                    st.success(f"{file.name} uploaded")

                else:

                    st.error(data.get("error", f"{file.name} failed"))

            except Exception:

                st.error("Backend connection failed")

    st.rerun()


# ======================
# Sidebar Upload UI
# ======================

st.sidebar.header("Upload Files")

st.sidebar.file_uploader(
    "Upload Resume",
    type=ALLOWED_TYPES,
    key="resume_file",
    on_change=upload_resume
)

st.sidebar.file_uploader(
    "Upload Job Descriptions",
    type=ALLOWED_TYPES,
    accept_multiple_files=True,
    key="job_files",
    on_change=upload_job
)

# ======================
# Main UI
# ======================

st.title("Resume Analyzer AI")

# Fetch latest data
resumes = fetch_resumes()
jobs = fetch_jobs()

col1, col2 = st.columns(2)

# ======================
# Resume dropdown
# ======================

with col1:

    st.subheader("Select Resume")

    if resumes:

        resume_options = {
            r["resume_name"]: r["resume_id"]
            for r in resumes
        }

        selected_resume_name = st.selectbox(
            "Choose Resume",
            list(resume_options.keys())
        )

        selected_resume_id = resume_options[selected_resume_name]

    else:

        st.warning("No resumes uploaded")

        selected_resume_id = None


# ======================
# Job dropdown
# ======================

with col2:

    st.subheader("Select Job")

    if jobs:

        job_options = {
            j["job_name"]: j["job_id"]
            for j in jobs
        }

        selected_job_name = st.selectbox(
            "Choose Job Description",
            list(job_options.keys())
        )

        selected_job_id = job_options[selected_job_name]

    else:

        st.warning("No job descriptions uploaded")

        selected_job_id = None


# ======================
# Question input
# ======================

st.subheader("Ask Question")

question = st.text_input(
    "",
    placeholder="What skills am I missing for this role?"
)


# ======================
# Analyze button
# ======================

if st.button("Analyze", type="primary"):

    if not selected_resume_id:

        st.error("Please upload and select a resume")

    elif not selected_job_id:

        st.error("Please upload and select a job description")

    elif not question.strip():

        st.error("Please enter a question")

    else:

        with st.spinner("Analyzing..."):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/analyze",
                    json={
                        "resume_id": selected_resume_id,
                        "job_id": selected_job_id,
                        "question": question
                    }
                )

                data = response.json()

                if data.get("success"):

                    st.success("Analysis Complete")

                    st.subheader("Result")

                    st.write(data["answer"])

                else:

                    st.error(data.get("error", "Analysis failed"))

            except Exception:

                st.error("Backend connection failed")