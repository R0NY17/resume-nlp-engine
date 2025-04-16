import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.pdf_reader import extract_text_from_pdf
from parser.education_extractor import extract_education

resume_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'resumes', 'sample_resume_john_doe.pdf'))
resume_text = extract_text_from_pdf(resume_path)

education_info = extract_education(resume_text)

print("Extracted Education Info:")
for entry in education_info:
    print(entry)