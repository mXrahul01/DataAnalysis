import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 4: Identify if there are any restaurant chains present in the dataset
restaurant_chains = df['Restaurant Name'].value_counts()
restaurant_chains = restaurant_chains[restaurant_chains > 1]

if not restaurant_chains.empty:
    print("Restaurant Chains Present in the Dataset:")
    print(restaurant_chains)
else:
    print("No Restaurant Chains Found in the Dataset.")

# Task 4: Analyze the ratings and popularity of different restaurant chains
if not restaurant_chains.empty:
    ratings_by_chain = df.groupby('Restaurant Name')['Aggregate rating'].mean()
    popularity_by_chain = df.groupby('Restaurant Name')['Votes'].sum()

    # Visualize the top 5 restaurant chains by average rating
    top_rated_chains = ratings_by_chain.nlargest(5)
    print("\nTop 5 Restaurant Chains by Average Rating:")
    print(top_rated_chains)

    # Visualize the top 5 restaurant chains by popularity (total votes)
    top_popular_chains = popularity_by_chain.nlargest(5)
    print("\nTop 5 Restaurant Chains by Popularity (Total Votes):")
    print(top_popular_chains)

    # Plot the top 5 restaurant chains by average rating
    plt.figure(figsize=(12, 6))
    top_rated_chains.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Top 5 Restaurant Chains by Average Rating')
    plt.xlabel('Restaurant Chain')
    plt.ylabel('Average Rating')
    plt.show()

    # Plot the top 5 restaurant chains by popularity
    plt.figure(figsize=(12, 6))
    top_popular_chains.plot(kind='bar', color='orange', edgecolor='black')
    plt.title('Top 5 Restaurant Chains by Popularity (Total Votes)')
    plt.xlabel('Restaurant Chain')
    plt.ylabel('Total Votes')
    plt.show()
