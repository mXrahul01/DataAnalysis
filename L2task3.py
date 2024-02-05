import pandas as pd
import folium

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Create a folium map centered around the mean latitude and longitude
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

# Add markers for each restaurant
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(restaurant_map)

# Save the map as an HTML file
restaurant_map.save('restaurant_locations_map.html')
