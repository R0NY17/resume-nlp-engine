import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.pdf_reader import extract_text_from_pdf
from parser.experience_extractor import extract_experience

resume_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'resumes', 'sample_resume_john_doe.pdf'))
resume_text = extract_text_from_pdf(resume_path)

experience_info = extract_experience(resume_text)

print("Extracted Experience:")
for entry in experience_info:
    print("-", entry)
