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

Netflix_genres = list(itertools.chain(*list(Netflix_release["Genres"].dropna().apply(lambda x: x.split(",")))))
Genres_info = dict(sorted(Counter(Netflix_genres).items(), key=lambda x: x[1], reverse=True))
netflix_data["genres"] = list(Genres_info.keys())[:10:]
netflix_data["genres"].append("Others")
netflix_data["genres_data"] = list(Genres_info.values())[:10:]
netflix_data["genres_data"].append(sum(list(Genres_info.values())[11::]))

# Languages and age

Netflix_ages = dict(Netflix_release["Age"].dropna().value_counts())
netflix_data["ages"] = list(Netflix_ages.keys())
netflix_data["ages_data"] = list(Netflix_ages.values())

Netflix_languages = list(itertools.chain(*list(Netflix_release["Language"].dropna().apply(lambda x: x.split(",")))))
Netflix_languages = dict(sorted(Counter(Netflix_languages).items(), key=lambda x: x[1], reverse=True))
netflix_data["languages"] = list(Netflix_languages.keys())[:10:]
netflix_data["languages_data"] = list(Netflix_languages.values())[:10:]

# Directors

Netflix_directors = list(itertools.chain(*list(Netflix_release["Directors"].dropna().apply(lambda x: x.split(",")))))
Netflix_directors = dict(sorted(Counter(Netflix_directors).items(), key=lambda x: x[1], reverse=True))
netflix_data["directors"] = list(Netflix_directors.keys())[:15:]
netflix_data["directors_data"] = list(Netflix_directors.values())[:15:]
# Hulu calculations

# Disney calculations

# Amazon Prime calculations
