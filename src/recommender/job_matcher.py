import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_job_descriptions(folder_path):
    job_texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                job_texts[filename] = f.read().lower()
    return job_texts

def recommend_jobs(resume_skills, job_descriptions, top_n=3):
    # Convert skill list to string
    resume_text = ' '.join(resume_skills).lower()

    corpus = [resume_text] + list(job_descriptions.values())
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)

    # Compute cosine similarity (resume is vector[0])
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

    ranked_jobs = sorted(
        zip(job_descriptions.keys(), similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_jobs[:top_n]
