from sklearn.metrics.pairwise import linear_kernel
from .preprocess import preprocess_data
from sklearn.feature_extraction.text import TfidfVectorizer
def get_recommendations(input_movies, input_languages, tfidf_vectorizer, tfidf_matrix, movies_df):
    # Preprocess input data
    combined_text = input_movies + ' ' + input_languages
    input_tfidf = tfidf_vectorizer.transform([combined_text])
    
    # Calculate cosine similarity between input and all movies
    cosine_similarities = linear_kernel(input_tfidf, tfidf_matrix)
    
    # Get top recommendations
    recommendation_indices = cosine_similarities.argsort()[:, ::-1][:, 1:6]  # Exclude first item (itself) and get top 5
    recommendations = []
    for indices in recommendation_indices:
        recommendations.append(movies_df.iloc[indices]['movie_titles'].tolist())
    
    return recommendations