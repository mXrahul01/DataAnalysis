import pandas as pd

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 4: Determine the percentage of restaurants that offer online delivery
percentage_online_delivery = (df['Has Online delivery'].value_counts(normalize=True) * 100).round(2)
print("Percentage of Restaurants Offering Online Delivery:")
print(percentage_online_delivery)

# Task 4: Compare the average ratings of restaurants with and without online delivery
average_rating_with_delivery = df[df['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()
average_rating_without_delivery = df[df['Has Online delivery'] == 'No']['Aggregate rating'].mean()

print("\nAverage Rating of Restaurants with Online Delivery:", round(average_rating_with_delivery, 2))
print("Average Rating of Restaurants without Online Delivery:", round(average_rating_without_delivery, 2))
