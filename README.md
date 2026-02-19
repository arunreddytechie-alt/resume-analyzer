Resume Analyzer AI

Resume Analyzer AI is an AI-powered application that analyzes resumes against job descriptions using Large Language Models (LLMs). It helps users understand their job fit, identify missing skills, and prepare for interviews.

This system allows users to upload resumes and multiple job descriptions, select a job, ask questions, and receive intelligent analysis.

⸻

Features
	•	Upload Resume (PDF, DOCX)
	•	Upload Multiple Job Descriptions
	•	Automatic file validation
	•	Select resume and job description
	•	Ask custom questions
	•	Get AI-powered analysis
	•	Fit score calculation
	•	Missing skills identification
	•	Interview preparation suggestions

⸻

System Architecture

Frontend:
	•	Streamlit UI

Backend:
	•	FastAPI REST API

AI:
	•	OpenAI GPT model

Parsing:
	•	PyMuPDF (PDF parsing)
	•	python-docx (DOCX parsing)

Storage:
	•	Local file storage

⸻

Project Structure
resume-analyzer/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   │    ├── upload.py
│   │    └── analyze.py
│   │
│   ├── services/
│   │    ├── parser.py
│   │    ├── validator.py
│   │    └── analyzer.py
│   │
│   ├── storage/
│   │    ├── resumes/
│   │    └── jobs/
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md



Prerequisites

Install the following:
	•	Python 3.10 or later
	•	pip
	•	OpenAI API Key

Check Python version:
python --version


Setup Instructions

Step 1: Clone the Repository
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git

cd resume-analyzer


Step 2: Create Virtual Environment
Mac/Linux:
python3 -m venv venv
source venv/bin/activate


Step 3: Install Backend Dependencies
cd backend
pip install -r requirements.txt



Dependencies include:
	•	fastapi
	•	uvicorn
	•	python-multipart
	•	pymupdf
	•	python-docx
	•	openai

⸻

Step 4: Set OpenAI API Key

Mac/Linux:
export OPENAI_API_KEY="your_api_key_here"


Step 5: Run Backend Server
From backend folder:
uvicorn main:app --reload

Backend runs at:
http://localhost:8000

API docs:
http://localhost:8000/docs


Step 6: Install Frontend Dependencies
Open new terminal.

Activate virtual environment.

Go to frontend folder:
cd frontend

pip install -r requirements.txt


Dependencies include:
	•	streamlit
	•	requests

⸻

Step 7: Run Frontend
streamlit run app.py


http://localhost:8501



How to Use

Step 1: Upload Resume
Use left sidebar to upload resume file.

Step 2: Upload Job Description
Upload one or more job descriptions.

Step 3: Select Resume
Choose resume from dropdown.

Step 4: Select Job
Choose job description from dropdown.

Step 5: Ask Question
Example questions:
	•	What is my fit score?
	•	What skills am I missing?
	•	How does my experience align with this role?

Step 6: Click Analyze
System will return AI-powered analysis.


Example Questions

What skills am I missing?
What is my fit score?
How should I prepare for interview?
What are my strengths for this job?