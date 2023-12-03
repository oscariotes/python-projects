# import nltk
# from nltk import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from nltk.probability import FreqDist
# import matpolotlib.pyplot as plt
# from nltk.stem.wordnet import WordNetLemmatizer
# from wordcloud import WordCloud
# from iPython import display


import os

# Example file paths (replace these with your file paths)
resume_file_path = 'resume/Laurente.txt'
job_description_file_path = 'resume/sample_job_desc.txt'

def read_files_to_list(resume_path, job_description_path):
    content_list = []

    # Read content of resume file
    with open(resume_path, 'r') as resume_file:
        content_list.append(resume_file.read().lower().strip())

    # Read content of job description file
    with open(job_description_path, 'r') as job_description_file:
        content_list.append(job_description_file.read()lower().strip())

    return content_list

# Get script directory
script_dir = os.path.dirname(__file__)
resume_path = os.path.join(script_dir, resume_file_path)
job_description_path = os.path.join(script_dir, job_description_file_path)

# Call the function with the file paths
resume_list = read_files_to_list(resume_path, job_description_path)

resume = resume_list[0]
job_description = resume_list[1]

print(resume)
print(job_description)


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


vectorizer = CountVectorizer()
vectorized_text = vectorizer.fit_transform(resume_list)


# Calculate cosine similarity
similarity_score = cosine_similarity(vectorized_text)[0][1]*100
similarity_score = round(similarity_score, 2)


# This the cosine similarity score


print('Similarity score:', str(similarity_score)+ '%')