from pathlib import Path
# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Files
SKILLS_FILE = BASE_DIR / "skills_list.txt"
JOB_DESCRIPTION_FILE = BASE_DIR / "Job_Description.txt"

# ML settings
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# Scoring thresholds
SEMANTIC_SIMILARITY_THRESHOLD = 0.6
FUZZY_MATCH_THRESHOLD = 95

supported_file_extensions = (".pdf", ".txt,", ".docx")