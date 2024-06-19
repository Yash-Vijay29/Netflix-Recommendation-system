from django.shortcuts import render
from .preprocess import preprocess_data
from .recommender import get_recommendations
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
def home(request):
    return render(request,"authentication/index.html")
def recommendations_view(request):
    if request.method == 'POST':
        # Extract input data from the form
        movie_titles = request.POST.get('movie_titles')
        preferred_languages = request.POST.get('preferred_languages')
        filepath = "data/NetflixDataset.csv"
        try:
         # Read the CSV data using appropriate encodings
         data = pd.read_csv(filepath, encoding='utf-8')
        except UnicodeDecodeError:
         data = pd.read_csv(filepath, encoding='ISO-8859-1')
         # Drop duplicate rows (if needed)
        data = data.drop_duplicates(subset='Title')
        # Preprocess data
        input_movies = movie_titles.split(',')
        input_languages = preferred_languages.split(',')
        tfidf_matrix = preprocess_data(data)
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        
        # Get recommendations
        recommendations = get_recommendations(movie_titles, preferred_languages, tfidf_vectorizer, tfidf_matrix, data)
        
        return render(request, 'authentication/index.html', {'recommendations': recommendations})