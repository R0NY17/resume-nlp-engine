import re

def load_skills(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        skills = set(line.strip().lower() for line in f if line.strip())
    return skills

def extract_skills(resume_text, known_skills):
    # Normalize text
    text = resume_text.lower()

    # Tokenize by words (basic split)
    words = re.findall(r'\b\w+\b', text)

    # Match known skills
    extracted = set()
    for skill in known_skills:
        if skill in text:
            extracted.add(skill)
    return list(extracted)