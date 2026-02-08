from pathlib import Path
from core.config import JOB_DESCRIPTION_FILE
#loading job description form the Job_description text file in same parent folder.
def load_job_description(filepath: Path = JOB_DESCRIPTION_FILE) -> str:
    if not filepath.exists():
        raise FileNotFoundError(f"Job Description file not found.")
    return filepath.read_text(encoding="utf-8")
