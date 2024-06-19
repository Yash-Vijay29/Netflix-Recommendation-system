
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def preprocess_data(movies_df):
  tfidf_vectorizer = TfidfVectorizer(stop_words='english')
  movies_df['Title'] = movies_df['Title']
  movies_df['Languages'] = movies_df['Languages']
  tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Title'] + ' ' + movies_df['Languages'])
  return tfidf_matrix
