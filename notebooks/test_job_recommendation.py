import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.pdf_reader import extract_text_from_pdf
from parser.skills_extractor import extract_skills, load_skills
from recommender.job_matcher import load_job_descriptions, recommend_jobs

resume_path = 'data/resumes/sample_resume_john_doe.pdf'
skills_path = 'data/skills.txt'
jobs_folder = 'data/job_descriptions/'

# Extract resume skills
resume_text = extract_text_from_pdf(resume_path)
known_skills = load_skills(skills_path)
resume_skills = extract_skills(resume_text, known_skills)

# Load job descriptions
job_descriptions = load_job_descriptions(jobs_folder)

# Recommend jobs
recommended = recommend_jobs(resume_skills, job_descriptions)

print("Recommended Jobs:")
for job, score in recommended:
    print(f"{job}: {round(score * 100, 2)}% match")
