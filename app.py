# Run Command
# streamlit run app.py

import streamlit as st
import pickle
import pandas as pd
import requests


# Function to fetch movie details (including poster)
def fetch_movie_details(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    data = response.json()
    return data


# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        movie_data = fetch_movie_details(movie_id)
        recommended_movies.append(movie_data)
    return recommended_movies


# Load movie data and similarity matrix
file_path_1 = 'C:/Users/MMT/PycharmProjects/movie recommender system/venv/movies_dict.pkl'
movies_dict = pickle.load(open(file_path_1, 'rb'))
movies = pd.DataFrame(movies_dict)

file_path_2 = 'C:/Users/MMT/PycharmProjects/movie recommender system/venv/similarity.pkl'
similarity_dict = pickle.load(open(file_path_2, 'rb'))
similarity = pd.DataFrame(similarity_dict)

# Set Streamlit page title and description
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬")
st.title("Movie Recommender System")
st.write("Select a movie, and we'll recommend similar movies for you.")

# User selects a movie
selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

# Display recommended movies and details with poster on the right and details on the left
if st.button('Recommend'):
    recommended_movies = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")
    for movie_data in recommended_movies:
        col1, col2 = st.columns(2)
        # Display the poster in the first column (on the right)
        with col1:
            st.image("https://image.tmdb.org/t/p/w500/" + movie_data['poster_path'], caption=movie_data['title'],width=200)
        # # Display the poster in the first column (on the right)
        # with col1:
        #     st.image("https://image.tmdb.org/t/p/w500/" + movie_data['poster_path'], caption=movie_data['title'],
        #              use_container_width=True)

        # Display movie details in the second column (on the left)
        with col2:
            st.write(f"**Title:** {movie_data['title']} ({movie_data['release_date'][:4]})")
            st.write(f"**Genres:** {', '.join([genre['name'] for genre in movie_data['genres']])}")
            st.write(f"**Overview:** {movie_data['overview']}")
            st.write(f"**Average Rating:** {movie_data['vote_average']}")
