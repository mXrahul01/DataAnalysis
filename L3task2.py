import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 2: Identify restaurants with the highest and lowest number of votes
restaurant_highest_votes = df.loc[df['Votes'].idxmax()]
restaurant_lowest_votes = df.loc[df['Votes'].idxmin()]

print("\nRestaurant with the Highest Number of Votes:")
print(restaurant_highest_votes[['Restaurant Name', 'Votes', 'Aggregate rating']])

print("\nRestaurant with the Lowest Number of Votes:")
print(restaurant_lowest_votes[['Restaurant Name', 'Votes', 'Aggregate rating']])

# Task 2: Analyze correlation between the number of votes and restaurant rating
plt.figure(figsize=(10, 6))
plt.scatter(df['Votes'], df['Aggregate rating'], alpha=0.5)
plt.title('Correlation between Number of Votes and Restaurant Rating')
plt.xlabel('Number of Votes')
plt.ylabel('Aggregate Rating')
plt.show()

# Calculate correlation coefficient
correlation_coefficient = df['Votes'].corr(df['Aggregate rating'])
print("\nCorrelation Coefficient between Number of Votes and Restaurant Rating:", round(correlation_coefficient, 2))
