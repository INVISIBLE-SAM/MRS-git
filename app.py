import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):


    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6b757bb6d0fec18c77a645b98a35c2ed&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
    



def recommend(movie_1):
    movie_index=movies_list[movies_list['title']==movie_1].index[0] #movie index find
    distances=similarity[movie_index] #index loss after sort
    movies_list1=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    #movie_list index similarity
    recommend_movies=[]
    recommended_movies_posters=[]
    for i in movies_list1:
        movie_id=movies_list.iloc[i[0]].movie_id
        recommend_movies.append(movies_list.iloc[i[0]].title) #index find title
        #poster append with movieid
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommended_movies_posters



movies_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movies_list_pic_1=movies_list['title'].values

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
'what would you like',
    movies_list_pic_1)
if st.button('recommend'):
        names,posters=recommend(selected_movie_name)

        col1,col2,col3,col4,col5=st.columns(5)
        with col1:
            
             st.text(names[0])
             st.image(posters[0])
        with col2:
             
             st.text(names[1])
             st.image(posters[1])
        with col3:
            
             st.text(names[2])
             st.image(posters[2])
        with col4:
            
             st.text(names[3])
             st.image(posters[3])
        with col5:
            
             st.text(names[4])
             st.image(posters[4])
       
