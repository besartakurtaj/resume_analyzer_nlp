from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def extract_skills(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    words = [w.lower() for w in tokens if w.isalpha() and w.lower() not in stop_words]
    return list(set(words))  # Remove duplicates

def compute_score(resume_skills, jd_skills):
    matches = set(resume_skills) & set(jd_skills)
    score = len(matches) / len(set(jd_skills)) * 100 if jd_skills else 0
    return round(score, 2), list(matches)
