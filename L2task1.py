import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 1: Analyze the distribution of aggregate ratings
plt.figure(figsize=(10, 6))
df['Aggregate rating'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Number of Restaurants')
plt.show()

# Task 1: Determine the most common rating range
most_common_rating_range = df['Aggregate rating'].mode().values
print("\nMost Common Rating Range:", most_common_rating_range)

# Task 1: Calculate the average number of votes received by restaurants
average_votes_received = df['Votes'].mean()
print("\nAverage Number of Votes Received by Restaurants:", round(average_votes_received, 2))
