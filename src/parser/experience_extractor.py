import re

def extract_experience(text):
    text = text.lower()
    experience_entries = []

    job_keywords = [
        "engineer", "developer", "intern", "analyst", "manager", "consultant", "specialist",
        "researcher", "data scientist", "project lead", "assistant", "technician"
    ]

    lines = text.split('\n')
    for line in lines:
        if any(job in line for job in job_keywords) and len(line.strip()) > 5:
            experience_entries.append(line.strip())

    return experience_entries