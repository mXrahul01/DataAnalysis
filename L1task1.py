import pandas as pd

# Provide the corrected absolute path to the CSV file
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'

# Load the dataset
df = pd.read_csv(dataset_path)


# Check the structure of the dataset
print(df.head())

# Task 1: Top Cuisines
top_cuisines = df['Cuisines'].str.split(', ', expand=True).stack().value_counts().nlargest(3)
print("Top Three Cuisines:")
print(top_cuisines)

# Task 1: Calculate the percentage of restaurants serving each top cuisine
total_restaurants = len(df)
percentage_per_cuisine = (top_cuisines / total_restaurants) * 100
print("\nPercentage of Restaurants Serving Each Top Cuisine:")
print(percentage_per_cuisine)
