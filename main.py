import pandas as pd
import numpy as np
anime = pd.read_csv('c:/Users/djidjikov/python/anime.csv')
rating = pd.read_csv('c:/Users/djidjikov/python/rating.csv')
anime_modified = anime.set_index('name')

df = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Stick Maker']], 
columns=['id','name', 'occupation'])

#789
print(anime)