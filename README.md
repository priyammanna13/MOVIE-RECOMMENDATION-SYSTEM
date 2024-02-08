# MOVIE-RECOMMENDATION-SYSTEM

# Technology
Machine Learning ,
python , pandas , numpy , scikitlearn

# Content Based Filtering

Content based filtering is a technique that uses the features of the items (such as genre, actors, director, etc.) to find the similarity between them and recommend the most similar items to the user. For example, if a user likes a movie that is a comedy and has Will Smith as an actor, the system will recommend other movies that are comedies and have Will Smith as an actor.


# Cosine Similarity

It is a metric that measures how similar two entities are (like documents or vectors in a multi-dimensional space), irrespective of size. Cosine similarity is widely used in NLP to find similar context words.


# Dataset
The dataset used for this project is the TMDB 5000 Movie Dataset, Metadata on ~5,000 movies from TMDb The dataset also includes movie metadata such as title, genres, release year, etc.

# Code
The code consists of the following steps:

Loading and exploring the dataset. Preprocessing the data and creating feature vectors for the movies. Computing the cosine similarity matrix for the movies. Defining a function to generate recommendations for a given movie title. Testing the system with some examples

# Results
The system is able to generate relevant recommendations for different movie titles based on the content features. For example, for the movie “IRON MAN”, the system recommends the following movies:

IRON MAN 2 IRON MAN 3 AVENGERS: AGE OF ULTRON ANT MAN

# Conclusion
This project demonstrates how to build a simple but effective movie recommender system using content based filtering and cosine similarity. The system can also be extended to use collaborative filtering or hybrid approaches to combine the advantages of both content based and user based methods.

# References
1. FREECODECAMP
2. Kaggle
