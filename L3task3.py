import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Task 3: Analyze the relationship between price range and availability of online delivery and table booking
price_range_counts = df['Price range'].value_counts()
online_delivery_counts = df.groupby('Price range')['Has Online delivery'].value_counts().unstack().fillna(0)
table_booking_counts = df.groupby('Price range')['Has Table booking'].value_counts().unstack().fillna(0)

# Plot the relationship between price range and availability of online delivery
plt.figure(figsize=(12, 6))
online_delivery_counts.plot(kind='bar', stacked=True, color=['skyblue', 'orange'], edgecolor='black')
plt.title('Relationship between Price Range and Online Delivery')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.legend(title='Has Online Delivery', loc='upper right')
plt.show()

# Plot the relationship between price range and availability of table booking
plt.figure(figsize=(12, 6))
table_booking_counts.plot(kind='bar', stacked=True, color=['skyblue', 'orange'], edgecolor='black')
plt.title('Relationship between Price Range and Table Booking')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.legend(title='Has Table Booking', loc='upper right')
plt.show()

# Task 3: Determine if higher-priced restaurants are more likely to offer online delivery and table booking
higher_priced_restaurants = df[df['Price range'] == 4]
online_delivery_percentage_higher_priced = (higher_priced_restaurants['Has Online delivery'].value_counts(normalize=True) * 100).round(2)
table_booking_percentage_higher_priced = (higher_priced_restaurants['Has Table booking'].value_counts(normalize=True) * 100).round(2)

print("\nPercentage of Higher-Priced Restaurants Offering Online Delivery:")
print(online_delivery_percentage_higher_priced)

print("\nPercentage of Higher-Priced Restaurants Offering Table Booking:")
print(table_booking_percentage_higher_priced)
