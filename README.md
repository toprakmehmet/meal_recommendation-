## Meal Recommendation
![header](https://github.com/toprakmehmet/meal_recommendation-/blob/master/pics/macrofit-meals.jpg)

## Description 
Using a content based recommendation system, this project recommends the 10 most similar meals based on ingredients.
  - Scraped data from ​https://www.allrecipes.com/
  - Gathered meal content information from ~21k meals (​Breakfast: 3790, Lunch: 1257, Dinner : 1302, Dessert: 15461​)
  - Dropped 2415 characters (teaspoon, tablespoon, cups, bag, numbers, symbols, brands etc) to improve results
  - Used ​TfidfVectorizer and cosine similarity to create best content based recommendation system
  - Built a content based filtration system and application interface using Streamlit and Pandas


## Python Tools:
   - Pandas
   - Beautifulsoup
   - TfidfVectorizer
   - Cosine Similarity
   - Content Based Recommendation System

## Visualization of Model Confusion Matrix 
## Baseline Model
![img](https://github.com/toprakmehmet/pokemon_types/blob/master/pics/baseline_conf_martix.png)
  

## Future Applications
As one of many avid pokemone fans out there. This model can assist in detemining the type of each pokemon and help trainers all over the digital universe to be the very best. As the nintendo company keeps releaseing new pokemone with every generation, this model can also be used to predict the type of pokemon that will be released as Pokemon does try to keep a balance in their creations.
