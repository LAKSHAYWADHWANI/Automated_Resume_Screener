import os
import re
from rapidfuzz import fuzz
from core.config import FUZZY_MATCH_THRESHOLD
def extract_skills_from_text(text, filepath, threshold = FUZZY_MATCH_THRESHOLD):
    if not os.path.exists(filepath):
        print(f"[ERROR]Skills file not found")
        return []
    with open (filepath, 'r' ,encoding ='utf-8') as f:
        skills = [line.strip().lower() for line in f if line.strip()]
    text = text.lower()
    found_skills = []
    words = re.findall(r'\b\w+\b', text)
    ngrams = list(set(' '.join(words[i:i+n]) for n in range(1,4)for i in range(len(words)-n+1)))
    for skill in skills:
        for phrase in  ngrams:
            if fuzz.ratio(skill.lower(), phrase) >= threshold:
                found_skills.append(skill)
                break
    return list(set(found_skills))
