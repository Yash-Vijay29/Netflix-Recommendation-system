First project ever, im building a netflix recommendation program based on a NetflixDataset
The recommendation system uses a hybrid model
using TF-IDF for content-based filtering and matrix factorization for collaborative filtering
VARIABLES UNDER CONSIDERATION:
For TF-IDF (Content-Based Filtering):
Title: The title of the movie can provide important keywords for content-based filtering.
Genre: Genres can be used as features for content-based recommendations.
Tags: Tags can provide additional keywords for content-based filtering.
Summary: The movie summary contains textual information that can be used to compute TF-IDF vectors.
Director, Writer, Actors: Names of directors, writers, and actors can also be used as features for content-based recommendations.
Language: Language can be considered if you want to recommend movies in the user's preferred language.
IMDb Score: IMDb scores can be used as weights to prioritize important words in the TF-IDF calculation.
