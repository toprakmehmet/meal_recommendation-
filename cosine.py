import pickle
import pandas as pd
with open('cosine_sim.pickle', 'rb') as file:
   cosine_sim = pickle.load(file)
df = pd.read_csv('Ingredient_lists_last.csv')

indices = pd.Series(df.index, index=df['Name'])


meal = sorted(df.Name, key=lambda x: x[0])
