import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.pdf_reader import extract_text_from_pdf
from parser.skills_extractor import load_skills, extract_skills

resume_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'resumes', 'sample_resume_john_doe.pdf'))
skills_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'skills.txt'))

resume_text = extract_text_from_pdf(resume_path)
known_skills = load_skills(skills_path)
found_skills = extract_skills(resume_text, known_skills)

print("Extracted Skills:")
print(found_skills)