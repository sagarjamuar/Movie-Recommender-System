import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommender System")

movies_list=pd.read_pickle("movies.pkl")
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    for i in distances[1:6]:
        movie_id = i[0]
        #fetch movie poster
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies_list.title.values)

if st.button('Recommended'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)