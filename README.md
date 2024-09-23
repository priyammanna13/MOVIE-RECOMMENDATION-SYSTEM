# Content Based Movie Recommendation System

## Overview

This project is a content-based movie recommendation system that suggests movies based on a user's favorite movie. It utilizes the TMDb API to fetch movie posters and provides a user-friendly interface using Streamlit.

## Features

- **Searchable Dropdown**: Users can type in their favorite movie to get recommendations.
- **Movie Posters**: Displays posters of recommended movies fetched from the TMDb API.
- **Cosine Similarity**: Utilizes TF-IDF vectorization and cosine similarity to find similar movies based on various features.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- TMDb API

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/priyammanna13/MOVIE-RECOMMENDATION-SYSTEM.git
   
   ```

2. **Install Required Packages**
   Ensure you have Python installed, then install the required packages using pip:
   ```bash
   pip install pandas numpy scikit-learn streamlit requests
   ```

3. **API Key**
   Replace `YOUR_TMDB_API_KEY` in the code with your actual TMDb API key. You can obtain an API key by signing up on [TMDb](https://www.themoviedb.org/).

4. **Run the Application**
   Execute the following command to start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter your favorite movie in the dropdown menu.
2. Click the "Recommend" button to see a list of suggested movies based on your input.
3. The recommended movies will be displayed along with their posters.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
