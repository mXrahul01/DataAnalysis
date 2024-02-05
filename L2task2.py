import pandas as pd
import itertools
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 2: Identify the most common combinations of cuisines
cuisine_combinations = df['Cuisines'].str.split(', ').dropna()
all_cuisine_list = list(itertools.chain.from_iterable(cuisine_combinations))
most_common_cuisine_combinations = pd.Series(all_cuisine_list).value_counts().head(5)
print("Most Common Cuisine Combinations:")
print(most_common_cuisine_combinations)

# Task 2: Determine if certain cuisine combinations tend to have higher ratings
average_ratings_by_cuisine_combination = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print("\nAverage Ratings by Cuisine Combination:")
print(average_ratings_by_cuisine_combination.head(5))

# Visualize the top 5 most common cuisine combinations
plt.figure(figsize=(10, 6))
most_common_cuisine_combinations.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 5 Most Common Cuisine Combinations')
plt.xlabel('Cuisine Combination')
plt.ylabel('Number of Restaurants')
plt.show()
