import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import requests

# Replace 'YOUR_TMDB_API_KEY' with your actual TMDb API key
TMDB_API_KEY = "f9a7b6e8690493b3b5160009420d3ff3"
TMDB_API_URL = "https://api.themoviedb.org/3/search/movie"

# Data Collection and Pre-Processing
movies_data = pd.read_csv("/home/priyam-manna/Downloads/movies_read.csv")

# Selecting the relevant features for recommendation
selected_features = ["genres", "keywords", "tagline", "cast", "director"]

# Replacing the null values with empty strings
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna("")

# Combining selected features into a single string
combined_features = (
    movies_data["genres"]
    + " "
    + movies_data["keywords"]
    + " "
    + movies_data["tagline"]
    + " "
    + movies_data["cast"]
    + " "
    + movies_data["director"]
)

# Converting the text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)


def fetch_poster(title):
    """
    Fetches the movie poster URL from TMDb API using the movie title.
    """
    params = {
        "api_key": TMDB_API_KEY,
        "query": title,
        "language": "en-US",
        "page": 1,
        "include_adult": False,
    }
    response = requests.get(TMDB_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            # Get the poster path from the first result
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None  # Return None if no poster is found


def recommend_movies(movie_name):
    list_of_all_titles = movies_data["title"].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        return "No close matches found. Please try another movie.", []

    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]["index"].values[
        0
    ]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, movie in enumerate(
        sorted_similar_movies[1:31], start=1
    ):  # Skip the first as it's the input movie itself
        index = movie[0]
        title_from_index = movies_data.loc[index, "title"]
        recommendations.append(title_from_index)

    return close_match, recommendations


# Streamlit App Interface
st.title("Movie Recommendation System")

# Extracting all movie titles for auto-complete recommendations
all_titles = movies_data["title"].tolist()

# User Input with searchable dropdown
movie_name = st.selectbox(
    "Enter your favorite movie:",
    options=all_titles,
    help="Start typing to search movies",
)

if st.button("Recommend"):
    if movie_name:
        close_match, recommendations = recommend_movies(movie_name)

        if recommendations:
            st.write(f'Movies suggested for you based on "{close_match}":')

            # Display recommendations with posters horizontally
            num_columns = 5  # Number of posters per row
            cols = st.columns(num_columns)
            for i, recommendation in enumerate(recommendations):
                poster_url = fetch_poster(recommendation)

                # Display the poster and title in the respective column
                with cols[i % num_columns]:
                    if poster_url:
                        st.image(poster_url, use_column_width=True)
                    st.caption(recommendation)
        else:
            st.write(recommendations)  # Display error message if no close match found
    else:
        st.write("Please enter a movie name to get recommendations.")
