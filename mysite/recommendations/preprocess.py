import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_data():
    # Load the Netflix dataset into a DataFrame
    netflix_df = pd.read_csv('data/NetflixDataset.csv', encoding='ISO-8859-1')

    # Fill NaN values with empty strings in relevant columns
    netflix_df['Title'].fillna('', inplace=True)
    netflix_df['Genre'].fillna('', inplace=True)
    netflix_df['Tags'].fillna('', inplace=True)
    netflix_df['Summary'].fillna('', inplace=True)
    netflix_df['Director'].fillna('', inplace=True)
    netflix_df['Writer'].fillna('', inplace=True)
    netflix_df['Actors'].fillna('', inplace=True)
    netflix_df['Languages'].fillna('', inplace=True)

    # Concatenate relevant text features into a single column
    netflix_df['combined_text'] = (
        netflix_df['Title'] + ' ' +
        netflix_df['Genre'] + ' ' +
        netflix_df['Tags'] + ' ' +
        netflix_df['Summary'] + ' ' +
        netflix_df['Director'] + ' ' +
        netflix_df['Writer'] + ' ' +
        netflix_df['Actors'] + ' ' +
        netflix_df['Languages']
    )

    # Initialize the TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # Fit the vectorizer to the combined text data
    tfidf_matrix = tfidf_vectorizer.fit_transform(netflix_df['combined_text'])

    return tfidf_matrix, tfidf_vectorizer, netflix_df
