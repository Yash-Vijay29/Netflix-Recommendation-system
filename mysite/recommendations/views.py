from django.shortcuts import render
from .preprocess import preprocess_data
from .recommender import recommend_movies
import pandas as pd
# Load and preprocess data once, when the module is loaded
tfidf_matrix, tfidf_vectorizer, netflix_df = preprocess_data()

def home(request):
    return render(request, "authentication/index.html")
def details(request,movie_title):
    # Load the Netflix dataset
    netflix_df = pd.read_csv('data/NetflixDataset.csv', encoding='ISO-8859-1')

    # Retrieve the movie details based on the movie title
    movie = netflix_df.loc[netflix_df['Title'] == movie_title]

    # Convert movie details to a dictionary
    movie_dict = movie.to_dict(orient='records')[0]

    # Pass the movie details to the template for rendering
    return render(request, 'authentication/details.html', {'movie': movie_dict})


def recommendations_view(request):
    if request.method == "POST":
        selected_movies = request.POST.get('selected_movies', '')
        selected_languages = request.POST.get('selected_languages', '')

        # Split the selected movies and languages into lists
        selected_movies_list = selected_movies.split(',')
        selected_languages_list = selected_languages.split(',')
        print("Selected languages:", selected_languages_list)
        print("Selected movies:", selected_movies_list)

        # Get movie recommendations
        try:
            recommendations = recommend_movies(
                selected_movies_list, selected_languages_list, tfidf_vectorizer, tfidf_matrix, netflix_df
            )
            print("Recommendations computed")
        except Exception as e:
            print(f"Error during recommendation: {e}")
            recommendations = pd.DataFrame()

        return render(request, "authentication/index.html", {
            'fname': request.user.first_name,
            'recommendations': recommendations.to_dict(orient='records') if not recommendations.empty else [],
            'selected_movies': selected_movies_list,
            'selected_languages': selected_languages_list,
        })
    else:
        return render(request, "authentication/index.html")
