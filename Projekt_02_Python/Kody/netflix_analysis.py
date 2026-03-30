import pandas as pd

df = pd.read_csv('../Dane/netflix_titles.csv')

print("--- 1. CLEANING MISSING DIRECTORS ---")
df['director'] = df['director'].fillna('Unknown')
print(f"Missing directors now: {df['director'].isnull().sum()}")
print("\n--- 2. FILTERING ONLY MOVIES ---")
df_movies = df[df['type'] == 'Movie'].copy()
print(f"We now have {df_movies.shape[0]} movies to analyze.")
print("\n--- 3. FIXING THE DURATION COLUMN ---")
df_movies['duration'] = df_movies['duration'].str.replace(' min', '').astype(int)
longest_movie = df_movies['duration'].max()
print(f"The longest movie on Netflix is {longest_movie} minutes long!")
longest_movie_time = df_movies['duration'].max()
print(f"Max duration: {longest_movie_time} minutes")
longest_movie_row = df_movies[df_movies['duration'] == longest_movie_time]
print("\n--- THE LONGEST MOVIE ON NETFLIX IS: ---")
print(longest_movie_row[['title', 'duration']])
print("\n---- MOVIE RELEASED IN THE YEAR 1942 ---")
movie_released_1942 = df_movies[df_movies['release_year'] == 1942]
print(movie_released_1942[['title', 'release_year']])