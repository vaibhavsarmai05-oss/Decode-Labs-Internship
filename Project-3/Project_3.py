import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
print("="*60)
print("Welcome to the Career Recommendation System!\n")
print("="*60)

data = pd.read_csv("raw_skills.csv")

skills_list = data["Skills"].tolist()

skill1 = input("Enter first skill: ").title()
skill2 = input("Enter second skill: ").title()
skill3 = input("Enter third skill: ").title()

user_skills = f"{skill1} {skill2} {skill3}"
print(f"\nYou entered the following skills: {user_skills}\n")


all_skills = skills_list + [user_skills]
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(all_skills)

user_vector = tfidf_matrix[-1]

job_vectors = tfidf_matrix[:-1]

similarity_scores = cosine_similarity(user_vector, job_vectors)
similarity_scores = similarity_scores.flatten()
top_indices = similarity_scores.argsort()[::-1][:3]

print("\nTop career recommendations:\n")

for rank, index in enumerate(top_indices, start=1):
    role = data.iloc[index]["Role"]
    score = similarity_scores[index] * 100
    print(f"{rank}. {role} - {score:.2f}% ")

print("\nThank you for using the Career Recommendation System!")
