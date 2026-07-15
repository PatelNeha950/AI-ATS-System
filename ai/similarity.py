from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_text):

    documents = [resume_text, job_text]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

    return round(similarity * 100, 2)