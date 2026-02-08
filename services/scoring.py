from sentence_transformers import SentenceTransformer, util
from core.config import EMBEDDING_MODEL_NAME
from core.config import SEMANTIC_SIMILARITY_THRESHOLD
model = SentenceTransformer(EMBEDDING_MODEL_NAME)
def score_resume_skills_semantic(resume_skills, jd_skills, threshold = SEMANTIC_SIMILARITY_THRESHOLD):
    if not jd_skills:
        return  0.0 , []
    matched_skills = []
    jd_embeddings = model.encode(jd_skills,convert_to_tensor = True)
    resume_embeddings = model.encode(resume_skills, convert_to_tensor = True)
    cosine_scores  =util.cos_sim(resume_embeddings,jd_embeddings)
    
    for i in range(len(resume_skills)):
        for j in range(len(jd_skills)):
            if cosine_scores[i][j] >= threshold:
                matched_skills.append(jd_skills[j])
                
    unique_matched_skills = list(set(matched_skills))
    score = (len(unique_matched_skills)/len(jd_skills)) * 100
    return round(score,2), unique_matched_skills
