import streamlit as st
import pandas as pd
import requests

movies = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Title of the app
st.title("Movie Recommender System")

# Input for the movie title
movie_title = st.selectbox("Select a movie:", movies['title'].tolist())

if st.button("Recommend"):
    recommendations = recommend_movies(movie_title, user_movie_ratings)
    st.write("### Recommended Movies:")
    for movie in recommendations.index:
        st.write(movie)
