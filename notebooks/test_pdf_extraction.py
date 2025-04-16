import os
import sys

# Add the src/ directory to the system path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.pdf_reader import extract_text_from_pdf

# Path to the sample resume PDF
pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'resumes', 'sample_resume_john_doe.pdf'))

# Extract and print the text
try:
    extracted_text = extract_text_from_pdf(pdf_path)
    print("Resume text extraction successful!\n")
    print(extracted_text[:1000])  # Print first 1000 characters
except Exception as e:
    print("Error:", e)
