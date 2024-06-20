from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(user_movies, preferred_languages, tfidf_vectorizer, tfidf_matrix, netflix_df, top_n=10):
    # Transform user's preferred movies into TF-IDF vectors
    user_tfidf_vectors = tfidf_vectorizer.transform(user_movies)

    # Compute cosine similarity between user's TF-IDF vectors and all other movies
    similarity_scores = cosine_similarity(user_tfidf_vectors, tfidf_matrix)

    # Get the indices of movies with highest similarity scores
    movie_indices = similarity_scores.argsort()[0][-top_n-1:][::-1]

    # Get the recommended movies based on the indices
    recommended_movies = netflix_df.iloc[movie_indices]

    # Filter out movies that the user has already input
    recommended_movies = recommended_movies[~recommended_movies['Title'].isin(user_movies)]

    # Filter recommended movies by preferred languages
    recommended_movies = recommended_movies[
        recommended_movies['Languages'].apply(lambda x: any(lang in x for lang in preferred_languages))
    ]

    # Select only the 'Title' and 'Image' columns
    recommended_movies = recommended_movies[['Title', 'Image']]

    return recommended_movies
