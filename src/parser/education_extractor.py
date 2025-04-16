import re

def extract_education(text):
    text = text.lower()
    education_entries = []

    degree_keywords = [
        "bachelor", "b.tech", "b.sc", "b.e",
        "master", "m.tech", "m.sc", "mca", "mba",
        "phd", "high school", "intermediate", "secondary school"
    ]

    # Match lines with degree + year (or just degree)
    lines = text.split('\n')
    for line in lines:
        if any(re.search(rf'\b{re.escape(degree)}\b', line) for degree in degree_keywords) and "language" not in line:
            # Try to extract graduation year
            match = re.search(r'(19|20)\d{2}', line)
            year = match.group(0) if match else None
            education_entries.append({'text': line.strip(), 'year': year})
    
    return education_entries
