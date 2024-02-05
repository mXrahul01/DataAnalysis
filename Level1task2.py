import pandas as pd

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 2: Identify the city with the highest number of restaurants
city_with_highest_restaurants = df['City'].value_counts().idxmax()
print("City with the Highest Number of Restaurants:", city_with_highest_restaurants)

# Task 2: Calculate the average rating for restaurants in each city
average_rating_by_city = df.groupby('City')['Aggregate rating'].mean()

# Task 2: Determine the city with the highest average rating
city_with_highest_avg_rating = average_rating_by_city.idxmax()
highest_avg_rating = average_rating_by_city.max()

print("\nAverage Rating for Restaurants in Each City:")
print(average_rating_by_city)

print("\nCity with the Highest Average Rating:", city_with_highest_avg_rating)
print("Highest Average Rating:", highest_avg_rating)
