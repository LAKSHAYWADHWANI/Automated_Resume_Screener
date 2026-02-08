# Automated Resume Screener
A production-oriented **Python + NLP system** that automatically screens and ranks resumes against a given job description using **skill matching** and **semantic similarity scoring**.

Designed with a **modular, backend-first architecture** to demonstrate real-world engineering practices beyond notebook or tutorial-style projects.

---
## 🚀 Overview
Recruiters often spend significant time manually reviewing resumes for skill alignment with job descriptions with some of the resumes not even meeting all the eligibility criteria wasting the recruiter's time.  
This project automates that process by:
- Extracting structured information from resumes (PDF, DOCX, TXT)
- Normalizing and preprocessing unstructured text
- Matching candidate skills against job requirements
- Ranking resumes using **semantic similarity** (embeddings-based scoring)
- Presenting results through an interactive Streamlit UI

The focus is on **clean system design, separation of concerns, and extensibility**, not just model accuracy.

---

## 🧠 System Workflow

Resume Upload 

↓

Text Extraction (PDF / DOCX / TXT)

↓

Text Cleaning & Normalization

↓

Skill Extraction (Fuzzy + Keyword Matching)

↓

Semantic Similarity Scoring (Embeddings)

↓

Resume Ranking

↓

Visualization & Export

---

## 🏗 Architecture

The project follows a **layered architecture** inspired by backend systems:

├── core/ # Configuration & logging

├── services/ # Business logic (parsing, NLP, scoring)

├── ui/ # Streamlit UI & presentation helpers

├── main.py # Application entry point

### Key Design Decisions
- **UI is decoupled from business logic** (services are framework-agnostic)
- **Configuration centralized** in `core/config.py`
- **Pure functions** where possible for testability
- Designed to be easily extended to:
  - FastAPI backend
  - Batch/CLI processing
  - Database persistence

---

## 🛠 Tech Stack

- **Language:** Python  
- **NLP:** Sentence Transformers (semantic embeddings)  
- **Text Processing:** Regex, fuzzy matching  
- **Data Handling:** Pandas  
- **UI:** Streamlit  
- **Visualization:** Plotly  
- **Architecture:** Modular, service-oriented design  

---

## ✨ Features

- Supports **PDF, DOCX, and TXT** resumes
- Skill extraction using configurable skill lists
- Semantic resume–JD matching using embeddings
- Resume ranking with percentage-based scoring
- Interactive visual comparison of candidates
- Export screening results to Excel
- Sample configuration files (no sensitive data committed)

---

## ▶️ How to Run Locally

### 1. Clone the repository
git clone https://github.com/<your-username>/automated-resume-screener.git
cd automated-resume-screener
### 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
### 3. Install dependencies
pip install -r requirements.txt
### 4. Run the application
streamlit run main.py

## 📌 Configuration Notes
- skills_list_sample.txt contains sample skills for matching
- Job_Description_Sample.txt demonstrates file-based JD input
- Real resumes or sensitive data are intentionally excluded from the repository

## ⚠️ Limitations
- No persistent storage (in-memory processing)
- Skill extraction relies on keyword/fuzzy matching
- Not optimized for very large resume batches
- Authentication and access control not implemented
- These are intentional trade-offs for clarity and modularity.

## 🔮 Future Improvements:
- FastAPI backend with REST endpoints
- Vector database integration for large-scale similarity search
- Configurable scoring weights
- Resume clustering and analytics
- Unit tests & CI pipeline
- Role-specific scoring profiles

## 👤 Author
Lakshay Wadhwani
B.Tech CSE (AI & Data Science)
Focused on building real, deployable systems with Python, NLP, and backend engineering principles.

## 📄 License
This project is for educational and demonstration purposes.
