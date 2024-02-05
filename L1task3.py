import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 3: Price Range Distribution - Visualization
plt.figure(figsize=(10, 6))
df['Price range'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Price Range Distribution Among Restaurants')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.show()

# Task 3: Calculate the percentage of restaurants in each price range category
total_restaurants = len(df)
percentage_per_price_range = (df['Price range'].value_counts() / total_restaurants) * 100

print("\nPercentage of Restaurants in Each Price Range Category:")
print(percentage_per_price_range)
