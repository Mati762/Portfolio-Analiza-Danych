import pandas as pd

df = pd.read_csv('../Dane/video_games.csv')

print("Rozmiar tabeli:",df.shape)
print(df.head(5))

print("Brakujace dane\n",df.isnull().sum())

df_clean = df.dropna(subset=['game'])
print(df_clean)

sorted_desc = df.sort_values(by=['price'], ascending=False)
print(sorted_desc.head()[['game', 'price']])



