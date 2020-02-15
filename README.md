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

## Raw Data
![img](https://github.com/toprakmehmet/meal_recommendation-/blob/master/pics/raw_most_used_ingredients.png)

## Clean Data
![img](https://github.com/toprakmehmet/meal_recommendation-/blob/master/pics/most_used_ingredient.png)

## Most Used Ingredients
# Breakfast
![img](https://github.com/toprakmehmet/meal_recommendation-/blob/master/pics/breakfast_popular_ingredients.png)

# Lunch
![img](https://github.com/toprakmehmet/meal_recommendation-/blob/master/pics/lunch_popular_ingredients.png)

# Dinner
![img](https://github.com/toprakmehmet/meal_recommendation-/blob/master/pics/dinner_popular_ingredients.png)

# Dessert
![img](https://github.com/toprakmehmet/meal_recommendation-/blob/master/pics/dessert_popular_ingredients.png)
  

## Demo of the Project with Streamlit
 Please see the below link
https://drive.google.com/file/d/137RQtVJbKYg9_Zq37oktPsjz9c3R7vfa/view?usp=sharing
