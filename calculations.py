#!/usr/bin/env python
# coding: utf-8

# In[141]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from collections import Counter
import itertools

# In[142]:


orginal_data = pd.read_csv('data.csv', sep=',')
data = orginal_data.copy(deep=True)

st.sheader("Calculations")
# 
st.markdown(
    "Following calculation will be provided for Netflix data. Same formulas were used to calculate data for other platforms and can be found in *calculations.py* inside the project.")

st.subheader("Netflix")


# In[143]:


Netflix_data = data[data["Netflix"] == 1]
st.code('''Netflix_data = data[data["Netflix"] == 1]''')
st.subheader("IMdB")

# In[144]:

st.code('''Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).mean().round(3)
Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).median()
Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).std().round(3)
''')
Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).mean().round(3)

# In[145]:


Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).median()

# In[146]:


Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).std().round(3)

st.subheader("Rotten Tomatoes")

# In[147]:
st.code('''Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).std().round(3)
Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).mean().round(3)
Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).median()
''')

Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).std().round(3)

# In[148]:


Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).mean().round(3)

# In[149]:


Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).median()

st.subheader("Release date")

# In[150]:


release_year = {}
Netflix_release = data[(data["Netflix"] == 1)]
years = dict(Netflix_release["Year"].value_counts().sort_values())
fig = go.Figure([go.Bar(x=list(years.keys()), y=list(years.values()))])
# fig.show()
st.plotly_chart(fig)

st.markdown(
    "Netflix is famous for its TV-series. Especially for its amount. The highest amount of series was released in 2018-2020 but many of them were postponed due to pandemic. However, as we can see from the graph it is obvious that Netflix produces only modern TV-show and lacks some old classic.")
# ### Genres

# In[163]:


genres = list(itertools.chain(*list(Netflix_release["Genres"].dropna().apply(lambda x: x.split(",")))))
Genres_info = dict(sorted(Counter(genres).items(), key=lambda x: x[1], reverse=True))
gen = list(Genres_info.keys())
gen_data = list(Genres_info.values())
pie_fig = go.Figure(data=[go.Pie(labels=gen, values=gen_data)])
# pie_fig.write_html("genres_plot.html")
# pie_fig.show()
st.plotly_chart(pie_fig)

st.markdown(
    "The most popular genres on Netflix are Comedy and Drama. Other categories can be either expensive or unpopular for a big auditory which Netflix certainly has. All in all, there is nothing special about it.")
# ### Age and language

# In[170]:


ages = dict(Netflix_release["Age"].dropna().value_counts())
ages_fig = go.Figure(data=[go.Pie(labels=list(ages.keys())[:20:], values=list(ages.values())[:20:])])
# lang_fig.write_html("language_plot.html")
# ages_fig.show()
st.plotly_chart(ages_fig)

st.markdown(
    "Netflix is various in terms of age category. Many of its movies has 18+ rating. About 38% of movies were created for younger category.")
# In[162]:


Netflix_languages = list(itertools.chain(*list(Netflix_release["Language"].dropna().apply(lambda x: x.split(",")))))
languages = dict(sorted(Counter(Netflix_languages).items(), key=lambda x: x[1], reverse=True))
lang_fig = go.Figure(data=[go.Pie(labels=list(languages.keys())[:20:], values=list(languages.values())[:20:])])
# lang_fig.write_html("language_plot.html")
lang_fig.show()

st.markdown(
    "All mentioned before is available mostly on English languages. To sum it up, Netflix wants to create an entertainment for the whole family")

st.subheader("Directors")

# In[161]:


directors = list(itertools.chain(*list(Netflix_release["Directors"].dropna().apply(lambda x: x.split(",")))))
director = dict(sorted(Counter(directors).items(), key=lambda x: x[1], reverse=True))
dir_fig = go.Figure([go.Bar(x=list(director.keys())[:15:], y=list(director.values())[:15:])])
# dir_fig.write_html("directors_plot.html")
# dir_fig.show()
st.plotly_chart(dir_fig)

# In[155]:


dict(sorted(Counter(directors).items(), key=lambda x: x[1], reverse=True))

# In[156]:


Netflix_release[Netflix_release["Directors"].str.contains("Raúl Campos") == True].sort_values(by="IMDb")

# In[172]:


data[data["Directors"].str.contains("Jay Chapman") == True].sort_values(by="IMDb")

# In[173]:


data[data["Directors"].str.contains("Ron Howard") == True].sort_values(by="IMDb")

# In[174]:


data[data["Directors"].str.contains("Wilfred Jackson") == True].sort_values(by="IMDb")

st.header("Hulu")
st.subheader("Movie release")
st.markdown(
    "Hulu was created in 2007 and nowadays belongs to Disney. Amount of available movies is less comparing them to the other streaming platforms. As for the content, Hulu has smallest library of projects. However, in the recent years it started to fix this problem.")
st.subheader("Hulu genres")
st.markdown(
    "Genres are pretty similar to other streaming platforms. The biggest categories are Drama and Comedy. There is nothing special about that data.")
st.subheader("Age and language")
st.markdown(
    "Data is very similar to Netflix. The main age category is 18+ but categories for children or young adults are significantly lower in amount comparing them to Netflix categories. Small amount of project makes them more local to the countries where Hulu is available. Therefore, main language is English.")

st.header("Prime videos")
st.subheader("Movie release")
st.markdown(
    "Amazon has a significant amount of old movies in library. In fact it is the only streaming service which has a reach library of old school movies and also provides a lot of modern products.")
st.subheader("Prime videos genres")
st.markdown(
    "As well as everywhere, Drama and Comedy are top genres. However, Prime Videos has very balanced categories and provides something for everyone.")
st.subheader("Age and language")
st.markdown(
    "Prime Videos has the biggest 18+ category comparing to other streaming platforms. The content for children is available and balanced. However, it is still small enough.")
st.markdown(
    "There are not many languages available because Prime videos in unavailable in many countries around the world.")

st.header("Disney+ videos")
st.subheader("Movie release")
st.markdown(
    "Disney has the richest library of cartoons produced by themselves. There are many projects that were released 90+ years ago making Disney+ is one of the biggest family-friendly streaming platform of all time.")
st.subheader("Prime videos genres")
st.markdown(
    "Due to the company's specialization the main genre is family. Interesting thing is that Drama genre which is the most popular category on other platform takes 6 place in Disney+. Genres like Adventure and fantasy also more popular comparing them to other streaming platforms.")
st.subheader("Age and language")
st.markdown(
    "All category takes leading place among other ages. From graph it is obvious that Disney+ provides content for the whole family and avoids adult categories.")
st.markdown(
    "Disney+ is available only in a small amount of countries. Therefore, it is not a surprise that primary language is English.")

st.header("Overall")
st.subheader("Movie release")
st.markdown(
    "Overall, there are not many old movies available in such platforms like Netflix, Hulu, etc. There are many thing for that. Movie industry development, copyrights and other reasons make old movies outsider from the modern streaming platform.")
st.subheader("Genres")
st.markdown(
    "The most popular genre available on streaming platforms - Drama. Second place takes comedy. It is hard to say why only these two categories take leading places but we can assume that genres that evoke emotions in people make more money and make people more involved in movie.")
st.subheader("Age and Language")
st.markdown(
    "As well as Netflix, overall statistics shows that significant part of movies were created for adult auditory. Other categories have about 40% of the marking.")
st.markdown("English remains the main language for all streaming platforms.")

# In[166]:


dur = data.sort_values(by="IMDb")
fig = px.scatter(dur, x="Runtime", y="IMDb")
# fig.write_html("runtime_rating.html")
# fig.show()
st.plotly_chart(fig)

# There is no clear relation between movie runtime and its rating. As it can be seen from the graph all categories of duration have either bad or good marks. Therefore there is correlation between these parameters.

# In[158]:


age = data.sort_values(by="IMDb")
fig = px.scatter(age, y="Age", x="IMDb")
# fig.show()
st.plotly_chart(fig)
# fig.write_html("fig.html")


# Nothing depends on age category. :(

# In[168]:


countries = list(itertools.chain(*list(data["Country"].dropna().apply(lambda x: x.split(",")))))
country = dict(sorted(Counter(countries).items(), key=lambda x: x[1], reverse=True))
country_data = pd.DataFrame(list(country.items()), index=list(range(0, len(country.keys()))),
                            columns=["Country", "Movies"])

# In[167]:


fig = px.scatter_geo(country_data, locations="Country", color="Country", hover_name="Country", size="Movies",
                     projection="natural earth", locationmode="country names")
# fig.write_html("map.html")
# fig.show()
st.plotly_chart(fig)

st.markdown(
    "The main place filming is USA. Majority of movies and TV-series were filmed there. Being an American company netflix prefer to hire directors in English speaking countries like USA and Britain. However, almost 900 projects were created in India. For some reasons directors from this country create twice more movies than USA or British directors.")
