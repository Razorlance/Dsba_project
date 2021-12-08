import pandas as pd
import numpy as np
import itertools
from collections import Counter

overall_data = {}
netflix_data = {}
hulu_data = {}
disney_data = {}
prime_data = {}

orginal_data = pd.read_csv('data.csv', sep=',')
data = orginal_data.copy(deep=True)
last_year = data[(data["Year"] == 2020)]

# Overall calculations


# Netflix calculations

Netflix_data = last_year[last_year["Netflix"] == 1]

# IMdB

netflix_data['imdb_mean'] = Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).mean().round(3)
netflix_data['imdb_median'] = Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).median()
netflix_data['imdb_std'] = Netflix_data["IMDb"].apply(lambda x: float(str(x)[:3])).std().round(3)

# Rotten tomatoes

netflix_data['RT_mean'] = Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).mean().round(3)
netflix_data['RT_median'] = Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).median()
netflix_data['RT_std'] = Netflix_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).std().round(3)

# Release year
Netflix_release = data[(data["Netflix"] == 1)]
netflix_years = Netflix_release["Year"].value_counts()
netflix_data['years'] = list(dict(sorted(netflix_years.items(), key=lambda x: x[0])).keys())
netflix_data['years_data'] = list(dict(sorted(netflix_years.items(), key=lambda x: x[0])).values())

# Genres

genres = list(itertools.chain(*list(Netflix_release["Genres"].dropna().apply(lambda x: x.split(",")))))
netflix_data["genres"] = list(map(str, Counter(genres).keys()))
netflix_data["genres_data"] = list(Counter(genres).values())

# Hulu calculations

# Disney calculations

# Amazon Prime calculations
