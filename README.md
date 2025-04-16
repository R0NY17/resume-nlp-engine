# Resume Parser & Job Recommendation Engine

This project is a rule-based Resume Parser and Job Recommendation Engine built using Python.
🧪 Note: This is a lightweight prototype using simple keyword matching and TF-IDF. Accuracy is limited and depends heavily on resume formatting and content quality.


## 🔧 Features
- Extract text from PDF resumes
- Parse skills, education, experience using NLP (SpaCy, NLTK, Transformers)
- Match resumes to job descriptions using TF-IDF + cosine similarity
- Job recommender system for candidates

## 🚀 Tech Stack
- Python
- PDFPlumber (resume text extraction)
- Rule-based parsing with Regex
- TF-IDF & Cosine Similarity (`scikit-learn`)

## ⚠️ Known Limitations
- Parsing logic is rule-based and fragile for unusual resume formats.
- No semantic understanding of text (no NER, no embeddings).
- Job matching relies on keyword overlap, not contextual meaning.

## 🚀 Future Improvements
- Use SpaCy for Named Entity Recognition (NER)
- Replace TF-IDF with BERT embeddings (Hugging Face Transformers)
- Build a web interface or CLI tool