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

# Netflix calculations

Netflix_data = data[data["Netflix"] == 1]

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

# Amazon Prime calculations

Prime_data = data[data["Prime Video"] == 1]

# IMdB

prime_data['imdb_mean'] = Prime_data["IMDb"].apply(lambda x: float(str(x)[:3])).mean().round(3)
prime_data['imdb_median'] = Prime_data["IMDb"].apply(lambda x: float(str(x)[:3])).median()
prime_data['imdb_std'] = Prime_data["IMDb"].apply(lambda x: float(str(x)[:3])).std().round(3)

# Rotten tomatoes

prime_data['RT_mean'] = Prime_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).mean().round(3)
prime_data['RT_median'] = Prime_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).median()
prime_data['RT_std'] = Prime_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).std().round(3)

# Release year
Prime_release = Prime_data
prime_years = Prime_release["Year"].value_counts()
prime_data['years'] = list(dict(sorted(prime_years.items(), key=lambda x: x[0])).keys())
prime_data['years_data'] = list(dict(sorted(prime_years.items(), key=lambda x: x[0])).values())

# Genres

Prime_genres = list(itertools.chain(*list(Prime_release["Genres"].dropna().apply(lambda x: x.split(",")))))
Genres_info = dict(sorted(Counter(Prime_genres).items(), key=lambda x: x[1], reverse=True))
prime_data["genres"] = list(Genres_info.keys())[:10:]
prime_data["genres"].append("Others")
prime_data["genres_data"] = list(Genres_info.values())[:10:]
prime_data["genres_data"].append(sum(list(Genres_info.values())[11::]))

# Languages and age

Prime_ages = dict(Prime_release["Age"].dropna().value_counts())
prime_data["ages"] = list(Prime_ages.keys())
prime_data["ages_data"] = list(Prime_ages.values())

Prime_languages = list(itertools.chain(*list(Prime_release["Language"].dropna().apply(lambda x: x.split(",")))))
Prime_languages = dict(sorted(Counter(Prime_languages).items(), key=lambda x: x[1], reverse=True))
prime_data["languages"] = list(Prime_languages.keys())[:10:]
prime_data["languages_data"] = list(Prime_languages.values())[:10:]

# Directors

Prime_directors = list(itertools.chain(*list(Prime_release["Directors"].dropna().apply(lambda x: x.split(",")))))
Prime_directors = dict(sorted(Counter(Prime_directors).items(), key=lambda x: x[1], reverse=True))
prime_data["directors"] = list(Prime_directors.keys())[:15:]
prime_data["directors_data"] = list(Prime_directors.values())[:15:]

Disney_data = data[data["Disney+"] == 1]

# IMdB

disney_data['imdb_mean'] = Disney_data["IMDb"].apply(lambda x: float(str(x)[:3])).mean().round(3)
disney_data['imdb_median'] = Disney_data["IMDb"].apply(lambda x: float(str(x)[:3])).median()
disney_data['imdb_std'] = Disney_data["IMDb"].apply(lambda x: float(str(x)[:3])).std().round(3)

# Rotten tomatoes

disney_data['RT_mean'] = Disney_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).mean().round(3)
disney_data['RT_median'] = Disney_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).median()
disney_data['RT_std'] = Disney_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).std().round(3)

# Release year
Disney_release = Disney_data
disney_years = Disney_release["Year"].value_counts()
disney_data['years'] = list(dict(sorted(disney_years.items(), key=lambda x: x[0])).keys())
disney_data['years_data'] = list(dict(sorted(disney_years.items(), key=lambda x: x[0])).values())

# Genres

Disney_genres = list(itertools.chain(*list(Disney_release["Genres"].dropna().apply(lambda x: x.split(",")))))
Genres_info = dict(sorted(Counter(Disney_genres).items(), key=lambda x: x[1], reverse=True))
disney_data["genres"] = list(Genres_info.keys())[:10:]
disney_data["genres"].append("Others")
disney_data["genres_data"] = list(Genres_info.values())[:10:]
disney_data["genres_data"].append(sum(list(Genres_info.values())[11::]))

# Languages and age

Disney_ages = dict(Disney_release["Age"].dropna().value_counts())
disney_data["ages"] = list(Disney_ages.keys())
disney_data["ages_data"] = list(Disney_ages.values())

Disney_languages = list(itertools.chain(*list(Disney_release["Language"].dropna().apply(lambda x: x.split(",")))))
Disney_languages = dict(sorted(Counter(Disney_languages).items(), key=lambda x: x[1], reverse=True))
disney_data["languages"] = list(Disney_languages.keys())[:10:]
disney_data["languages_data"] = list(Disney_languages.values())[:10:]

# Directors

Disney_directors = list(itertools.chain(*list(Disney_release["Directors"].dropna().apply(lambda x: x.split(",")))))
Disney_directors = dict(sorted(Counter(Disney_directors).items(), key=lambda x: x[1], reverse=True))
disney_data["directors"] = list(Disney_directors.keys())[:15:]
disney_data["directors_data"] = list(Disney_directors.values())[:15:]

# Hulu

Hulu_data = data[data["Hulu"] == 1]

# IMdB

hulu_data['imdb_mean'] = Hulu_data["IMDb"].apply(lambda x: float(str(x)[:3])).mean().round(3)
hulu_data['imdb_median'] = Hulu_data["IMDb"].apply(lambda x: float(str(x)[:3])).median()
hulu_data['imdb_std'] = Hulu_data["IMDb"].apply(lambda x: float(str(x)[:3])).std().round(3)

# Rotten tomatoes

hulu_data['RT_mean'] = Hulu_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).mean().round(3)
hulu_data['RT_median'] = Hulu_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).median()
hulu_data['RT_std'] = Hulu_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).std().round(3)

# Release year
Hulu_release = Hulu_data
hulu_years = Hulu_release["Year"].value_counts()
hulu_data['years'] = list(dict(sorted(hulu_years.items(), key=lambda x: x[0])).keys())
hulu_data['years_data'] = list(dict(sorted(hulu_years.items(), key=lambda x: x[0])).values())

# Genres

Hulu_genres = list(itertools.chain(*list(Hulu_release["Genres"].dropna().apply(lambda x: x.split(",")))))
Genres_info = dict(sorted(Counter(Hulu_genres).items(), key=lambda x: x[1], reverse=True))
hulu_data["genres"] = list(Genres_info.keys())[:10:]
hulu_data["genres"].append("Others")
hulu_data["genres_data"] = list(Genres_info.values())[:10:]
hulu_data["genres_data"].append(sum(list(Genres_info.values())[11::]))

# Languages and age

Hulu_ages = dict(Hulu_release["Age"].dropna().value_counts())
hulu_data["ages"] = list(Hulu_ages.keys())
hulu_data["ages_data"] = list(Hulu_ages.values())

Hulu_languages = list(itertools.chain(*list(Hulu_release["Language"].dropna().apply(lambda x: x.split(",")))))
Hulu_languages = dict(sorted(Counter(Hulu_languages).items(), key=lambda x: x[1], reverse=True))
hulu_data["languages"] = list(Hulu_languages.keys())[:10:]
hulu_data["languages_data"] = list(Hulu_languages.values())[:10:]

# Directors

Hulu_directors = list(itertools.chain(*list(Hulu_release["Directors"].dropna().apply(lambda x: x.split(",")))))
Hulu_directors = dict(sorted(Counter(Hulu_directors).items(), key=lambda x: x[1], reverse=True))
hulu_data["directors"] = list(Hulu_directors.keys())[:15:]
hulu_data["directors_data"] = list(Hulu_directors.values())[:15:]

# Overall

Overall_data = data

# IMdB

overall_data['imdb_mean'] = Overall_data["IMDb"].apply(lambda x: float(str(x)[:3])).mean().round(3)
overall_data['imdb_median'] = Overall_data["IMDb"].apply(lambda x: float(str(x)[:3])).median()
overall_data['imdb_std'] = Overall_data["IMDb"].apply(lambda x: float(str(x)[:3])).std().round(3)

# Rotten tomatoes

overall_data['RT_mean'] = Overall_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).mean().round(3)
overall_data['RT_median'] = Overall_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).median()
overall_data['RT_std'] = Overall_data["Rotten Tomatoes"].dropna().apply(lambda x: float(str(x)[:2])).std().round(3)

# Release year
Overall_release = Overall_data
overall_years = Overall_release["Year"].value_counts()
overall_data['years'] = list(dict(sorted(overall_years.items(), key=lambda x: x[0])).keys())
overall_data['years_data'] = list(dict(sorted(overall_years.items(), key=lambda x: x[0])).values())

# Genres

Overall_genres = list(itertools.chain(*list(Overall_release["Genres"].dropna().apply(lambda x: x.split(",")))))
Genres_info = dict(sorted(Counter(Overall_genres).items(), key=lambda x: x[1], reverse=True))
overall_data["genres"] = list(Genres_info.keys())[:10:]
overall_data["genres"].append("Others")
overall_data["genres_data"] = list(Genres_info.values())[:10:]
overall_data["genres_data"].append(sum(list(Genres_info.values())[11::]))

# Languages and age

Overall_ages = dict(Overall_release["Age"].dropna().value_counts())
overall_data["ages"] = list(Overall_ages.keys())
overall_data["ages_data"] = list(Overall_ages.values())

Overall_languages = list(itertools.chain(*list(Overall_release["Language"].dropna().apply(lambda x: x.split(",")))))
Overall_languages = dict(sorted(Counter(Overall_languages).items(), key=lambda x: x[1], reverse=True))
overall_data["languages"] = list(Overall_languages.keys())[:10:]
overall_data["languages_data"] = list(Overall_languages.values())[:10:]

# Directors

Overall_directors = list(itertools.chain(*list(Overall_release["Directors"].dropna().apply(lambda x: x.split(",")))))
Overall_directors = dict(sorted(Counter(Overall_directors).items(), key=lambda x: x[1], reverse=True))
overall_data["directors"] = list(Overall_directors.keys())[:15:]
overall_data["directors_data"] = list(Overall_directors.values())[:15:]
